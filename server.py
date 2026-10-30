import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx

BASE = "https://api.india.delta.exchange"
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(timeout=18, headers={"Accept":"application/json","User-Agent":"IndiaTradingCoach-PWA/1.0"})
    yield
    await app.state.http.aclose()

app = FastAPI(title="Delta Exchange Trading Coach", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home():
    return FileResponse("static/index.html")

@app.get("/manifest.webmanifest")
async def manifest():
    return FileResponse("static/manifest.webmanifest", media_type="application/manifest+json")

@app.get("/sw.js")
async def sw():
    return FileResponse("static/sw.js", media_type="application/javascript")

@app.get("/api/products")
async def products(contract_types: str = "perpetual_futures,call_options,put_options", states: str = "live", page_size: int = 100):
    try:
        r = await app.state.http.get(BASE+"/v2/products", params={"contract_types":contract_types,"states":states,"page_size":min(max(page_size,1),200)})
        r.raise_for_status()
        return r.json()
    except httpx.HTTPError as e:
        raise HTTPException(502, f"Delta products API unavailable: {str(e)[:200]}")

@app.get("/api/tickers")
async def tickers(symbol: str | None = None):
    try:
        params = {"symbol":symbol} if symbol else {}
        r = await app.state.http.get(BASE+"/v2/tickers", params=params)
        r.raise_for_status()
        return r.json()
    except httpx.HTTPError as e:
        raise HTTPException(502, f"Delta ticker API unavailable: {str(e)[:200]}")

@app.get("/api/candles")
async def candles(symbol: str, resolution: str = "5m", start: int | None = None, end: int | None = None):
    if resolution not in {"1m","3m","5m","15m","30m","1h","2h","4h","6h","12h","1d","1w"}:
        raise HTTPException(400, "Unsupported candle resolution")
    if not start or not end:
        raise HTTPException(400, "start and end Unix timestamps are required")
    try:
        r = await app.state.http.get(BASE+"/v2/history/candles", params={"symbol":symbol,"resolution":resolution,"start":start,"end":end})
        r.raise_for_status()
        return r.json()
    except httpx.HTTPError as e:
        raise HTTPException(502, f"Delta candles API unavailable: {str(e)[:200]}")

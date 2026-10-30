# Delta Trading Coach (India)

Mobile-first Progressive Web App for Delta Exchange India public market data.
It is **analysis only**. No account login, API key, API secret, order, position or wallet endpoint is included.

## Run locally
1. Install Python 3.10+.
2. Extract this ZIP.
3. In the extracted folder run:
   - Windows: double-click `run.bat`
   - macOS/Linux: `bash run.sh`
4. Open `http://127.0.0.1:8000`.

Public market data does not require Delta API credentials. This app connects to:
- REST: `https://api.india.delta.exchange`
- Public WebSocket: `wss://public-socket.india.delta.exchange`

## Install on Android home screen
A true installable PWA needs to be served from HTTPS (or localhost on the same device). After hosting this folder on an HTTPS server:
1. Open the HTTPS app URL in Chrome on Android.
2. Tap the app's **Install App** prompt, or Chrome ⋮ → **Add to Home screen** / **Install app**.
3. The app icon appears on the home screen and opens in standalone app view.

If you run it on a laptop and open it on your phone over plain `http://192.168...`, Chrome may not offer PWA installation because that is not a secure context. Use HTTPS hosting for installation. Do not expose the local server publicly without proper security review.

## Included
- Delta India live public WebSocket ticker
- Live candle updates (1m–1d supported resolutions)
- Historical candles through REST API
- Public live products list for futures and options
- Option ticker Greeks/IV where supplied in ticker payload
- EMA-based context, position risk calculator, local journal
- PWA manifest, service worker and home-screen icon

## Limitations
- The market context is simple EMA analysis, not AI and not a guaranteed buy/sell signal.
- The chart displays OHLC candles but does not include advanced drawing tools, historical tick replay, or a strategy backtest.
- Product list pagination is limited to the first page in this starter build.
- Contract multiplier, fees, funding, leverage, liquidation price and margin must be verified on Delta before a trade.
- The app stores journal entries in the browser's local storage on that device.
- A stable network and exchange availability are required for live data.

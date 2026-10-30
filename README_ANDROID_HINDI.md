# Delta Exchange Trading Coach — Android पर चलाने का तरीका

यह प्रोजेक्ट Android-friendly Progressive Web App (PWA) है। इसे Chrome से install करके home screen पर सामान्य ऐप की तरह खोला जा सकता है। यह अभी signed APK नहीं है।

## सबसे आसान तरीका: एक बार HTTPS पर host करें

1. इस पूरे folder को GitHub repository में upload करें। `server.py`, `requirements.txt`, `render.yaml`, `Procfile` और `static/` folder repository के root में होने चाहिए।
2. Render.com पर account बनाएं और **New → Blueprint** चुनें। अपनी GitHub repository connect करें। Render `render.yaml` पढ़कर service deploy करेगा।
3. Deploy पूरा होने पर Render आपको HTTPS URL देगा, जैसे `https://your-app.onrender.com`।
4. अपने Android फोन में Chrome खोलकर यह URL खोलें।
5. Chrome के ⋮ menu में **Install app** या **Add to Home screen** दबाएं।
6. Home screen पर Delta Coach icon आ जाएगा। उसे दबाकर ऐप खोलें।

## जरूरी बातें

- Live market data के लिए इंटरनेट और Delta Exchange India की public API/WebSocket उपलब्ध होना जरूरी है।
- App public market data पढ़ता है। इसमें Delta account login, API secret या order placement शामिल नहीं है।
- यह analysis/risk-coaching tool है, guaranteed trading signal नहीं। Trade से पहले contract size, fees, margin और liquidation details Delta पर verify करें।
- Render की free service idle रहने पर sleep हो सकती है; पहली बार खुलने पर कुछ समय लग सकता है। अधिक reliable always-on use के लिए suitable paid hosting लें।
- APK चाहिए तो पहले app को HTTPS पर deploy करना होगा; उसके बाद Android wrapper/TWA बनाकर signed APK अलग से compile करना पड़ेगा।

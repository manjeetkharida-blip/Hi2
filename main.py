import asyncio
import json
import random
import string
import time
import uuid
import base64
import requests
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketDisconnect
import os
import threading
import sys

app = FastAPI()

# --- UI & CONFIG ---
@app.get("/", response_class=HTMLResponse)
async def index():
    return open("index.html").read()

# Global State
state = {
    "running": False,
    "hits": 0,
    "misses": 0,
    "threads": 0,
    "token": "",
    "chat_id": ""
}

ws_clients = []

class HunterThread(threading.Thread):
    def __init__(self, token, chat_id):
        super().__init__(daemon=True)
        self.token = token
        self.chat_id = chat_id
        self.used_usernames = set()
        self.lock = threading.Lock()

    def run(self):
        while state["running"]:
            prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 7)))
            domain = random.choice(["hi2.in", "telegmail.com"])
            email = f"{prefix}@{domain}"

            if prefix in self.used_usernames:
                continue
            
            # Check IG Bloks
            try:
                device = str(uuid.uuid4())
                family = str(uuid.uuid4())
                android = "android-" + uuid.uuid4().hex[:16]
                brands = ["samsung", "Google", "Xiaomi", "OnePlus"]
                models = ["SM-G973F", "Pixel 7", "M2102J20SG"]
                brand = random.choice(brands)
                model = random.choice(models)
                dpi = random.choice(["420", "450"])
                res = random.choice(["1080x2280", "1080x2400"])
                android_ver = random.choice(["11", "12", "13", "14"])
                insta_ver = random.choice([280, 290, 300, 310])
                ua = f"Instagram {insta_ver}.0.0.{random.randint(10,99)} Android ({android_ver}; {dpi}dpi; {res}; {brand}; {model}; en_US)"
                
                payload = {
                    'params': json.dumps({
                        "client_input_params": {
                            "search_query": email,
                            "is_whatsapp_installed": 1,
                            "ig_android_qe_device_id": device,
                            "text_input_id": f"akyuf0:{random.randint(50, 70)}"
                        },
                        "server_params": {
                            "device_id": android,
                            "family_device_id": family
                        }
                    }),
                    'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
                }
                headers = {
                    'User-Agent': ua,
                    'x-ig-android-id': android,
                    'x-ig-device-id': device,
                    'x-ig-family-device-id': family,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                
                r = requests.post("https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/", 
                                  data=payload, headers=headers, timeout=15)
                
                hit = email.lower() in r.text.lower()
                
                with self.lock:
                    if hit:
                        state["hits"] += 1
                        msg = f"🎯 HIT: {email}\n@{prefix}"
                        self.send_telegram(msg)
                        # Send to Web UI
                        for client in list(ws_clients):
                            try:
                                asyncio.run_coroutine_threadsafe(client.send_json({"type": "log", "msg": msg, "hit": True}), None)
                            except:
                                pass
                    else:
                        state["misses"] += 1
                    
                    self.used_usernames.add(prefix)
                    
            except Exception:
                pass
            time.sleep(0.5)

    def send_telegram(self, text):
        try:
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", 
                          data={"chat_id": self.chat_id, "text": text}, timeout=10)
        except:
            pass

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    ws_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        if websocket in ws_clients:
            ws_clients.remove(websocket)

@app.post("/start")
async def start_hunter(request: Request):
    body = await request.json()
    token = body.get('token')
    chat_id = body.get('chat_id')
    
    if not token or not chat_id:
        return {"status": "error", "message": "Missing credentials"}

    state["token"] = token
    state["chat_id"] = chat_id
    state["running"] = True
    state["threads"] += 1
    
    t = HunterThread(token, chat_id)
    t.start()
    
    return {"status": "started", "threads": state["threads"]}

@app.post("/stop")
async def stop_hunter():
    state["running"] = False
    state["threads"] = 0
    return {"status": "stopped"}

@app.get("/stats")
async def get_stats():
    return JSONResponse(state)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

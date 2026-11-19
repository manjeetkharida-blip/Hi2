import asyncio
import json
import random
import string
import time
import uuid
import base64
import requests
from fastapi import FastAPI, WebSocket, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import os
import threading
import sys
import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

# --- APP SETUP ---
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- DATABASE SETUP (SQLite) ---
DB_FILE = "hunter.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Users Table
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)''')
    # Hits Table
    c.execute('''CREATE TABLE IF NOT EXISTS hits 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, email TEXT, username TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# Global State
state = {
    "running": False,
    "threads": 0,
    "token": "",
    "chat_id": ""
}

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
                        msg = f"🎯 HIT: {email}\n@{prefix}"
                        self.send_telegram(msg)
                        self.save_to_db(email, prefix)
                    else:
                        pass
                    
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

    def save_to_db(self, email, username):
        """Saves hit to SQLite"""
        try:
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            # We need a default user_id if not logged in, but let's assume we track by session later
            # For now, we'll insert without user_id or use a generic ID
            c.execute("INSERT INTO hits (email, username) VALUES (?, ?)", (email, username))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"DB Error: {e}")

# --- API ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return open("index.html").read()

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
    # Fetch recent hits from DB
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM hits ORDER BY id DESC LIMIT 50")
        rows = c.fetchall()
        conn.close()
        
        logs = []
        for row in rows:
            logs.append({
                "id": row[0],
                "email": row[2],
                "username": row[3],
                "created_at": row[4]
            })
    except:
        logs = []
        
    return JSONResponse({
        "running": state["running"],
        "hits_count": len(logs),
        "logs": logs
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

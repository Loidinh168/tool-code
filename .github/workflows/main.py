import requests
from datetime import datetime

# ==== THAY TOKEN & CHAT_ID Ở ĐÂY ====
TOKEN = "8290533409:AAH8H85S3w1fdvv41QGfMT4_maTQk34VVMo"
CHAT_ID = "CHAT_ID_HERE"

CHECK_IN = "09:00"
CHECK_OUT = "19:00"

def notify(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

now = datetime.now()
time_now = now.strftime("%H:%M")

weekday = now.weekday()  # 0 = Mon ... 4 = Fri

# ===== CHỈ GỬI TỪ THỨ 2 → THỨ 6 =====
if weekday < 5:
    if time_now == CHECK_IN:
        notify("✅ CHECK-IN: Đến giờ check-in (09:00)")
    elif time_now == CHECK_OUT:
        notify("🏁 CHECK-OUT: Đến giờ check-out (19:00)")

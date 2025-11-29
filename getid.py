import requests

TOKEN = "8290533409:AAH8H85S3w1fdvv41QGfMT4_maTQk34VVMo"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())

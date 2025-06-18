# wifi_qr.py
# pip install wifi_qrcode_generator pillow

from wifi_qrcode_generator import wifi_qrcode as wifi
from PIL import Image as img

ssid = "Free Wi-Fi"
security = "WPA"
password = "securepassword"

qr = wifi(ssid, False, security, password)

qr.make_image().save("wifi_qr.png")

image_display = img.open("wifi_qr.png")
image_display.show()
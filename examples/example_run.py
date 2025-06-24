import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wifiqrcode_gen.generator import generate_wifi_qr_image,generate_wifi_qr,build_full_image

## Parameters
ssid="WifiTest"
password="PassTest"
security="WPA"
hidden=False

# FULL A4 IMAGE
output_path="qrcodes\output_qr.png"
generate_wifi_qr_image(ssid,password,security,hidden,output_path)

# ONLY QRCODE
output_path="qrcodes\only_qr.png"
qr_only=generate_wifi_qr(ssid, password)
qr_only.save(output_path)

# ONLY IMAGE
output_path="qrcodes\only_img.png"
qr_only=generate_wifi_qr(ssid, password)
bloco_img = build_full_image(qr_only, ssid, password)
bloco_img.save(output_path)
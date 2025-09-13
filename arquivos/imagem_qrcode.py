import qrcode

# pip install qrcode Pillow
data="Opa eu sou a aneli"

img = qrcode.make(data)

img.save("qrcode_aneli.png")
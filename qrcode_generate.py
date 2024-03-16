import qrcode

img = qrcode.make("https://aniwatchtv.to/home")

img.save("qrcode.png")
import qrcode
data = "Hello This is Arindam"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("qr code created successfully")
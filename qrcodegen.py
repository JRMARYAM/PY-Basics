import qrcode

def generate_qr(data, filename="QR_CODE.png"):
    qr = qrcode.QRCode(border=2)  
    qr.add_data(data)
    qr.make(fit=True)  
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

data = "https://join.skype.com/invite/wZbOp8aQeIWd"
generate_qr(data)

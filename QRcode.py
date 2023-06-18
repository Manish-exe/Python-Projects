import qrcode 
from PIL import Image

# img = qr.make("hello i'm manish")
# img.save("qr.png")  ----basic code to generate qr code

qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=15,border=5)
qr.add_data("hello mummy")
qr.make(fit=True)
img = qr.make_image(fill_colour="red",back_colour="blue")
img.save("qr2.png")

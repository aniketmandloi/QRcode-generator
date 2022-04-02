from ensurepip import version
import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data ="https://www.linkedin.com/in/aniket-mandloi-91b4261a2/"
# I have given my linkedin profile link, you can give any link you want

qr.add_data(data)
qr.make(fit=True)
img = qr.make_img(fill="black", back_color ="white")
img.save("qr.png")
from pyzbar.pyzbar import decode
from PIL import Image
from pdf2image import convert_from_path

# Open the image file
path = "Scratch Paper/USED/John Doe.pdf"
image_list = convert_from_path(path)
document = image_list[0]
document.show()

# Decode the QR code or barcode
data = decode(document)[0].data.decode().split("\n")

print(data)
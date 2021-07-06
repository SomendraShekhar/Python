# Import necessary modules
from pyzbar.pyzbar import decode
from PIL import Image

print("Welcome to QR Code Reader")

#Opening the image
img = Image.open("QRCODE.png")

#Decoding the image
d = decode(img)

#Printing the result
print("Your Secret MESSAGE: ")
print(d[0].data.decode())
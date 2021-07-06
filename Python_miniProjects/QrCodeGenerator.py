#import module
import pyqrcode

print("Welcome to QR Code Generator")

msg = input("Type your secret message: ")

code = pyqrcode.create(msg)

code.png("QRCODE.png", scale=5)

print("QR Code Generated Sucessfully !")
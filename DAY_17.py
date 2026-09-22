# Day_17
import qrcode

data = input("Enter a text or a link :")
img = qrcode.make(data)
img.save("img.png")
img.show()

print("Qr code generated sucessfully")
import qrcode
# For website to qrcode
img = qrcode.make("https://pypi.org/project/qrcode/")
img.save("QRcodedocumentation.jpg")

# For text to qrcode
txt = qrcode.make("This is a text")
txt.save("text.jpg")

#Decode the qrcode by making use of openCV library
import cv2
d = cv2.QRCodeDetector()
val,_,_ = d.detectAndDecode(cv2.imread("text.jpg"))
print("Decoded text is: " + val)
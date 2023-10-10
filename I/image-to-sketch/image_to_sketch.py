import cv2
#Reading image
image = cv2.imread("dog.jpg")
#Converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Image inversion
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21,21), 0)
inverted_blur = 255 - blurred
pencil_sketch = cv2.divide(gray_image,inverted_blur,scale = 256.0)

cv2.imwrite('sketchDog.jpg',pencil_sketch)
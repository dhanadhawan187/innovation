from PIL import Image
import pytesseract
images=Image.open("cam1-fr5.jpg")
str=pytesseract.image_to_string(images)
print("output text:\t"+str)

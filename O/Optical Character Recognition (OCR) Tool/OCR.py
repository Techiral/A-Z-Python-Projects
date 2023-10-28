from PIL import Image
import pytesseract

# Replace this with the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_tool(image_path):
    try:
        # Open an image using PIL (Python Imaging Library)
        image = Image.open(image_path)
        
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        
        # Print the extracted text
        print(text)
    
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    # Replace 'your_image.png' with the path to your image file
    image_path = 'your_image.png'
    ocr_tool(image_path)

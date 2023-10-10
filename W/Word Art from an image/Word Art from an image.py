# Importing required modules 
from PIL import Image 
import pywhatkit 

# Store path of image in input_path 
input_path = 'D:\Programming\Github Projects\Word Art from an image\google.png'

# Processing image 
input = Image.open(input_path) 

# Convert image to text form 
pywhatkit.image_to_ascii_art(input_path,'textfile') 

# read word art text file 
read_file = open("textfile.txt","r") 

# Print word art generated file 
print(read_file.read()) 

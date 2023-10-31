from PIL import Image, ImageFilter, ImageEnhance

# Open an image
image_path = "image.jpg"
image = Image.open(image_path)

# Define a menu to choose the operation
print("Image Processing Options:")
print("1. Gaussian Blur")
print("2. Brightness Adjustment")
print("3. Contrast Adjustment")
print("4. Rotate")
choice = input("Enter the option (1/2/3/4): ")

if choice == "1":
    # Apply Gaussian Blur filter
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))
    output_image_path = "blurred_image.jpg"
    blurred_image.save(output_image_path)
    print("Gaussian Blur applied. Modified image saved as 'blurred_image.jpg'.")

elif choice == "2":
    # Adjust brightness
    brightness_factor = float(input("Enter brightness factor (0.0 to 2.0): "))
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(brightness_factor)
    output_image_path = "brightness_adjusted_image.jpg"
    adjusted_image.save(output_image_path)
    print("Brightness adjusted. Modified image saved as 'brightness_adjusted_image.jpg'.")

elif choice == "3":
    # Adjust contrast
    contrast_factor = float(input("Enter contrast factor (0.0 to 2.0): "))
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(contrast_factor)
    output_image_path = "contrast_adjusted_image.jpg"
    adjusted_image.save(output_image_path)
    print("Contrast adjusted. Modified image saved as 'contrast_adjusted_image.jpg'.")

elif choice == "4":
    # Rotate the image
    angle = float(input("Enter rotation angle (in degrees): "))
    rotated_image = image.rotate(angle)
    output_image_path = "rotated_image.jpg"
    rotated_image.save(output_image_path)
    print(f"Image rotated by {angle} degrees. Modified image saved as 'rotated_image.jpg'.")

else:
    print("Invalid choice. Please select a valid option (1/2/3/4).")

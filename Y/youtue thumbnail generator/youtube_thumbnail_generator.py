pip install pillow
from PIL import Image, ImageDraw, ImageFont

def generate_youtube_thumbnail(title, size=(1280, 720), text_color=(255, 255, 255), background_color=(0, 0, 0), font_size=48):
    # Create a blank image with the specified size and background color
    thumbnail = Image.new("RGB", size, background_color)

    # Load a font (you need to specify the font file path)
    font = ImageFont.truetype("path_to_your_font_file.ttf", font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(thumbnail)

    # Calculate text position for centering
    text_width, text_height = draw.textsize(title, font)
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2

    # Add text to the image
    draw.text((x, y), title, fill=text_color, font=font)

    # Save the generated thumbnail
    thumbnail.save("youtube_thumbnail.png")
    print("YouTube thumbnail created: youtube_thumbnail.png")

if __name__ == "__main__":
    video_title = input("Enter your YouTube video title: ")
    generate_youtube_thumbnail(video_title)

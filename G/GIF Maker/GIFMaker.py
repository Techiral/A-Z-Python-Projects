
import os
import imageio

# Directory containing the image frames
frame_dir = 'frames'  # Replace with the directory path containing your image frames

# Output GIF file name
output_gif = 'output.gif'

# List image files in the frame directory
frame_files = sorted([os.path.join(frame_dir, filename) for filename in os.listdir(frame_dir) if filename.endswith('.png')])

# Create the GIF from the image frames
with imageio.get_writer(output_gif, mode='I', duration=0.5) as writer:
    for frame_file in frame_files:
        image = imageio.imread(frame_file)
        writer.append_data(image)

print(f'GIF created: {output_gif}')

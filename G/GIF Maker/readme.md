# GIF Maker - Python

GIF Maker is a Python script that allows you to create a GIF animation from a sequence of image frames. It uses the Pillow (PIL) library for image manipulation and the imageio library for GIF creation.

## Usage

1. **Prepare Image Frames**:

   Place the image frames (in PNG format) that you want to include in the GIF in a directory. By default, the script expects these frames to be in a directory named 'frames', but you can adjust this in the code by modifying the `frame_dir` variable.

2. **Configuration**:

   In the Python script (`create_gif.py`), configure the following variables:
   
   - `frame_dir`: Set this to the path of the directory containing your image frames.
   - `output_gif`: Set this to the desired name of the output GIF file.

3. **Run the Script**:

   Execute the Python script using the following command:

   ```bash
   python create_gif.py

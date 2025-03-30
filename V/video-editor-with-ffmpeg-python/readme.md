# Video Editor with FFmpeg

This is a Python project that utilizes the FFmpeg library to perform various video operations, including format conversion, audio extraction, frame extraction, video trimming, and adjusting video speed.

## Prerequisites

Before running this project, ensure that you have FFmpeg installed on your system. You can download FFmpeg from the official website: [FFmpeg](https://ffmpeg.org/download.html).

## Usage

1. Place the video file you want to edit in the same directory as `video_editor.py`.

2. Run the script `video_editor.py` and follow the prompts to select the desired video editing options.

### Video Editing Options

- **Change Video Format**: Convert the video to a different format (e.g., mov, mp4, m4a, 3gp, 3g2, mj2).

- **Convert Video to MP3**: Extract the audio from the video and save it as an MP3 file.

- **Extract Frames**: Extract frames from the video and save them as individual images.

- **Trim Video**: Trim the video by specifying a start and end time (in the format hh:mm:ss).

- **Adjust Video Speed**: Change the speed of the video, which can be useful for creating slow-motion or fast-motion videos.

## Examples

Here are some examples of how to use the video editing options:

```bash
# Change the format of the video to mp4
Do you want to change the format of the video (y/n): y
Input the valid output format (mov, mp4, m4a, 3gp, 3g2, mj2): mp4

# Convert the video to MP3 audio
Do you want to convert the video to MP3 (y/n): y

# Extract frames from the video
Do you want to extract frames from the video (y/n): y

# Trim the video
Do you want to trim the video (y/n): y
Enter the starting time (hh:mm:ss): 00:01:00
Enter the ending time (hh:mm:ss): 00:02:00

# Adjust the speed of the video
Do you want to change the speed of the video (y/n): y
Input the speed (0.5, 1, 1.5, etc): 1.5

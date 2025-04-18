import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

# Function to extract thumbnails
def extract_thumbnail(video_url, output_directory):
    try:
        # Validate video URL
        if not video_url.startswith("https://www.youtube.com/watch?v="):
            raise ValueError("Invalid YouTube video URL")

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get video's thumbnail URL
        thumbnail_url = yt.thumbnail_url

        # Download thumbnail image
        thumbnail_path = os.path.join(output_directory, "thumbnail.jpg")
        yt.streams.filter(file_extension='jpg').first().download(output_path=output_directory, filename="thumbnail")

        return thumbnail_path
    except VideoUnavailable as e:
        return f"Video is unavailable: {str(e)}"
    except ValueError as e:
        return f"Invalid video URL: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=your_video_id"  # Replace with the YouTube video URL
    output_directory = "thumbnails"  # Replace with your desired output directory

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    thumbnail_url = extract_thumbnail(video_url, output_directory)
    if "Error" in thumbnail_url:
        print(thumbnail_url)
    else:
        print(f"Thumbnail URL: {thumbnail_url}")
        print(f"Thumbnail image downloaded to {output_directory}/thumbnail.jpg")

import instaloader # pip install instaloader

def download_instagram_pictures(username, download_folder):
    L = instaloader.Instaloader() # Create an instance of Instaloader class

    try:
        profile = instaloader.Profile.from_username(L.context, username) # Get profile from username
        for post in profile.get_posts():
            L.download_post(post, download_folder) # Download all posts from profile
        print(f"Downloaded {len(profile.get_posts())} pictures from {username}")
    except Exception as e:
        print(f"An error occurred: {e}") # Print error message

if __name__ == "__main__":
    username = "instagram_username"
    download_folder = "downloaded_pictures"

download_instagram_pictures(username, download_folder) 

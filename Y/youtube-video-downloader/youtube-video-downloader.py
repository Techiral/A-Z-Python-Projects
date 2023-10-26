import pytube

url=int(input("Enter the url of the video: ")) #Enter the url of the video

path=input("Enter the path where you want to save the video: ") #Enter the path where you want to save the video
try:


    yt=pytube.YouTube(url) #object creation using YouTube which was imported in the beginning
except:
    print("Connection Error") #to handle exception
    mp4files = yt.filter('mp4') #to filter all the files with mp4 extension
    yt.set_filename('Downloaded_Video') #setting the filename
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) #getting the video with the extension and resolution passed in the get() function
try:
    d_video.download(path) #downloading the video
except:
    print("Some Error!")
print("Task Completed!") #printing the message after successful completion of the code
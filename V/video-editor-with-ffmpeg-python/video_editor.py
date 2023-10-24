import ffmpeg
import os

def change_video_format(input_file, output_file, format):
    print(format)
    input_stream = ffmpeg.input(input_file)
    output_stream = ffmpeg.output(input_stream, output_file, vcodec="libx264")
    ffmpeg.run(output_stream)

def convert_video_to_audio(input_file, output_file):
    input_stream = ffmpeg.input(input_file)
    output_stream = ffmpeg.output(input_stream, output_file, acodec='mp3')
    ffmpeg.run(output_stream)

def convert_video_to_frames(input_file, output_folder):
    input_stream = ffmpeg.input(input_file)
    ffmpeg.output(input_stream, f'{output_folder}/frame%04d.png').run()

def cut_video(input_file, output_file, start_time, end_time): 
    input_stream = ffmpeg.input(input_file, ss=start_time, to=end_time)
    output_stream = ffmpeg.output(input_stream, output_file, acodec='copy', vcodec='copy')
    ffmpeg.run(output_stream)

def adjust_video_speed(input_file, output_file, speed):
    input_stream = ffmpeg.input(input_file)
    output_stream = ffmpeg.output(input_stream, output_file, filter_complex=f'[0]setpts={1/speed}*PTS', map='0')
    ffmpeg.run(output_stream)

if __name__=="__main__":
    input_=input("Place The video in the same directory as video_editor.py\nand Input the video name (e.g. input_video.mp4): ")

    change_format_opt=input("Do you want to change the format of the video(y/n): ")
    if change_format_opt=='y' or change_format_opt=='Y':
        format=input("Input the valid output format (mov,mp4,m4a,3gp,3g2,mj2): ")
        print(f"output_vids/{input_[0:-4]}.{format}")
        change_video_format(input_, f"output_vids/{input_[0:-4]}.{format}", format)

    cvt_to_audio_opt=input("Do you want to convert the video to mp3(y/n): ")
    if cvt_to_audio_opt=='y' or cvt_to_audio_opt=='Y':
       convert_video_to_audio(input_, f"output_vids/{input_[0:-4]}.mp3")

    cvt_vid_to_frames=input("Do you want to extract frames from the video(y/n): ")
    if cvt_vid_to_frames=='y' or cvt_vid_to_frames=='Y':
        path = f"./{input_}_frames"
        os.mkdir(path)
        print(path)
        convert_video_to_frames(input_, path)
        
    cut_opt=input("Do you want to trim the video(y/n): ")
    if cut_opt=='y' or cut_opt=='Y':
        st=input("Enter the starting time(hh:mm:ss): ")
        et=input("Enter the ending time(hh:mm:ss): ")
        cut_video(input_, f"output_vids/trimmed_{input_}", st, et)

    adjust_speed_opt=input("Do you want to change the speed of video(y/n): ")
    if adjust_speed_opt=='y' or adjust_speed_opt=='Y':
        speed=float(input("Input the speed(0.5,1,1.5 etc): "))
        adjust_video_speed(input_, f'output_vids/sped_up_{input_}', speed)

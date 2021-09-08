# !pip install moviepy --user
# !pip install ffmpeg
import moviepy.editor as mp
import os
s_path = input() #Enter the Source path
files = os.listdir(path)
size = len(files)
print("Total samples: ",size)
print("Sample file:   ",files[0])
d_path = input() #Enter the Destination path
for i in range(len(files)):
    s_temp = path+files[i]
    video = mp.VideoFileClip(s_temp)
    d_temp = d_path+files[i][:-3]+"mp3"
    video.audio.write_audiofile(d_temp)
print("All your files are successfully converted")
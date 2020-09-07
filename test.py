'''
itags, progressive
18 = 360p
135 = 480p
22=720p 
'''
'''from moviepy.editor import *
video = VideoFileClip("1w.mp4")
video.audio.write_audiofile("1w.mp3")'''

#https://www.youtube.com/watch?v=a3HZ8S2H-GQ
#4k
#https://www.youtube.com/watch?v=OfIQW6s1-ew
from pytube import YouTube
link = 'https://www.youtube.com/watch?v=OfIQW6s1-ew'
yt = YouTube(link)


for i in yt.streams.filter():
    print(i)
    print("\n")

#yt.streams.get_by_itag(160).download()
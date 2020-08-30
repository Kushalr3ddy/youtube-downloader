'''
itags
18 = 360p
135 = 480p

'''
'''from moviepy.editor import *
video = VideoFileClip("1w.mp4")
video.audio.write_audiofile("1w.mp3")'''

#https://www.youtube.com/watch?v=a3HZ8S2H-GQ
'''
import pytube

link ="https://www.youtube.com/watch?v=a3HZ8S2H-GQ"

yt = pytube.YouTube(link)

#for i in yt.streams.get_by_itag():
#    print(i)
#yt.streams.get_by_itag('18').download()
import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("w.mp4"))
video.audio.write_audiofile(os.path.join("videos","movie_sound.mp3"))
'''
import tkinter as tk

#ffmpeg -i video.mp4 -vn audio.mp3
'''
itags, progressive
18 = 360p
135 = 480p
22=720p 
'''
'''from moviepy.editor import *
video = VideoFileClip("1w.mp4")
video.audio.write_audiofile("1w.mp3")

#https://www.youtube.com/watch?v=a3HZ8S2H-GQ

#4k
#https://www.youtube.com/watch?v=OfIQW6s1-ew
from pytube import YouTube
import requests
from PIL import Image
from io import BytesIO
link = 'https://www.youtube.com/watch?v=OfIQW6s1-ew'
yt = YouTube(link)
key = link[32:]
img = requests.get(f"https://img.youtube.com/vi/{key}/0.jpg")
im = Image.open(img.raw)
im.show()



for i in yt.streams.filter():
    print(i)
    print("\n")

#yt.streams.get_by_itag(160).download()
# '''
import threading
import time
def f():
    print("hello world")
    time.sleep(1)

def g():
    x = threading.Thread(target=f)
    print("first")
    time.sleep(1)
    x.start()
    print("second")

g()
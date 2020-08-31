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

for i in yt.streams.filter(file_extension='mp4'):
   print(i)
   print("\n")

#yt.streams.get_by_itag('18').download()
import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("w.mp4"))
video.audio.write_audiofile(os.path.join("videos","movie_sound.mp3"))
'''


#ffmpeg -i video.mp4 -vn audio.mp3

from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

var1 = IntVar()

e = Radiobutton(root,text="x",variable=var1)
y =Radiobutton(root,text="y",variable=var1)
e.pack()
y.pack()

label = Label(root)
label.pack()
root.mainloop()
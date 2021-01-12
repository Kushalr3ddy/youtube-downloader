import tkinter
from pytube import YouTube
import webbrowser
import requests
from PIL import Image
from tkinter import PhotoImage
import time
import threading

app = tkinter.Tk()
app.title('yt downlodr')
app.geometry('450x400')
app.resizable(False,False)

try:
    app.iconbitmap("coderarena.ico")
except:
    pass

def download():
    link = e.get()
    status.place(x= 100,y=80)
    key = link[32:]
    #picture =requests.get(f"https://img.youtube.com/vi/{key}/0.jpg")
    #img = PhotoImage(file=(picture.raw))
    #time.sleep(2)
    #pic.create_image(20,20, anchor=NW, image=img)
    t1 = threading.Thread(YouTube(link).streams.first().download())
    t1.start()
    status.destroy()


#widgets
label = tkinter.Label(app,text="youtube video downloader")
info = tkinter.Label(app,text = "follow me on instagram:@coder_arena")
e = tkinter.Entry(app,width=50)
btn1 = tkinter.Button(app,text='download',command =download)
btn2 = tkinter.Button(app,text='paste')
version = tkinter.Label(app,text='v0.1')
status = tkinter.Label(app,text = "downloading")
mp3 = tkinter.Checkbutton(app,text='mp3')
mp4 = tkinter.Checkbutton(app,text='mp4')
pic = tkinter.Canvas(app,height=100)


#widget positions
label.place(x=20,y=10)
e.place(x= 30,y=40)
btn1.place(x=340,y=35)
info.place(x=220,y=370)
version.place(x=10,y=370)
mp3.place(x=50,y=320)
mp4.place(x=50,y=350)
pic.place(x=30,y=60)

app.mainloop()
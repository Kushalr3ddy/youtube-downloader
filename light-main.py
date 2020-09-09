import tkinter
from pytube import *
import webbrowser

app = tkinter.Tk()
app.title('yt downlodr')
app.geometry('450x140')
app.resizable(False,False)

try:
    app.iconbitmap("coderarena.ico")
except:
    pass

def download():
    link = e.get()
    YouTube(link).streams.first().download()
    status.place(x= 100,y=80)
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


#widget positions
label.place(x=20,y=10)
e.place(x= 30,y=40)
btn1.place(x=340,y=35)
info.place(x=220,y=120)
version.place(x=10,y=120)
mp3.place(x=50,y=60)
mp4.place(x=50,y=90)


app.mainloop()
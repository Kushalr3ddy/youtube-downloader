import tkinter as tk
from tkinter import messagebox
import os
from pytube import YouTube
import webbrowser
import time
from moviepy.video.io.VideoFileClip import *
import pyperclip as pclip
#from moviepy.audio.fx import audio_fadein

app = tk.Tk()
app.title('yt downlodr')
app.geometry('550x140')
app.resizable(False,False)
Bcol='#4b4f4c'
app.configure(bg=Bcol)

try:
    app.iconbitmap("yt.ico")
except:
    pass
#messagebox.showinfo("warning", "the window will stop responding while downloading \nDO NOT CLOSE when this happens")

# functions
def me():
    webbrowser.open('https://www.instagram.com/coder_arena/',new=2)
    '''If new is 0, the url is opened in the same browser window if possible. 
    If new is 1, a new browser window is opened if possible. 
    If new is 2, a new browser page (“tab”) is opened if possible'''

'''
def dismp3():
    mp3.config(state='disabled')
    mp4.config(state='active')

def dismp4():
    mp4.config(state='disabled')
    mp3.config(state='active')

'''

def paste():#pastes the clipboard content into entry
    e.delete(0,tk.END)
    e.insert(0,pclip.paste())

###checkbutton functions######
def check144():
    
    var240.set(0)
    var360.set(0)
    var480.set(0)
    var720.set(0)

def check240():
    
    var144.set(0)
    var360.set(0)
    var480.set(0)
    var720.set(0)

def check360():
    
    var144.set(0)
    var240.set(0)
    var480.set(0)
    var720.set(0)

def check480():

    var144.set(0)
    var240.set(0)
    var360.set(0)
    var720.set(0)

def check720():

    var144.set(0)
    var240.set(0)
    var360.set(0)
    var480.set(0)

#############################

###################################################
def download(): 
    global link
    link = e.get()
    if len(link)==0:
        tk.messagebox.showerror("Error","please insert link")
        pass
    #status.place(x= 100,y=80)
    yt = YouTube(link)
    if var1.get()==1 and var2.get()==0:
        yt.streams.get_by_itag('18').download('saved',yt.title)#foldername,filename,first
    elif var1.get() ==0 and var2.get() ==1:
        yt.streams.get_by_itag('18').download('saved',yt.title)#foldername,filename,first
        video = VideoFileClip(f"saved\\{yt.title}.mp4")
        video.audio.write_audiofile(f"saved\\{yt.title}.mp3")
        #os.remove(f"{yt.title}.mp4")
    elif var1.get() ==1 and var2.get() ==1:
        tk.messagebox.showerror("Error","select only one of the checkboxes")
    else:
        tk.messagebox.showerror('Error',"select one of the checkbox")
###########################################################


#variables required
var1 = tk.IntVar()
var2 = tk.IntVar()
resvar =tk.StringVar()
#resvar.set(0)
var144 = tk.IntVar()
var240 = tk.IntVar()
var360 = tk.IntVar()
var480 = tk.IntVar()
var720 = tk.IntVar()

#widgets
label = tk.Label(app,text="video downloader for youtube",bg=Bcol)
info = tk.Button(app,width = 5,text = "info",command = me)
e = tk.Entry(app,width=50)
rename = tk.Entry(app)
btn1 = tk.Button(app,text='download',command =download)
btn2 = tk.Button(app,text='paste')
version = tk.Label(app,text='v0.2',bg=Bcol)
status = tk.Label(app,text = "downloading")
mp3 = tk.Checkbutton(app,text='mp3 and mp4',variable = var2,bg=Bcol,command=lambda:var1.set(0))
mp4 = tk.Checkbutton(app,text='only mp4',variable = var1,bg=Bcol,command=lambda:var2.set(0))
#working = tk.Label(app,text = "downloading")
pbtn = tk.Button(app,text ='paste',width=8,command = paste)
elabel = tk.Label(app,text ="select format",bg=Bcol)
rlabel = tk.Label(app,text ="resolution",bg=Bcol)
res144 =tk.Checkbutton(app,text="144p",variable = var144,bg=Bcol,onvalue=1,offvalue=0,command=lambda:check144())
res240 =tk.Checkbutton(app,text="240p",variable = var240,bg=Bcol,onvalue =1,offvalue=0,command=lambda:check240())
res360 = tk.Checkbutton(app,text="360p",variable = var360,bg=Bcol,onvalue=1,offvalue=0,command=lambda:check360())
res480 =tk.Checkbutton(app,text="480p",variable = var480,bg=Bcol,onvalue=1,offvalue=0,command=lambda:check480())
res720 =tk.Checkbutton(app,text="720p",variable = var720,bg=Bcol,onvalue=1,offvalue=0,command=check720)
resmenu = tk.Menubutton(app)
#widget positions 
label.place(x=20,y=10)
e.place(x= 30,y=40,width=400)
btn1.place(x=433,y=35)
info.place(x=500,y=113)
version.place(x=10,y=120)
mp3.place(x=50,y=75)
mp4.place(x=50,y=100)
pbtn.place(x=365,y=61)
elabel.place(x=40,y=60)
rlabel.place(x=170,y=60)
res144.place(x=170,y=75)
res240.place(x=170,y=100)
res360.place(x=230,y=75)
res480.place(x=230,y=100)
res720.place(x=290,y=75)
#resmenu.place(x=,y=)
#working.place(x= 100,y = 120)



if __name__ =='__main__':
    app.mainloop()
'''
itags, progressive
18 = 360p
135 = 480p

'''
'''from moviepy.editor import *
video = VideoFileClip("1w.mp4")
video.audio.write_audiofile("1w.mp3")'''

#https://www.youtube.com/watch?v=a3HZ8S2H-GQ

from tkinter import *


top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()
top.mainloop()


from pygame import mixer
import time
from tkinter import *

master = Tk()
hour = IntVar
minute = IntVar
hour1 = Scale(master, from_=0, to=24, variable = hour, activebackground = ('red'),bg=('yellow'),font=('italics'),label=('HOUR'),length=300,sliderlength=50,tickinterval=2,width=30)
hour1.pack() 
minu = Scale(master, from_=0, to=60, orient=HORIZONTAL, variable = minute, activebackground = ('red'),bg=('yellow'),font=('italics'),label=('MINUTE'),length=500,sliderlength=50,tickinterval=10,width=30) 
minu.pack() 


def sel():
    conf=Label(master,text='close this window to confirm')
    conf.pack()
    global hour
    global minute
    hour=hour1.get()
    minute=minu.get()
    return(hour)
    return(minute)

button = Button(master, text="Confirm Alarm", command=sel,activebackground=('green'))
button.pack(anchor=CENTER)
mainloop()
hour2=hour
minute2=minute


  

import datetime 

def alarm():
    while 1==1:
        if (hour2==datetime.datetime.now().hour and minute2==datetime.datetime.now().minute):
            print("wake up you lazy")
            mixer.init()
            mixer.music.load('C:/Users/Dell/Desktop/Billie_Eilish_-_bad_guy_(version_2).mp3')
            mixer.music.play()
            sn=input("press s to stop the alarm")
            if sn=="s":
               
                mixer.music.pause()
               
            else:
                print("wake up !!!!!!")
            break
    
alarm()

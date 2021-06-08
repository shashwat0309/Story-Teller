from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root =Tk(className='Story Teller')
root.resizable(False, False) 
root.geometry("600x600")
root.configure(bg='ghost white')
root.title("Story Teller")
Label(root, text="Story Teller", font="arial 20 bold").pack()
Label(root, text="Select A Story From Our Collection", font="arial 14").place(x=140,y=60)
story = StringVar()
def story1():
    f = open("story/story1.txt", "r")
    Message =  f.read()
    speech = gTTS(text = Message)
    speech.save('story.mp3')
    playsound('story.mp3')

Button(root, text="Story 1", bg="red" ,width="10",font="arial 14", command=story1).place(x=10,y=100)
Label(root, text="Listen Your Custom Story", font="arial 14").place(x=180,y=200)
msg = StringVar()
entryfield = Entry(root, textvariable=msg, width='50').place(x=130,y=230)
def Text_to_speech():
    Message = msg.get()
    speech = gTTS(text = Message)
    speech.save('storycustom.mp3')
    playsound('storycustom.mp3')
    os.remove("storycustom.mp3")
def Exit():
    root.destroy()

def Reset():
    msg.set("")
    os.remove("storycustom.mp3")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=130,y=260)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=230 , y = 260)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=330 , y = 260)
root.mainloop()

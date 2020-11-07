from tkinter import*
from tkinter  import ttk
import datetime
import pyowm
import pyttsx3
from threading import *
from time import  strftime

font=("arial",40)

root=Tk()
root.title("Smart clock")
root.geometry("855x335")
root.maxsize(855,355)
root.minsize(855,355)

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

root.configure(background="black")



def day():
    string=strftime("%A")
    text1.config(text=string)
    print (string)

def am():
    string = strftime("%p")
    text7.config(text=string)
    print(string)


def time():
    string1 = strftime("%I:%M:%S")
    text2.config(text=string1)
    text2.after(1000,time)

def date():
    string=datetime.date(2020,11,5)
    string1 = strftime("%b      %d         %Y")
    dt=f"DATE :  {string1}"
    print(string1)
    text3.config(text=dt)


def total_day():

    string=datetime.date(2020,11,5)
    string2= strftime("%j")
    ts=f"Day number of year: {string2} Days"
    print(string2)
    text4.config(text=ts)

def total_week():
    string=datetime.date(2020,11,5)
    string3= strftime("%U")#Sunday as the first day of week, 00-53
    ts=f"Week number of year: {string3} Week"
    print(string3)
    text5.config(text=ts)


def wth():
    owm = pyowm.OWM('e4dd31629d0ef54e3dd86d6265fc12bf')
    observation = owm.weather_at_place("Rangpur")
    w = observation.get_weather()
    # Weather details
    l = w.get_temperature('celsius')
    v = l['temp_max']
    ws = f" {v}°C"
    print(ws)
    text6.config(text=ws)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:

        speak('good morning sir welcome to our smart clock')

    if hour > 12 and hour < 18:

        speak('good afternoon sir welcome to our smart clock')

    elif hour > 18 and hour <= 24:

        speak('good evening sir welcome to our smart clock')



text1= Label(root, font=font,background="black", foreground="cyan")
text1.pack(anchor='sw',padx=320,pady=20)

text7=Label(root,font=("Bodoni MT Black",20,'bold'), background="black", foreground="cyan")
text7.pack(anchor='n')

text2 = Label(root, font=font, background="black", foreground="cyan")
text2.pack(side=TOP,padx=270,fill=X)


text6=Label(root,font=("Bodoni MT Black",20,'bold'), background="black", foreground="cyan")
text6.pack(anchor='se')


text3=Label(root,font=("arial",15,'bold','italic'), background="black", foreground="cyan")
text3.pack(anchor='sw')


text5=Label(root,font=("arial",15,'bold','italic'), background="black", foreground="cyan")
text5.pack(anchor='nw')


text4=Label(root,font=("arial",15,'bold','italic'), background="black", foreground="red")
text4.pack(anchor='nw')


if __name__ == "__main__":
    day()
    time()
    am()
    date()
    total_week()
    total_day()
    wth()
    wishme()



root.mainloop()

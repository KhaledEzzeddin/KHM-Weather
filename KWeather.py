from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
#-----------------------------------------------------
url="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key="2b980defab2037105b2465caee9b70c1"

win=Tk()

win.title("KWeather")

win.geometry("450x325+100+50")
win.resizable(width=False,height=False)

icon=PhotoImage(file="Weather.png")
win.call("wm","iconphoto",win._w,icon)
#--------------------------------------------------------
def gwthr(city):
    urwpi=requests.get(url.format(city,api_key))
    if urwpi:
        jsonData=urwpi.json()
        city=jsonData["name"]
        contry=jsonData["sys"]["country"]
        tempk=jsonData["main"]["temp"]
        tempc=tempk-273.15
        tempf=(tempk-273.15)*9/5+32
        wthr=jsonData["weather"][0]["main"]
        pres=jsonData["main"]["pressure"]
        des=jsonData["weather"][0]["description"]
        fire=(city,contry,tempc,tempf,wthr,pres,des)
        return fire
    else:
        return None
def serch():
    city=citytx.get()
    wthrdt=gwthr(city)
    if wthrdt:
        lbloc["text"]=(f"location:{wthrdt[0]},{wthrdt[1]}")
        lbltemp["text"]=("Temperature:{:.2f}°C,{:.2f}°F".format(wthrdt[2],wthrdt[3]))
        lblwth["text"]=(f"weather:{wthrdt[4]}")
        lblprs["text"]= (f"Pressure:{wthrdt[5]}")
    else:
        messagebox.showerror("Error",f"can not find city {city}")



#----------------------------------------------------
can0=Canvas(win,width=450,height=300,bg="#B6B6B4",relief="raise")
can0.pack()

can1=Canvas(win,width=445,height=250,bg="#D1D0CE")
can0.create_window(224,180,window=can1)

can2=Canvas(win,width=445,height=50,bg="#B6B6B4")
can0.create_window(224,300,window=can2)
#--------------------------------------------------------
photo=Image.open("WH.png")
photo=photo.resize((45,45))
img1=ImageTk.PhotoImage(photo)
lblimg=Label(win,width=42,height=42,image=img1,bg="#B6B6B4")
can0.create_window(25,25,window=lblimg)

citytx=StringVar()

cityen=Entry(win,text="Location",fg="black",width=20,bg="#D1D0CE",bd=0,font=("times",14),textvariable=citytx)
can0.create_window(270,25,window=cityen)

mytit=Label(win,text="KWeather",font=("times",14,"bold"),bg="#B6B6B4")
can0.create_window(100,20,window=mytit)

serbtn=Button(win,command=serch,text="Refesh",padx=4,pady=2,relief=FLAT,cursor="hand2",activebackground="#c1bebe",font=("helvetica",10,"bold"),bg="#D1D0CE",fg="black")
can0.create_window(410,25,window=serbtn)
#------------------------------------------------------
lbloc=Label(win,text="",bg="#D1D0CE")
lbloc.config(font=("times",16,"bold"))
can1.create_window(210,30,window=lbloc)

lbltemp=Label(win,text="",bg="#D1D0CE")
lbltemp.config(font=("times",16,"bold"))
can1.create_window(210,80,window=lbltemp)

lblwth=Label(win,text="",bg="#D1D0CE")
lblwth.config(font=("times",16,"bold"))
can1.create_window(210,140,window=lblwth)

lblprs=Label(win,text="",bg="#D1D0CE")
lblprs.config(font=("times",16,"bold"))
can1.create_window(210,200,window=lblprs)
#-----------------------------------------------
mytit=Label(win,text="Development In Python By Khaled Ezzeddin",font=("times",10),bg="#B6B6B4")
can2.create_window(225,25,window=mytit)
#---------------------------------------------
win.mainloop()

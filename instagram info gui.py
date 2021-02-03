from tkinter import *
from bs4 import BeautifulSoup
import requests
root= Tk()
root.geometry("480x130")
f1 = Frame(root,bg="pink",borderwidth=10)
f1.grid()
L1 = Label(f1,text="USERNAME",fg = "Black",bg="pink")
L1.grid(row=1,column=0)
L2 = Label(f1,text="FOLLOWERS",fg = "Black",bg="pink")
L2.grid(row=2,column=0)
L3 = Label(f1,text="FOLLOWING",fg = "Black",bg="pink")
L3.grid(row=3,column=0)
L4 = Label(f1,text="POSTS",fg = "Black",bg="pink")
L4.grid(row=4,column=0)
username=StringVar()
s1=Entry(f1,textvariable=username)
s1.grid(row=1,column=1,ipadx=100)
a=StringVar()
s2=Entry(f1,textvariable=a)
s2.grid(row=2,column=1,ipadx=100)
b=StringVar()
s3=Entry(f1,textvariable=b)
s3.grid(row=3,column=1,ipadx=100)
c=StringVar()
s4=Entry(f1,textvariable=c)
s4.grid(row=4,column=1,ipadx=100)
URL="https://www.instagram.com/{}/"
def parse_data(s):
    data={}
    s=s.split("-")[0]
    s=s.split(" ")
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data
def scrape_data(username):
    r=requests.get(URL.format(username))
    s=BeautifulSoup(r.text, "html.parser")
    meta=s.find("meta", property ="og:description")
    return parse_data(meta.attrs['content'])
def button_func():
    data = scrape_data(s1.get())
    a.set(data["Followers"])
    b.set(data["Following"])
    c.set(data["Posts"])
    s2.update()
    s3.update()
    s4.update()
b1=Button(text="GET DATA",command=button_func)
b1.grid(row=4,column=0)
root.mainloop()

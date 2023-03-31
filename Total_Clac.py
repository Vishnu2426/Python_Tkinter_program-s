#a=int(input("Enter Maths"))
#b=int(input("Enter Enlish"))
#c=int(input("Enter Tamil"))
#d=int(input("Enter Social"))
#e=int(input("Enter Science"))
#Total=a+b+c+d+e
#Average=Total/100*5
#print("Total",Total)
#print("Average",Average)


from tkinter import*
from tkinter import messagebox
import tkinter as tk

m=Tk()
m.geometry("500x300")

def add():
    if En1.get()=="" or En2.get()=="" or En3.get()=="" or En4.get()=="" or En5.get()=="":
        messagebox.showerror("Error","Enter Values")
        
    n1=int(En1.get())
    n2=int(En2.get())
    n3=int(En3.get())
    n4=int(En4.get())
    n5=int(En5.get())
    result=n1+n2+n3+n4+n5
    result_label.config(text=result)

    if En1.get()=="" or En2.get()=="" or En3.get()=="" or En4.get()=="" or En5.get()=="":
        messagebox.showerror("Error","Enter All Values")

def Avg():
    m1=int(En1.get())
    m2=int(En2.get())
    m3=int(En3.get())
    m4=int(En4.get())
    m5=int(En5.get())
    result2=m1+m2+m3+m4+m5
    result3=result2/500*100
    avg_label.config(text=result3)

maths=Label(m,text="Maths")
maths.place(x=50,y=100)
En1=Entry(m)
En1.place(x=110,y=100)
Tamil=Label(m,text="Tamil")
Tamil.place(x=50,y=130)
En2=Entry(m)
En2.place(x=110,y=130)
Socail=Label(m,text="Social")
Socail.place(x=50,y=160)
En3=Entry(m)
En3.place(x=110,y=160)
Science=Label(m,text="Science")
Science.place(x=50,y=190)
En4=Entry(m)
En4.place(x=110,y=190)
Socail=Label(m,text="Social")
Socail.place(x=50,y=220)
En5=Entry(m)
En5.place(x=110,y=220)

btn=Button(m,text="Total",command=add)
btn.place(x=120,y=250)

result_label=Label(m,text="Result:")
result_label.place(x=250,y=200)

btn1=Button(m,text="Percentage",command=Avg)
btn1.place(x=200,y=250)

avg_label=Label(m,text="avg")
avg_label.place(x=250,y=230)


m.mainloop()


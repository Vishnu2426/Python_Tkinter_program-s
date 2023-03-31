from tkinter import*
from gtts import gTTS
import os
from PIL import ImageTk, Image  
root=Tk()
root.geometry("800x500")
root.config(bg="gray")
def play():
    language="en"
    convert=gTTS(text=entry.get(),
                 lang=language,
                 slow=False)
    convert.save("convert.mp3")
    os.system("convert.mp3")
                 
        



label=Label(root,text="Text To Voice !!!!!!",bg="gray",fg="black", font ="vernanda 30")
label.place(x=5,y=180)

entry=Entry()
entry.place(x=2,y=240,height=30,width=790)


btn=Button(text="Convert" ,bg="black",fg="green",font="veranda 12",command=play)
btn.place(x=150,y=290,width=60)

pic=Image.open("C:\\Users\\Vishnu Ram\\OneDrive\\Desktop\\Python\\voice.jpg")
pic=pic.resize((790,150))
img = ImageTk.PhotoImage(pic)

my_label=Label(image=img)
my_label.pack()


root.mainloop()

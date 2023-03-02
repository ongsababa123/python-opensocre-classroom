from msilib.schema import RadioButton
import tkinter as tk
from turtle import color
import tkinter.messagebox as mbox

root = tk.Tk()
root.geometry("300x400")
root.minsize(150,400)
var = tk.IntVar()

fruit = [("Apple",3, "red"), ("Orange",7,"orange"), ("Mango",4, "green")]

def getdata():
    print(var.get())
    for text,value,color in fruit:
        tk.Label(frame1,text="You selected the option " + str(value)).grid(row=0,column=0,sticky=tk.EW)
        if value == var.get():
            print(value,text,color)
            break
        
def show():
    for text,value,color in fruit:
        if value == var.get():
            mbox.showinfo(title="Show Selected",message =
                          "Fruit ID         : "+ str(value) + "\n" +
                          "Fruit Name   : " + str(text) + "\n" +
                          "Color            : " + str(color))
     
def exit():
    root.destroy() 
           
for text,value,color in fruit:
    tk.Radiobutton(root,text=text,value=value,variable=var,bg=color,command=getdata).pack(anchor=tk.W,fill=tk.BOTH,expand=True)
    

frame1 = tk.Frame(root)
frame1.pack(expand=True,fill=tk.BOTH)
frame1.rowconfigure(0,weight = 1)#กำหนดของ row0
frame1.columnconfigure(0,weight = 1)#กำหนดของ col0

f2 = tk.Frame(root,bg="PINK")
f2.pack(expand=True,fill=tk.BOTH)

tk.Label(frame1).grid(row=0,column=0,sticky=tk.EW)

b1 = tk.Button(f2,text="Test",bg="BLUE")
b1.pack(side=tk.LEFT,expand=True,ipadx=0,ipady=0,fill=tk.BOTH)

b2 = tk.Button(f2,text="Show",bg="GREEN",command=show)
b2.pack(side=tk.LEFT,expand=True,padx=5,pady=0,fill=tk.X)

b3 = tk.Button(f2,text="Exit",bg="YELLOW",command=exit)
b3.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)


root.mainloop()
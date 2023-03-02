import tkinter as tk

def getdata():
    print(var.get())
    for text,value in DATA:
        if value == var.get():
            print(value,text)
            break
root = tk.Tk()
var = tk.IntVar()
DATA = [('Java',5),('C++',3),('Python',2)]

for text,value in DATA:
    tk.Radiobutton(root,text=text,value=value,variable=var,command=getdata,indicatoron=0).pack(anchor=tk.W,fill=tk.BOTH,expand=True)

for text,value in DATA:
    tk.Radiobutton(root,text=text,value=value,variable=var,command=getdata).pack(anchor=tk.W)

# var = set(2)
root.mainloop()
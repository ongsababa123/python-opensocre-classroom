import tkinter as tk

win = tk.Tk()
win.title("Test layout")
win.geometry("300x300")
win.minsize(150,300)

f1 = tk.Frame(win,bg="RED")
f1.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
f2 = tk.Frame(win,bg="BLUE")
f2.pack(side=tk.BOTTOM,fill=tk.X)

for i in range(5):
    tk.Button(f1,text="BT["+str(i)+"]",fg="red").pack(side=tk.LEFT,expand=True,fill=tk.Y)

b1 = tk.Button(f2,text="Test",bg="BLUE")
b1.pack(side=tk.LEFT,expand=True,ipadx=0,ipady=0,fill=tk.BOTH)

b2 = tk.Button(f2,text="Test",bg="GREEN")
b2.pack(side=tk.LEFT,expand=True,padx=0,pady=0,fill=tk.BOTH)

b3 = tk.Button(f2,text="Test",bg="YELLOW")
b3.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

win.mainloop()
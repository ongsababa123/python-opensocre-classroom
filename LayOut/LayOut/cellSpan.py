import tkinter as tk
win = tk.Tk()
win.geometry("300x300")
win.minsize(150,300)

frame1 = tk.Frame(win,bg="red")
frame1.pack(expand=True,fill=tk.BOTH)
frame1.rowconfigure(0,weight = 1)#กำหนดของ row0
frame1.rowconfigure(1,weight = 1)#กำหนดของ row1
frame1.columnconfigure(0,weight = 1)#กำหนดของ col0
frame1.columnconfigure(1,weight = 2)#กำหนดของ col1
tk.Label(frame1,bg="green",text="Name: ").grid(row=0,column=0,columnspan=2,sticky=tk.EW)
tk.Label(frame1,bg="green",text="Name: ").grid(row=1,column=0,sticky=tk.EW)
e1 = tk.Entry(frame1,bg="yellow").grid(row=1,column=1,sticky=tk.EW)
tk.Label(frame1,bg="green",text="Tel: ").grid(row=2,column=0,sticky=tk.EW)
e1 = tk.Entry(frame1,bg="yellow").grid(row=2,column=1,sticky=tk.EW)
#bt1 = tk.Button(frame1,bg="green").grid(row=0,column=0,sticky=tk.NSEW)
win.mainloop()
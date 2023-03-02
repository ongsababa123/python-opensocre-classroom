import tkinter as tk
root = tk.Tk()
root.title("Login")
root.geometry("240x100")

frame1 = tk.Frame(root)
frame1.pack(fill=tk.BOTH)
frame1.rowconfigure(0,weight = 1)#กำหนดของ row0
frame1.rowconfigure(1,weight = 1)#กำหนดของ row1
frame1.rowconfigure(2,weight = 4)#กำหนดของ row2
frame1.columnconfigure(0,weight = 1)#กำหนดของ col0
frame1.columnconfigure(1,weight = 2)#กำหนดของ col1
tk.Label(frame1,text="Username: ").grid(row=0,column=0,sticky=tk.EW, padx=5, pady=5)
eUsername = tk.Entry(frame1).grid(row=0,column=1,sticky=tk.EW, padx=5, pady=5)

tk.Label(frame1,text="Password: ").grid(row=1,column=0,sticky=tk.EW, padx=5, pady=5)
ePassword = tk.Entry(frame1).grid(row=1,column=1,sticky=tk.EW, padx=5, pady=5)

bLogin = tk.Button(frame1,text="Login").grid(row=3,column=1,sticky=tk.E, padx=5, pady=5)

root.mainloop()
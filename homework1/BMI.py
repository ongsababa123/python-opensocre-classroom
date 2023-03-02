from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} ผอม')
    elif (bmi > 18.5) and (bmi < 22.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} ปกติ')
    elif (bmi > 23) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} เกินเกณฑ์')
    elif (bmi > 25) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} อ้วน')
    elif (bmi > 30):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} อ้วนมาก') 
    else:
        messagebox.showerror('bmi-pythonguides', 'บางอย่างผิดพลาด!')   

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)



height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
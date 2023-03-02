import tkinter as tk
import tkinter.simpledialog as dialog
import tkinter.messagebox as mbox

class MyDialog(dialog.Dialog): #ในวงเล็บแปลว่าเป็นการสืบทอดคุณสมบัติ
    def __init__(self,parent): 
        super().__init__(parent,"Simple input form")
        
    def apply(self):
        mbox.showinfo("test apply")
        print(mbox.askokcancel(title="Ask ?",message="What to know?"))
        
    def cancel(self):
        mbox.showinfo("test cancel")
        self.destroy()
        
root = tk.Tk()
m = MyDialog(root)
root.mainloop()
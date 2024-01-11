from tkinter import *
from tkinter import messagebox

class UserInputDialog(Toplevel):
    def __init__(self, master=None, input_frame=None):
        super().__init__(master)
        self.title("USER INPUT")
        self.geometry("350x150")
        self.resizable(False, False)
        self.input_frame = input_frame
        
        self.label = Label(self,
                           text="Enter 15 array elements separated by spaces:",
                           font=('Arial', 11),)
        self.label.place(x=20,y=10)

        self.user_input_var = StringVar()

        self.entry = Entry(self,
                           textvariable=self.user_input_var,
                           width=35,
                           font=('Arial', 13))
        self.entry.place(x=15,y=50)

        self.ok_button = Button(self,
                                text="INSERT",
                                fg='white',
                                bg='green',
                                font=('Arial', 10, 'bold'),
                                command=self.on_ok)
        self.ok_button.place(x=135,y=100)

    def on_ok(self):
        user_input = self.user_input_var.get().split()

        try:
            user_input = [int(element) for element in user_input]
            if len(user_input) == 15:
                self.input_frame.set_user_input(user_input)
                self.destroy()
            else:
                messagebox.showwarning("Invalid Input", "Please enter exactly 15 elements.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values.")
    
    def on_close(self):
        self.destroy()
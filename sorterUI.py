# import threading
# import time
from tkinter import *
from tkinter import ttk
from userInput import UserInputDialog
from color import *

class SorterUI(Frame):
    def __init__(self, main_frame=None):
        super().__init__(main_frame)
        self.main_frame = main_frame

        self.window = Toplevel(main_frame)
        self.window.geometry("900x600")
        self.window.resizable(False, False)


        self.back_button = Button(self.window,
                                  text="BACK",
                                  fg='black',
                                  bg='pink',
                                  font=('Arial', 10, 'bold'),
                                  command=self.go_back)
        self.back_button.place(x=10,y=10)
        
        self.label2 = Label(self.window,
                            text="Select sorting speed:",
                            font=('mincho', 15, 'bold'),
                            fg='black')
        self.label2.place(x=270, y=60)

        self.speed_option = ["Slow", "Normal", "Fast"]

        self.speed_combobox = ttk.Combobox(self.window,
                                     values=self.speed_option,
                                     state='readonly',
                                     font=('Arial', 11))
        self.speed_combobox.place(x=450, y=64)
        self.speed_combobox.set(self.speed_option[0])

        self.user_input = Button(self.window, text="INPUT ARRAY",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.on_input)
        self.user_input.place(x=220, y=100)

        self.generate_random = Button(self.window, text="RANDOM ARRAY",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.on_generate_random)
        self.generate_random.place(x=330, y=100)

        self.start_sort = Button(self.window, text="START",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.run_sort)
        self.start_sort.place(x=490, y=100)

        self.window.protocol("WM_DELETE_WINDOW", self.exit_application)

        self.visual = Frame(self.window,
                            width=870,
                            height=430,
                            bg='black',
                            bd=1,
                            relief=FLAT)
        self.visual.place(x=15, y=160)

        self.canvas = Canvas(self.window,
                             width=855,
                             height=415,
                             bg=WHITE)
        self.canvas.place(x=20, y=165)

        self.array_data = []

    def go_back(self):
        self.window.destroy()
        self.main_frame.window.deiconify()

    def exit_application(self):
        self.main_frame.window.destroy()

    def set_sort_speed(self):
        pass

    def array_data_draw(self, array_data, color_array):
        self.canvas.delete("all")
        canvas_width = 855
        canvas_height = 415
        x_width = canvas_width / (len(array_data) + 1)
        offset = 20
        spacing = 5
        normalized_array_data = [i / max(array_data) for i in array_data]

        for i, height in enumerate(normalized_array_data):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 390
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0 + 0.5 * x_width, y0 - 10, text=str(array_data[i]), anchor=S, fill="black")

        self.window.update_idletasks()
        
    def on_input(self):
        print("Input elements...")
        self.get_user_input()

    def get_user_input(self):
        user_input_element = UserInputDialog(self.window, self)
        user_input_element.grab_set()
        user_input_element.wait_window()

    def set_user_input(self, user_input):
        print("User: " ,user_input)

    def on_generate_random(self):
        print("Random:" ,self.array_data)

    def run_sort(self):
        print("Sorting Algorithm...")
        

    def on_pause(self):
        print("Pressed...")

    def on_previous(self):
        print("Previous...")


if __name__ == "__main__":
    window = Tk()
    frame = SorterUI(window)
    frame.pack()
    window.mainloop()

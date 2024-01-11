from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bubbleSort import BubbleSort
from insertionSort import InsertionSort 
from selectionSort import SelectionSort
from mergeSort import MergeSort
from quickSort import QuickSort

class MainFrame(Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.window.geometry("900x600")
        self.window.resizable(False, False)
        self.window.title("ALGORITHM SORTING VISUALIZER")

        self.label1 = Label(self.window,
                            text="ALGORITHM VISUALIZER",
                            font=('Arial', 40, 'bold'),
                            fg='red')
        self.label1.place(x=120,y=50)

        self.label2 = Label(self.window,
                            text="Select an algorithm:",
                            font=('mincho', 15, 'bold'),
                            fg='black')
        self.label2.place(x=270, y=200)

        self.options = ["--select--",
                        "Bubble Sort",
                        "Insertion Sort",
                        "Selection Sort",
                        "Merge Sort",
                        "Quick Sort"]
        
        self.combobox = ttk.Combobox(self.window,
                                     values=self.options,
                                     state='readonly',
                                     font=('Arial', 11))
        self.combobox.place(x=450, y=204)
        self.combobox.set(self.options[0])

        self.enterBtn = Button(self.window, text="ENTER",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.on_enter)
        self.enterBtn.place(x=425, y=250)

        self.enterBtn = Button(self.window, text="EXIT",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.on_exit)
        self.enterBtn.place(x=830, y=550)

        self.current_window = None

    def on_enter(self):
        selected_algorithm = self.combobox.get()

        if selected_algorithm == "Bubble Sort":
            self.destroy_current_window()
            self.current_window = BubbleSort(self)
            self.window.withdraw()
        elif selected_algorithm == "Insertion Sort":
            self.destroy_current_window()
            self.current_window = InsertionSort(self)
            self.window.withdraw()
        elif selected_algorithm == "Selection Sort":
            self.destroy_current_window()
            self.current_window = SelectionSort(self)
            self.window.withdraw()
        elif selected_algorithm == "Merge Sort":
            self.destroy_current_window()
            self.current_window = MergeSort(self)
            self.window.withdraw()
        elif selected_algorithm == "Quick Sort":
            self.destroy_current_window()
            self.current_window = QuickSort(self)
            self.window.withdraw()
        else:
            messagebox.showwarning("Invalid Input", "Select an Algorithm")


    def destroy_current_window(self):
        if self.current_window:
            self.current_window.destroy()

    def on_exit(self):
        self.window.destroy()

if __name__ == "__main__":
    window = Tk()
    frame = MainFrame(window)
    frame.pack()
    window.mainloop()

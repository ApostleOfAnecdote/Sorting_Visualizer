import json
import os
import random
import threading
from tkinter import *
from sorterUI import SorterUI

BLUE = '#3498db'
YELLOW = '#f1c40f'
PURPLE = '#9b59b6'
DARK_BLUE = '#2c3e50'


class QuickSort(SorterUI):
    def __init__(self, quick=None):
        super().__init__(quick)
        self.window.title("QUICK SORT ALGORITHM")
        self.speed = self.set_sort_speed()

        self.label1 = Label(self.window,
                            text="QUICK SORT ALGORITHM",
                            font=('Arial', 30, 'bold'),
                            fg='red')
        self.label1.pack()

        self.pause = Button(self.window, text="PAUSE",
                            fg='black',
                            bg='orange',
                            font=('Arial', 10, 'bold'),
                            command=self.on_pause)
        self.pause.place(x=560, y=100)

        self.previous = Button(self.window, text="PREVIOUS",
                               fg='black',
                               bg='orange',
                               font=('Arial', 10, 'bold'),
                               command=self.draw_last_iteration)
        self.previous.place(x=630, y=100)

        self.start_sort.configure(state=DISABLED)
        self.pause.configure(state=DISABLED)
        self.previous.configure(state=DISABLED)

        self.pause_var = BooleanVar()
        self.pause_var.set(False)

    def on_generate_random(self):
        self.array_data = [random.randint(1, 100) for _ in range(15)]
        self.array_data_draw(self.array_data, [BLUE for _ in range(len(self.array_data))])
        self.start_sort.configure(state=NORMAL)

    def set_user_input(self, user_input):
        self.array_data = user_input
        self.array_data_draw(self.array_data, [BLUE for _ in range(len(self.array_data))])
        self.start_sort.configure(state=NORMAL)

    def set_sort_speed(self):
        sort_speed = self.speed_combobox.get()
        if sort_speed == 'Slow':
            return 1
        elif sort_speed == 'Normal':
            return 0.5
        else:
            return 0.01

    def partition(self, array_data, low, high):
        speed = self.set_sort_speed()
        pivot = array_data[high]
        i = low - 1

        for j in range(low, high):
            if self.pause_var.get():
                while self.pause_var.get():
                    self.previous.configure(state=NORMAL)
                    self.window.update()
                    self.previous.configure(state=DISABLED)

            if array_data[j] < pivot:
                i += 1
                array_data[i], array_data[j] = array_data[j], array_data[i]

            color_array = [YELLOW if x == i or x == j else BLUE for x in range(len(array_data))]
            self.array_data_draw(array_data, color_array)
            self.window.update()
            self.window.after(int(speed * 500))
            print("sort speed: ", speed)

        array_data[i + 1], array_data[high] = array_data[high], array_data[i + 1]
        color_array = [YELLOW if x == i + 1 or x == high else BLUE for x in range(len(array_data))]
        self.array_data_draw(array_data, color_array)
        self.window.update()
        self.window.after(int(speed * 500))
        print("sort speed: ", speed)

        return i + 1

    def quick_sort(self, array_data, low, high):
        if low < high:
            partition_index = self.partition(array_data, low, high)

            self.quick_sort(array_data, low, partition_index - 1)
            self.quick_sort(array_data, partition_index + 1, high)

    def run_sort(self):
        self.user_input.configure(state=DISABLED)
        self.generate_random.configure(state=DISABLED)
        self.start_sort.configure(state=DISABLED)
        self.speed_combobox.configure(state=DISABLED)
        self.pause.configure(state=NORMAL)

        print("quick sort running")
        array_data = self.array_data.copy()

        self.quick_sort(array_data, 0, len(array_data) - 1)

        self.array_data_draw(array_data, [BLUE for x in range(len(array_data))])

        self.user_input.configure(state=NORMAL)
        self.generate_random.configure(state=NORMAL)
        self.start_sort.configure(state=DISABLED)
        self.speed_combobox.configure(state='readonly')
        self.pause.configure(state=DISABLED)

    def on_pause(self):
        self.pause_var.set(not self.pause_var.get())
        new_text = "RESUME" if self.pause_var.get() else "PAUSE"
        self.pause.configure(text=new_text)

    def draw_last_iteration(self):
        last_iteration = getattr(self, 'iteration', 0)
        if last_iteration > 1:
            iteration_to_draw = last_iteration - 1
            folder_path = "json_files"
            filename = os.path.join(folder_path, f"iteration_{iteration_to_draw}_data.json")

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    iteration_data = json.load(file)
                    data = iteration_data["data"]
                    color_array = [BLUE for _ in range(len(data))]

                    if "color_array" in iteration_data:
                        color_array = iteration_data["color_array"]

                    self.array_data_draw(data, color_array)

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

        iteration = getattr(self, 'iteration', 0)
        iteration += 1
        self.iteration = iteration

        folder_path = "json_files"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        filename = os.path.join(folder_path, f"iteration_{iteration}_data.json")

        with open(filename, "w") as file:
            json.dump({"data": array_data, "color_array": color_array}, file)

        self.window.update_idletasks()

if __name__ == "__main__":
    window = Tk()
    quick_frame = QuickSort(window)
    quick_frame.pack()

    sorting_thread = threading.Thread(target=quick_frame.run_sort)
    sorting_thread.start()

    window.mainloop()

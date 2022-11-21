import tkinter as tk
from tkinter import ttk
from timeit import default_timer as timer
from datetime import timedelta
import pyautogui as pag
import random
import time
import math
import threading

movements = ['random', 'back and forth', 'circular']
init_question = 'Mouse movement'
sleeping_question = 'Seconds between movements'
speed = 0.4
# sleeping = 15
runs = 0
status = ""


class App:
    def __init__(self):
        self.root = tk.Tk()

        width = 600  # Width
        height = 350  # Height
        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight()  # Height of the screen
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.root.title('Moving Mouse')
        self.root.resizable(False, False)
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid()
        self.mainframe.columnconfigure(list(range(1, 7)), minsize=(width/6)-2)
        ttk.Label(self.mainframe, text='Moving Mouse', font=("Brass Mono", 30))\
            .grid(row=0, column=2, columnspan=4, pady=12)
        ttk.Label(self.mainframe, text='Welcome to the Moving Mouse. \n '
                                       'Please specify how you want your mouse to be moved.',
                  justify='center', font=("Brass Mono", 15)).grid(row=1, column=2, columnspan=4, pady=(0, 20))
        self.init_question = ttk.Label(self.mainframe, text=init_question, font=("Brass Mono", 15))
        self.init_question.grid(row=2, column=1, columnspan=3, sticky='E')
        self.movements = ttk.Combobox(self.mainframe, values=movements)
        self.movements.grid(row=2, column=4, columnspan=2)
        self.sleeping_option = ttk.Label(self.mainframe, text=sleeping_question,
                                         background='white', font=("Brass Mono", 15))
        self.sleeping_option.grid(row=3, column=1, columnspan=3, sticky='E')
        self.sleeping = ttk.Spinbox(self.mainframe, from_=1, to=60)
        self.sleeping.grid(row=3, column=4, columnspan=2)
        s = ttk.Style()
        s.configure('my.TButton', font=("Brass Mono", 15))
        self.set_text_button = ttk.Button(self.mainframe, text="Move, bitch!",
                                          padding=20, style='my.TButton', command=lambda: self.go_button())
        self.set_text_button.grid(row=4, column=3, columnspan=2, pady=(10, 0))
        self.info = ttk.Label(self.mainframe, text="", anchor='center')
        self.info.grid(row=5, column=1, columnspan=6)
        self.kill = ttk.Button(self.mainframe, text="Quit",
                               command=lambda: threading.Thread(target=self.killing).start())
        self.kill.grid(row=6, column=3, columnspan=2, rowspan=2, sticky='S', pady=(35, 0))
        self.root.mainloop()
        return

    def moving_mouse(self):
        movement = self.movements.get()
        sleeping = int(self.sleeping.get())
        time.sleep(1)
        start = timer()

        def outcome():
            global runs
            global status
            runs += 1
            end = timer()
            time_d = timedelta(seconds=end - start)
            time_diff = str(time_d).split('.')[0]
            status = f'This code has been running {runs} {"times" if runs != 1 else "time"} for {time_diff}.'
            self.info["text"] = status
            self.info.grid(row=5, column=1, columnspan=6)
            print(status)
            time.sleep(sleeping)

        if movement == 'random':
            while True:
                x = random.randint(600, 700)
                y = random.randint(200, 600)
                pag.moveTo(x, y, speed)
                outcome()

        elif movement == 'back and forth':
            while True:
                x = 200
                y = x
                moves = 1
                for i in range(moves):
                    pag.move(x, -y, speed)
                    pag.move(-x, y, speed)
                outcome()

        elif movement == 'circular':
            while True:
                radius = 5
                for i in range(360):
                    if i % 6 == 0:
                        pag.move(radius * math.cos(math.radians(i)), radius * math.sin(math.radians(i)))
                outcome()

    def go_button(self):
        t = threading.Thread(target=self.moving_mouse)
        t.daemon = True
        t.start()

    def killing(self):
        self.root.quit()


if __name__ == '__main__':
    App()

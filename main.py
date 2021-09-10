import tkinter as tk
from tkinter import ttk
import numpy as np
import random
import numpy

# This program aims to improve an existing PRNG and make it far better.
# In general you should choose a large number on the RNG Page to get a 'more random' number.


LARGE_FONT = ("Verdana", 30)
text_font = ("Verdana", 16)



class root(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "3x + 1")
        self.geometry("1920x1080")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RNG):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    # The first window. Includes some general information

    def __init__(self, parent, controller):
        self.answer = "Answer: "
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        welcomeText = "The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows:\n\n\n Start with any positive integer n.\n Then each term is obtained from the previous term as follows:\n\n If the previous term is even, the next term is one half of the previous term.\n If the previous term is odd, the next term is 3 times the previous term plus 1. \n\n The conjecture is that no matter what value of n, the sequence will always reach 1. \n\n\n The conjecture is named after Lothar Collatz, who introduced the idea in 1937, two years after receiving his doctorate.\n\n It is also known as the 3n + 1 problem, the 3n + 1 conjecture, the Ulam conjecture (after Stanisław Ulam), Kakutani's problem (after Shizuo Kakutani),\n the Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse), or the Syracuse problem.\n\n The sequence of numbers involved is sometimes referred to as the hailstone sequence or hailstone numbers \n(because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers.\n\nPaul Erdős said about the Collatz conjecture: 'Mathematics may not be ready for such problems.'  He also offered US$500 for its solution.\n\n Jeffrey Lagarias stated in 2010 that the Collatz conjecture 'is an extraordinarily difficult problem, completely out of reach of present day mathematics.'"

        text = tk.Label(self, text=welcomeText, font=text_font).pack()
        button = ttk.Button(self, text="Start Graphing",
                            command=lambda: controller.show_frame(RNG))
        button.place(x=670, y=600)


class RNG(tk.Frame):
    # In this frame all the 'magic' happens

    def __init__(self, parent, controller):

        self.answer = "Answer: "


        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Random Number Generator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        text = tk.Label(self, text = "Choose a number: ").pack()
        number = tk.Entry(self, width=10)
        numberChosen = tk.IntVar()
        answer = tk.Label(self, text=self.answer)


        def chooseNumber():
            return number.get()

        def randomNumberGenerator():
            # Applying the 3x+1 algorithm to improve an existing PRNG

            upperLimit = 100000000  # This can be changed

            # The existing PRNG that will be used is random.randint instead
            x = random.randint(4, upperLimit)
            y = numpy.array(x)
            r = 100  # Randomness r

            for r in range(0, r):
                while x > 4:
                    if (x % 2) == 0:
                        x = x / 2
                    else:
                        x = 3 * x + 1
                    y = numpy.append(y, x)  # Adds x as the last element in y
                x = y[random.randint(0, len(y) - 1)]

            answer.configure(text="Answer: " + str(x))
            return x

        answer.pack()
        entryButton = ttk.Button(self, text="Enter", command=randomNumberGenerator).pack()
        number.pack()
        homeButton = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        homeButton.place(x=670, y=600)




app = root()
app.mainloop()
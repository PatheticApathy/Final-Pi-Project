from tkinter import *
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
forward = 20
back = 5
left = 13
right = 23
reset = 27

INTERVAL = 100
running = False

class ArrowKeys(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        master.attributes("-fullscreen", True)
        self.master = master
        #GPIO.setup(forward, GPIO.OUT)
        #GPIO.setup(back, GPIO.OUT)
        #GPIO.setup(left, GPIO.OUT)
        #GPIO.setup(right, GPIO.OUT)
        #GPIO.setup(reset, GPIO.OUT)

    def setup_GUI(self):

        def b1touchscreen():
            global running
            if running:
                #GPIO.output(forwad, GPIO.HIGH)
                window.after(INTERVAL, b1touchscreen)

        def b2touchscreen():
            global running
            if running:
                #GPIO.output(right, GPIO.HIGH)
                window.after(INTERVAL, b2touchscreen)

        def b3touchscreen():
            global running
            if running:
                #GPIO.output(left, GPIO.HIGH)
                window.after(INTERVAL, b3touchscreen)

        def b4touchscreen():
            global running
            if running:
                #GPIO.output(down, GPIO.HIGH)
                window.after(INTERVAL, b4touchscreen)

        def b5touchscreen():
            global running
            if running:
                pass
                #GPIO.output(reset, GPIO.HIGH)

        def start1(self):
            global running
            running = True
            b1touchscreen()

        def start2(self):
            global running
            running = True
            b2touchscreen()

        def start3(self):
            global running
            running = True
            b3touchscreen()

        def start4(self):
            global running
            running = True
            b4touchscreen()

        def start5(self):
            global running
            running = True
            b5touchscreen()

        def stop(self):
            global running
            running = False
            #GPIO.output(forward, GPIO.LOW)
            #GPIO.output(back, GPIO.LOW)
            #GPIO.output(left, GPIO.LOW)
            #GPIO.output(right, GPIO.LOW)
            #GPIO.outpur(reset, GPIO.LOW)
        
        b6 = Button(self.master, text="Exit", bg="red", command=exit)
        b6.pack(anchor=NE)
        b6.configure(font=("Times New Roman", 20, "bold"))

        b5 = Button(self.master, text="Reset Accelerometer", bg="red")
        b5.pack(anchor=NW)
        b5.configure(font=("Times New Roman", 20, "bold"))

        b1 = Button(self.master, text="↑", bg="tan")
        b1.pack(ipadx=55, ipady=50)
        b1.configure(font=("Times New Roman", 20, "italic"))

        b2 = Button(self.master, text="→", bg="tan")
        b2. pack(ipadx=50, ipady=50, side=RIGHT, expand=True)
        b2.configure(font=("Times New Roman", 20, "italic"))

        b3 = Button(self.master, text="←", bg="tan")
        b3.pack(ipadx=50, ipady=50, side=LEFT, expand=True)
        b3.configure(font=("Times New Roman", 20, "italic"))

        b4 = Button(self.master, text="↓", bg="tan")
        b4.pack(ipadx=55, ipady=50, side=BOTTOM, expand=True)
        b4.configure(font=("Times New Roman", 20, "italic"))

        b1.bind("<ButtonPress-1>", start1)
        b1.bind("<ButtonRelease-1>", stop)
        b2.bind("<ButtonPress-1>", start2)
        b2.bind("<ButtonRelease-1>", stop)
        b3.bind("<ButtonPress-1>", start3)
        b3.bind("<ButtonRelease-1>", stop)
        b4.bind("<ButtonPress-1>", start4)
        b4.bind("<ButtonRelease-1>", stop)
        b5.bind("<ButtonPress-1>", start5)
        b5.bind("<ButtonRelease-1>", stop)

window = Tk()

k = ArrowKeys(window)
k.setup_GUI()

window.config(bg="green")
window.title("ArrowKeys")
window.mainloop()
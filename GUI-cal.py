from tkinter import *

screen = Tk()
screen.title('Yantra')
screen.geometry('280x450')

value1 = Entry(screen, bg = 'white', font=('arial',18,'bold'), bd = 8, justify = 'right')
value1.grid(row = 0, column = 0)

screen.mainloop()
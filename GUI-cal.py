from tkinter import *

screen = Tk()
screen.title('Yantra')
screen.geometry('280x310')

#adding the value screen 

value1 = Entry(screen, bg = 'white', font=('arial',18,'bold'), bd = 8, justify = 'right')
value1.grid(row = 0, columnspan = 4)

#Adding the number keys/buttons

#--------1st row-----------

k7 = Button(screen,text = '7', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k7.grid(row = 1,column = 0)

k8 = Button(screen,text = '8', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k8.grid(row = 1,column = 1)

k9 = Button(screen,text = '9', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k9.grid(row = 1,column = 2)

kadd = Button(screen,text = '+', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
kadd.grid(row = 1,column = 3)

#--------2nd row-----------

k4 = Button(screen,text = '4', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k4.grid(row = 2,column = 0)

k5 = Button(screen,text = '5', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k5.grid(row = 2,column = 1)

k6 = Button(screen,text = '6', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k6.grid(row = 2,column = 2)

ksub = Button(screen,text = '-', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
ksub.grid(row = 2,column = 3)

#--------3rd row-----------

k1 = Button(screen,text = '1', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k1.grid(row = 3,column = 0)

k2 = Button(screen,text = '2', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k2.grid(row = 3,column = 1)

k3 = Button(screen,text = '3', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k3.grid(row = 3,column = 2)

kmul = Button(screen,text = 'x', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
kmul.grid(row = 3,column = 3)

#--------4th row-----------

kclear = Button(screen,text = 'C', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
kclear.grid(row = 4,column = 0)

k0 = Button(screen,text = '0', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
k0.grid(row = 4,column = 1)

keq = Button(screen,text = '=', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
keq.grid(row = 4,column = 2)

kdiv = Button(screen,text = '÷', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
kdiv.grid(row = 4,column = 3)



screen.mainloop()
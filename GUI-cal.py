from tkinter import *

screen = Tk()
screen.title('Yantra')
screen.geometry('280x310')

#function to enter values using buttons 
def click(number):
	global operator
	operator += str(number)
	tvar.set(operator)

#function to clear the inputs
def clear():
	global operator
	operator = ''
	tvar.set(operator)


#adding the value screen 

tvar = StringVar()
operator = ''

value1 = Entry(screen, bg = 'white', font=('arial',18,'bold'), bd = 8, justify = 'right', textvariable = tvar)
value1.grid(row = 0, columnspan = 4)

#Adding the number keys/buttons

#--------1st row-----------

k7 = Button(screen,text = '7', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(7))
k7.grid(row = 1,column = 0)

k8 = Button(screen,text = '8', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(8))
k8.grid(row = 1,column = 1)

k9 = Button(screen,text = '9', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(9))
k9.grid(row = 1,column = 2)

kadd = Button(screen,text = '+', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('+'))
kadd.grid(row = 1,column = 3)

#--------2nd row-----------

k4 = Button(screen,text = '4', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(4))
k4.grid(row = 2,column = 0)

k5 = Button(screen,text = '5', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(5))
k5.grid(row = 2,column = 1)

k6 = Button(screen,text = '6', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(6))
k6.grid(row = 2,column = 2)

ksub = Button(screen,text = '-', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('-'))
ksub.grid(row = 2,column = 3)

#--------3rd row-----------

k1 = Button(screen,text = '1', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(1))
k1.grid(row = 3,column = 0)

k2 = Button(screen,text = '2', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(2))
k2.grid(row = 3,column = 1)

k3 = Button(screen,text = '3', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(3))
k3.grid(row = 3,column = 2)

kmul = Button(screen,text = 'x', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('x'))
kmul.grid(row = 3,column = 3)

#--------4th row-----------

kclear = Button(screen,text = 'C', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = clear)
kclear.grid(row = 4,column = 0)

k0 = Button(screen,text = '0', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(0))
k0.grid(row = 4,column = 1)

keq = Button(screen,text = '=', font=('arial',15,'bold'), bd = 5,padx=12,pady=7)
keq.grid(row = 4,column = 2)

kdiv = Button(screen,text = '÷', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('÷'))
kdiv.grid(row = 4,column = 3)



screen.mainloop()
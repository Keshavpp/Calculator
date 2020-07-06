from tkinter import *

screen = Tk()
screen.title('YANTRA') #name of calculator
screen.configure(bg = 'gray') #backgroud colour of calc

#max & min size of the calc tab
screen.maxsize(width =280 , height =295 ) 
screen.minsize(width =280, height = 295)

#setting icon for appl
screen.iconbitmap('calc.ico')

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

#function to find result of query
def equalsTo():
	global operator
	answer = eval(operator)
	operator = str(answer)
	tvar.set(answer)



#adding the value screen 

tvar = StringVar()
operator = ''

value1 = Entry(screen, bg = 'white', font=('arial',18,'bold'), bd = 8, justify = 'right', textvariable = tvar)
value1.grid(row = 0, columnspan = 4)

#Adding the number keys/buttons

#--------1st row-----------

k7 = Button(screen,text = '7', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(7),activebackground='black', activeforeground ='white') 
k7.grid(row = 1,column = 0)

k8 = Button(screen,text = '8', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(8),activebackground='black', activeforeground ='white')
k8.grid(row = 1,column = 1)

k9 = Button(screen,text = '9', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(9),activebackground='black', activeforeground ='white')
k9.grid(row = 1,column = 2)

kadd = Button(screen,text = '+', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('+'),activebackground='black', activeforeground ='white')
kadd.grid(row = 1,column = 3)

#--------2nd row-----------

k4 = Button(screen,text = '4', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(4),activebackground='black', activeforeground ='white')
k4.grid(row = 2,column = 0)

k5 = Button(screen,text = '5', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(5),activebackground='black', activeforeground ='white')
k5.grid(row = 2,column = 1)

k6 = Button(screen,text = '6', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(6),activebackground='black', activeforeground ='white')
k6.grid(row = 2,column = 2)

ksub = Button(screen,text = '-', font=('arial',15,'bold'), bd = 5,padx=14,pady=7,command = lambda:click('-'),activebackground='black', activeforeground ='white')
ksub.grid(row = 2,column = 3)

#--------3rd row-----------

k1 = Button(screen,text = '1', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(1),activebackground='black', activeforeground ='white')
k1.grid(row = 3,column = 0)

k2 = Button(screen,text = '2', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(2),activebackground='black', activeforeground ='white')
k2.grid(row = 3,column = 1)

k3 = Button(screen,text = '3', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(3),activebackground='black', activeforeground ='white')
k3.grid(row = 3,column = 2)

kmul = Button(screen,text = 'x', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('*'),activebackground='black', activeforeground ='white')
kmul.grid(row = 3,column = 3)

#--------4th row-----------

kclear = Button(screen,text = 'C', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = clear,activebackground='black', activeforeground ='white')
kclear.grid(row = 4,column = 0)

k0 = Button(screen,text = '0', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click(0),activebackground='black', activeforeground ='white')
k0.grid(row = 4,column = 1)

keq = Button(screen,text = '=', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = equalsTo,activebackground='black', activeforeground ='white')
keq.grid(row = 4,column = 2)

kdiv = Button(screen,text = '÷', font=('arial',15,'bold'), bd = 5,padx=12,pady=7,command = lambda:click('/'),activebackground='black', activeforeground ='white')
kdiv.grid(row = 4,column = 3)



screen.mainloop()
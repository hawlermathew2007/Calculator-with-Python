from tkinter import *

#\u03C0
#\u221A

def button_press(num):
	
	global equatext

	equatext = equatext + str(num)

	equalabel.set(equatext)

def equal():
	
	global equatext

	try:
		total = str(eval(equatext))

		equalabel.set(total)

		equatext = total 

	except SyntaxError:
		equalabel.set("SyntaxError")
		equatext = ""

	except ZeroDivisionError:
		equalabel.set("ArithmethicError")
		equatext = ""

	except TypeError:
		equalabel.set("SyntaxError")
		equatext = ""

	if equatext == "":
		equalabel.set("PleaseEnterNumber")

def clear():
	
	global equatext

	equalabel.set("")

	equatext = ""

window = Tk()
window.title("Calculator")
# window.geometry("455x414")

equatext = ""
equalabel = StringVar()

label = Label(window,textvariable=equalabel,font=("Consolas",20),bg='white',width=30,height=2,padx=2,justify=LEFT)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,width=9,height=4,font=35,
	command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,width=9,height=4,font=35,
	command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,width=9,height=4,font=35,
	command=lambda: button_press(3))
button3.grid(row=0,column=2)

button3 = Button(frame,text=3,width=9,height=4,font=35,
	command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,width=9,height=4,font=35,
	command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,width=9,height=4,font=35,
	command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,width=9,height=4,font=35,
	command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,width=9,height=4,font=35,
	command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,width=9,height=4,font=35,
	command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,width=9,height=4,font=35,
	command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,width=9,height=4,font=35,
	command=lambda: button_press(0))
button0.grid(row=3,column=0)

b_open = Button(frame,text='(',width=9,height=4,font=35,
	command=lambda: button_press('('))
b_open.grid(row=0,column=3)

b_close = Button(frame,text=")",width=9,height=4,font=35,
	command=lambda: button_press(")"))
b_close.grid(row=0,column=4)

decimal = Button(frame,text=".",width=9,height=4,font=55,
	command=lambda: button_press("."))
decimal.grid(row=3,column=1)

equal = Button(frame,text="=",width=20,height=4,font=45,command=equal)
equal.grid(row=3,column=3,columnspan=2)

clear = Button(frame,text="AC",width=9,height=4,font=35,command=clear)
clear.grid(row=3,column=2)

multply = Button(frame,text="x",width=9,height=4,font=45,
	command=lambda: button_press("*"))
multply.grid(row=1,column=3)

divide = Button(frame,text="/",width=9,height=4,font=45,
	command=lambda: button_press("/"))
divide.grid(row=1,column=4)

plus = Button(frame,text="+",width=9,height=4,font=45,
	command=lambda: button_press("+"))
plus.grid(row=2,column=3)

minus = Button(frame,text="-",width=9,height=4,font=45,
	command=lambda: button_press("-"))
minus.grid(row=2,column=4)

window.mainloop()
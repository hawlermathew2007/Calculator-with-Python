from tkinter import *
import math

def submit():

	a = float(entry1.get())
	b = float(entry2.get())
	c = float(entry3.get())

	delta = result_delta(a,b,c)

	txt.set("delta = " + str(b) + "^2" + "-" + "4" + "." + str(a) + "." + str(c) + " = " + str(delta))
	equa.set("Your equation is: " + str(a) + "x^2" + " + " + str(b) + "x" + " + " + str(c))

	separator = Label(window, text="").grid(row=3,column=0,columnspan=2)
	displayequation = Label(window,textvariable=equa).grid(row=4,column=0,columnspan=2,sticky=W)
	displaydelta = Label(window,textvariable= txt).grid(row=5,column=0,columnspan=2,sticky=W)

	def delete():
		ask1.destroy()
		sure.destroy()
		nah.destroy()
		entry1.insert(END, '')
		entry2.insert(END, '')
		entry3.insert(END, '')

	if delta < 0:

		separator1 = Label(window, text="---------------------------------").grid(row=6,column=0,columnspan=2,sticky=W)
		unsolvable = Label(window,text="The equation is unsolvable.").grid(row=7,column=0,columnspan=2,sticky=W)

		separator4 = Label(window, text="---------------------------------").grid(row=8,column=0,columnspan=2,sticky=W)
		separator5 = Label(window, text="").grid(row=9,column=0,columnspan=2,sticky=W)

	elif delta > 0:

		separator1 = Label(window, text="---------------------------------").grid(row=6,column=0,columnspan=2,sticky=W)
		solvable = Label(window,text="The equation has 2 result.").grid(row=7,column=0,columnspan=2,sticky=W)

		x1 = lambda a,b: (-b + math.sqrt(delta))/2*a
		x2 = lambda a,b: (-b - math.sqrt(delta))/2*a

		rx1.set("x1 = " + str(x1(a,b)))
		rx2.set("x2 = " + str(x2(a,b)))

		separator2 = Label(window, text="---------------------------------").grid(row=8,column=0,columnspan=2,sticky=W)
		r_x1 = Label(window,textvariable=rx1).grid(row=9,column=0,columnspan=2,sticky=W)
		r_x2 = Label(window,textvariable=rx2).grid(row=10,column=0,columnspan=2,sticky=W) 

	elif delta == 0:

		separator2 = Label(window, text="---------------------------------").grid(row=6,column=0,columnspan=2,sticky=W)
		double_e = Label(window,text="The equation has double result.").grid(row=7,column=0,columnspan=2,sticky=W)

		x1x2 = lambda a,b: -b/(2*a)

		rx1x2.set("x1 = " + str(round(x1x2(a,b))))

		separator3 = Label(window, text="---------------------------------").grid(row=8,column=0,columnspan=2,sticky=W)
		r_x1x2 = Label(window,textvariable=rx1x2).grid(row=9,column=0,columnspan=2,sticky=W)

	ask1 = Label(window,text="Do you wanna calculate again?")
	ask1.grid(row=12,column=0,columnspan=2,sticky=W)

	sure = Button(window,text="Sure", command=delete)
	sure.grid(row=12,column=1,columnspan=1,padx=50,sticky=W)

	nah = Button(window,text="No", command=quit)
	nah.grid(row=12,column=1,columnspan=1,stick=E)


def result_delta(a,b,c):
	return float(b)**2 - 4*float(a)*float(c)


def yes():
	global ask1
	global sure
	global nah

	ask1.destroy()
	sure.destroy()
	nah.destroy()

window = Tk()

txt = StringVar()
equa = StringVar()
rx1 = StringVar()
rx2 = StringVar()
rx1x2 = StringVar()

window.geometry("380x420")

label1 = Label(window,text="a").grid(row=0,column=0)
entry1 = Entry(window)
entry1.grid(row=1,column=0)

label2 = Label(window,text="b").grid(row=0,column=1,padx=5)
entry2 = Entry(window)
entry2.grid(row=1,column=1,padx=5)

label3 = Label(window,text="c").grid(row=0,column=2)
entry3 = Entry(window)
entry3.grid(row=1,column=2)

submit = Button(window,text="submit", command=submit).grid(row=2,column=0,columnspan=3)

window.mainloop()
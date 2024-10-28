from tkinter import *
import math 
import random
# should add some good looking result: 1/2pi, sqrt(2), fraction

# problem: pi is still like string data type when go with other digit
# solution return error or make multi with the left nearest digit (if syntax such as "x" or "!" ignore)
# problem: the computer thing is still if player type "xx" and "//"
# solution: check if next to "x" or "/" has digit

def button_press(num):
	
	global equatext
	global display

	equatext.append(num)
	print(equatext)

	for i in equatext:
		display += str(i)

	equalabel.set(display)
	display = ""


def clear():
	
	global equatext

	equalabel.set("")

	display = ""
	equatext = []

def delete():
	
	global equatext
	global display

	if equatext == []:
		return

	equatext.remove(equatext[len(equatext)-1])

	for i in equatext:
		display += str(i)

	equalabel.set(display)
	display = ""

def equal():
	
	global equatext

	try:
		short = 0
		for i in range(len(equatext)):
			short = 0
			if equatext[i] == "x" or equatext[i] == u'\u00F7' or equatext[i] == u'\u03C0':
				if equatext[i] == "x":
					syntax = "*"
				elif equatext[i] == u'\u00F7':
					syntax = "/"
				else:
					syntax = math.pi

				remove_elem = equatext[i]
				short = 1

			if short == 1:
				equatext.remove(remove_elem)
				equatext.insert(i, syntax)

		total_string = ""

		factorial_string = ""
		math_syntax = ["*", "/", "+", "-"]

		if "%" in equatext or "!" in equatext:	#problem 3! x 3!
			x = "no"
			if "%" in equatext:
				x = equatext.index("%")
			if "!" in equatext:
				x = equatext.index("!")
			if x == 0 or not str(equatext[x-1]).isdigit():
				equalabel.set("SyntaxError")
				equatext = []
				return
			if x <= len(equatext) - 2 and str(equatext[x+1]).isdigit():
				equalabel.set("SyntaxError")
				equatext = []
			i = 0
			while i < len(equatext):
				factorial = False
				percent = False
				string = ""
				temp = []
				k = 0
				print(i)
				if equatext[i] == "!" or equatext[i] == "%":
					if equatext[i] == "!":
						factorial = True
					else:
						percent = True
					for b in range(i):
						if equatext[i-(b+1)] in math_syntax:
							k = i-(b+1)
							break
						string += str(equatext[i-(b+1)])
					if factorial:
						result = math.factorial(int(string[::-1]))
					if percent:
						result = float(string[::-1])/100 
					indexes = []
					temp = equatext

					if k == 0:
						indexes = [0]

					for a in range(k, i):
						indexes.append(a+1)

					equatext = []
					for b in range(len(temp)):
						if b in indexes:
							continue
						equatext.append(temp[b])

					if k == 0:
						equatext.insert(0, result)
					else:
						equatext.insert(k+1, result)

				i += 1

		if "\u221A" in equatext: # This part is not working, so no square root

			indexOf_sqrt = equatext.index("\u221A")
			numberOf_sqrtSymbol = equatext.count("\u221A")
			fromSqrtToEnd_list = equatext[equatext.index("\u221A"):len(equatext)]
			in_parenthesis_asString = ""

			for i in range(numberOf_sqrtSymbol):
				indexOf_closeParenthesis = fromSqrtToEnd_list.index(")")
				in_parenthesis_asList = fromSqrtToEnd_list[1:indexOf_closeParenthesis-1]
				in_parenthesis_asString = ''.join(in_parenthesis_asList)
				valueOf_sqrt = str(math.sqrt(eval(in_parenthesis_asString)))
				fromSqrtToEnd_list = fromSqrtToEnd_list[indexOf_closeParenthesis+1, len(fromSqrtToEnd_list)]
				equatext = [num for num in equatext if item not in equatext[equatext.index("\u221A"):indexOf_closeParenthesis]]
				equatext.insert(indexOf_sqrt, valueOf_sqrt)
				indexOf_sqrt = equatext.index("\u221A")
			

		for i in equatext:
			total_string += str(i)
		
		total = str(eval(total_string))

		equalabel.set(total)

		equatext = [total]

	except SyntaxError:
		equalabel.set("SyntaxError")
		equatext = []

	except ZeroDivisionError:
		equalabel.set("ArithmethicError")
		equatext = []

	except TypeError:
		equalabel.set("SyntaxError")
		equatext = []

	if equatext == []:
		equalabel.set("PleaseEnterNumber")
		print(equatext)

window = Tk()
window.title("Calculator")
window.resizable(False, False)

equatext = []
display = ""
equalabel = StringVar()

label = Label(window,textvariable=equalabel,font=("Consolas",20),bg='white',width=42,height=2,padx=2,justify=LEFT)
label.pack()

frame = Frame(window)
frame.pack()

b_open = Button(frame,text='(',width=9,height=4,font=35,
	command=lambda: button_press('('))
b_open.grid(row=0,column=0)

b_close = Button(frame,text=")",width=9,height=4,font=35,
	command=lambda: button_press(")"))
b_close.grid(row=0,column=1)

ran = Button(frame, text= "Ran#",width=9,height=4,font=35,
	command=lambda: button_press("Ran#"))
ran.grid(row= 0, column= 2)

ranint = Button(frame, text= "RanInt",width=9,height=4,font=35,
	command=lambda: button_press("RanInt#("))
ranint.grid(row= 0, column= 3)

colon = Button(frame, text= ",",width=9,height=4,font=35,
	command=lambda: button_press(","))
colon.grid(row= 0, column= 4)

_del = Button(frame, text= "DEL",width=9,height=4,font=35,
	command= lambda: delete()) #missing a command
_del.grid(row= 0, column= 5)

ac = Button(frame, text= "AC",width=9, height=4, font=35,
	command=lambda: clear())
ac.grid(row= 0, column= 6)

percent = Button(frame, text= "%",width=9,height=4,font=35,
	command=lambda: button_press("%"))
percent.grid(row= 1, column= 0)

sqrt = Button(frame, text= u"\u221A",width=9,height=4,font=35,
	command=lambda: button_press(u'\u221A'+"("))
sqrt.grid(row= 1, column= 1)

b1 = Button(frame, text= 1,width=9,height=4,font=35,
	command=lambda: button_press(1))
b1.grid(row= 1, column= 2)

b2 = Button(frame, text= 2,width=9,height=4,font=35,
	command=lambda: button_press(2))
b2.grid(row= 1, column= 3)

b3 = Button(frame, text= 3,width=9,height=4,font=35,
	command=lambda: button_press(3))
b3.grid(row= 1, column= 4)

multiple = Button(frame, text= "x",width=9,height=4,font=35,
	command=lambda: button_press("x"))
multiple.grid(row= 1, column= 5)

divide = Button(frame, text= u'\u00F7',width=9,height=4,font=35,
	command=lambda: button_press(u'\u00F7'))
divide.grid(row= 1, column= 6)

cos = Button(frame, text= "cos",width=9,height=4,font=35,
	command=lambda: button_press("cos("))
cos.grid(row= 2, column= 0)

tan = Button(frame, text= "tan",width=9,height=4,font=35,
	command=lambda: button_press("tan("))
tan.grid(row= 2, column= 1)

b4 = Button(frame, text= 4,width=9,height=4,font=35,
	command=lambda: button_press(4))
b4.grid(row= 2, column= 2)

b5 = Button(frame, text= 5,width=9,height=4,font=35,
	command=lambda: button_press(5))
b5.grid(row= 2, column= 3)

b6 = Button(frame, text= 6,width=9,height=4,font=35,
	command=lambda: button_press(6))
b6.grid(row= 2, column= 4)

plus = Button(frame, text= "+",width=9,height=4,font=35,
	command=lambda: button_press("+"))
plus.grid(row= 2, column= 5)

minus = Button(frame, text= "-",width=9,height=4,font=35,
	command=lambda: button_press("-"))
minus.grid(row= 2, column= 6)

sin = Button(frame, text= "sin",width=9,height=4,font=35,
	command=lambda: button_press("sin("))
sin.grid(row= 3, column= 0)

exclam = Button(frame, text= "!",width=9,height=4,font=35,
	command=lambda: button_press("!"))
exclam.grid(row= 3, column= 1)

b7 = Button(frame, text= 7,width=9,height=4,font=35,
	command=lambda: button_press(7))
b7.grid(row= 3, column= 2)

b8 = Button(frame, text= 8,width=9,height=4,font=35,
	command=lambda: button_press(8))
b8.grid(row= 3, column= 3)

b9 = Button(frame, text= 9,width=9,height=4,font=35,
	command=lambda: button_press(9))
b9.grid(row= 3, column= 4)

r_sqrt = Button(frame, text= "R_" + u"\u221A",width=9,height=4,font=35)		# need particular command
r_sqrt.grid(row= 3, column= 5)

r_pi = Button(frame, text= "R_" + u'\u03C0',width=9,height=4,font=35)		# need particular command
r_pi.grid(row= 3, column= 6)

expond = Button(frame, text= "^",width=9,height=4,font=35,
	command=lambda: button_press("^("))
expond.grid(row= 4, column= 0)

pi = Button(frame, text= u'\u03C0',width=9,height=4,font=35,
	command=lambda: button_press(u'\u03C0'))
pi.grid(row= 4, column= 1)

zero = Button(frame, text= 0,width=9,height=4,font=35,
	command=lambda: button_press(0))
zero.grid(row= 4, column= 2)

dot = Button(frame, text= ".",width=9,height=4,font=35,
	command=lambda: button_press("."))
dot.grid(row= 4, column= 3)

ans = Button(frame, text= "Ans",width=9,height=4,font=35, 
	command= lambda: button_press("Ans"))
ans.grid(row= 4, column= 4)

# minus = Button(frame, text= "-",width=9,height=4,font=35,
# 	command=lambda: button_press("-"))
# minus.grid(row= 4, column= 5)

equal = Button(frame,text="=",width=19,height=4,font=35,command=equal)
equal.grid(row=4,column=5,columnspan=6)

window.mainloop()
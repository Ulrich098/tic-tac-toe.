from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic Tac Toe')
tk.resizable(0,0)


click = True

def checker(buttons):
	global click
	if buttons['text'] == ' ' and click == True:
		buttons['text'] = 'X'
		click = False
		
	elif buttons['text'] == ' ' and click == False:
		buttons['text'] = 'O'
		click = True
                        
	elif check() == True:
	    tkinter.messagebox.showinfo('Warming',' Hey! This Button Already Pressed')
	
	
                
	if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
		button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
		button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
		button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
		button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
		button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
		button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
		button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X') :
	    tkinter.messagebox.showinfo('Winner X','You have just won a game')
	   

	if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
		button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
		button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
		button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
		button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
		button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
		button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
		button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O') :
	    tkinter.messagebox.showinfo('Winner O','You have just won a game')

	if (button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and
		button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and
		button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' ') :
	    tkinter.messagebox.showinfo('Draw','No one won!')
	    clear()
	    
def check():
        if (button1['text'] == 'X' or button1['text'] == 'O' or
                button2['text'] == 'X' or button2['text'] == 'O' or
                button3['text'] == 'X' or button3['text'] == 'O' or
                button4['text'] == 'X' or button4['text'] == 'O' or
                button5['text'] == 'X' or button5['text'] == 'O' or
                button6['text'] == 'X' or button6['text'] == 'O' or
                button7['text'] == 'X' or button7['text'] == 'O' or
                button8['text'] == 'X' or button8['text'] == 'O' or
                button9['text'] == 'X' or button9['text'] == 'O') :
            return True

def clear():
        button1['text'] = ' '
        button2['text'] = ' '
        button3['text'] = ' '
        button4['text'] = ' '
        button5['text'] = ' '
        button6['text'] = ' '
        button7['text'] = ' '
        button8['text'] = ' '
        button9['text'] = ' '



        
button1 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button1))
button1.grid(row=1, column=0)

button2 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button2))
button2.grid(row=1, column=1)

button3 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4,  command=lambda:checker(button3))
button3.grid(row=1, column=2)

button4 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button4))
button4.grid(row=2, column=0)

button5 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button5))
button5.grid(row=2, column=1)

button6 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button6))
button6.grid(row=2, column=2)

button7 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button7))
button7.grid(row=3, column=0)

button8 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button8))
button8.grid(row=3, column=1)

button9 = Button(tk,text=' ', font=('Times 26 bold'), height = 3, width =8, borderwidth=4, command=lambda:checker(button9))
button9.grid(row=3, column=2)

button10 = Button(tk,text='Clear', font=('Times 26 bold'), height = 1, width =8, command=lambda:clear())
button10.grid(row=4, columnspan=3)



tk.mainloop()

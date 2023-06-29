from tkinter import *

def afficher() :
 if (check1.get() + check2.get() + check3.get() + check4.get() > 1) :
    output = 'too many options selected'
 else :
    nombre1=int(entry1.get())
    nombre2=int(entry2.get())
    if check1.get() :
        output = nombre1 + nombre2
    elif check2.get() :
        output = nombre1 - nombre2
    elif check3.get() :
        output = nombre1 * nombre2
    elif check4.get() :
        output = round(nombre1/nombre2,2)
    else :
        output = 'choice between : +, -, x, /'

 sorty1.delete(0, 'end')
 sorty1.insert(0, output)

window = Tk()
window.geometry('600x280')
window.title("Simple calculate snake")
label1 = Label(window, text='Calculate', fg = 'white', bg = 'grey', font = ('Arial', 32))

button1 = Button(window, text = 'Calcul', width = 10, height = 2, command = afficher, fg = 'white', bg = 'green', font = ('Arial', 10))

entry1 = Entry(fg = 'black', bg = 'yellow', font = ('Arial', 12))
entry2 = Entry(fg = 'black', bg = 'yellow', font = ('Arial', 12))
sorty1 = Entry(fg = 'black', bg = 'green', font = ('Arial', 15), width = 40)

check1=IntVar()
check2=IntVar()
check3=IntVar()
check4=IntVar()

checkbutton1 = Checkbutton(window, text = "Plus", variable=check1)
checkbutton2 = Checkbutton(window, text = "Moins", variable=check2)
checkbutton3 = Checkbutton(window, text = "Multipl", variable=check3)
checkbutton4 = Checkbutton(window, text = "Div", variable=check4)

entry1.grid(row = 1, column = 1, padx = 10, pady = 10)
entry2.grid(row = 1, column = 2, padx = 10, pady = 10)

checkbutton1.grid(row = 2, column = 0, padx = 10, pady = 10)
checkbutton2.grid(row = 2, column = 1, padx = 10, pady = 10)
checkbutton3.grid(row = 2, column = 2, padx = 10, pady = 10)
checkbutton4.grid(row = 2, column = 3, padx = 10, pady = 10)

button1.grid(row = 3, column = 1, columnspan = 2, pady = 10)

sorty1.grid(row = 4, column = 1, columnspan = 2, pady = 10)

window.mainloop()

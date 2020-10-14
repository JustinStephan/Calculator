import tkinter as tk

window = tk.Tk()

def buttonPress(button):
    newText = button
    if button == 'C':
        newText = ''
    
    entryText.set(newText)
    print(button)

def makeButtons(buttons,row, column):
    r = row
    c = column
    for button in buttons:
        tk.Button(
            window,
            text = button, 
            width = 5, 
            height = 2, 
            command = lambda b=button: buttonPress(b)).grid(row = r, column = c)
        r +=1
def updateEntry(entry):
    e = 'placeholder'

entryText = tk.StringVar()
entry = tk.Entry(window, textvariable = entryText).grid(row = 0, column = 0, rowspan = 2, columnspan = 5)
column1 = ['(','7','4','1','+/-']
makeButtons(column1,2,0)

column2 = [')','8','5','2','0']
makeButtons(column2,2,1)

column3 = ['C','9','6','3','.']
makeButtons(column3,2,2)

column4 = ['/','x','-','+','=']
makeButtons(column4,2,3)


window.mainloop()
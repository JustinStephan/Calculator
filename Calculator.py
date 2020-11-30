import tkinter as tk

root = tk.Tk()
root.title('Calculator')


numStack = ''
equation = ''
answer = False
def buttonPress(button):
    global numStack
    global equation
    global answer 

    if button == 'C':
        answer = False
        numStack, newText, equation = '', '', ''

    if button.isnumeric() or button == '.':
        if answer is True:
            print ('huge dump')
            numStack = ''
            answer = False
        numStack = numStack + button

    if button == '-' or button =='+' or button =='x' or button =='/':
        answer = False
        if button == 'x':
            button = '*'
        equation = equation + numStack + button
        numStack = ''

    if button == '=':
        equation = equation + numStack
        numStack = str(eval(equation))
        equation = ''
        if float(numStack) == int(float(numStack)):
            numStack = str(int(float(numStack)))
        answer = True

    if button == '+/-':
        answer = False
        if numStack != '':
            if '-' in numStack:
                numStack = numStack.replace('-','')
            else:
                numStack = '-' + numStack

    newText = numStack
    entryText.set(newText)
    
    

def makeButtons(buttons,row, column):
    r = row
    c = column
    for button in buttons:
        tk.Button(
            root,
            font = ('helvetica', 14),
            text = button, 
            width = 7, 
            height = 3, 
            command = lambda b=button: buttonPress(b)).grid(row = r, column = c)
        r +=1
def updateEntry(entry):
    e = 'placeholder'


entryText = tk.StringVar()
entry = tk.Entry(root, textvariable = entryText, width=17, font = ('helvetica', 24)).grid(row = 0, column = 0, rowspan = 1, columnspan = 4)

column1 = ['','7','4','1','+/-']
column2 = ['','8','5','2','0']
column3 = ['C','9','6','3','.']
column4 = ['/','x','-','+','=']


makeButtons(column1,2,0)
makeButtons(column2,2,1)
makeButtons(column3,2,2)
makeButtons(column4,2,3)


root.mainloop()
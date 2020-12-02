import tkinter as tk

class Calculator:
    numStack = ''
    equation = ''
    answer = False
    columns = []

    def __init__(self,columns):
        self.columns = columns
        self.createWindow()
        
        self.root.mainloop()

    def createWindow(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.entryText = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable = self.entryText, width=17, font = ('helvetica', 24)).grid(row = 0, column = 0, rowspan = 1, columnspan = 4)
        self.makeButtons()   
             
    def makeButtons(self):
        for column in range(0, len(self.columns)):
            r = 2
            c = column
            for button in self.columns[column]:
                tk.Button(
                    self.root,
                    font = ('helvetica', 14),
                    text = button, 
                    width = 7, 
                    height = 3, 
                    command = lambda b=button: self.buttonPress(b)).grid(row = r, column = c)
                r +=1

    def buttonPress(self, button):
        if button == 'C':
            self.answer = False
            self.numStack, self.newText, self.equation = '', '', ''

        if button.isnumeric() or button == '.':
            if self.answer is True:
                self.numStack = ''
                self.answer = False
            self.numStack = self.numStack + button

        if button == '-' or button =='+' or button =='x' or button =='/':
            self.answer = False
            if button == 'x':
                button = '*'
            self.equation = self.equation + self.numStack + button
            self.numStack = ''

        if button == '=':
            self.equation = self.equation + self.numStack
            self.numStack = str(eval(self.equation))
            self.equation = ''
            if float(self.numStack) == int(float(self.numStack)):
                self.numStack = str(int(float(self.numStack)))
            self.answer = True

        if button == '+/-':
            self.answer = False
            if self.numStack != '':
                if '-' in self.numStack:
                    self.numStack = self.numStack.replace('-','')
                else:
                    self.numStack = '-' + self.numStack

        self.newText = self.numStack
        self.entryText.set(self.newText)

columns = [['','7','4','1','+/-'],
            ['','8','5','2','0'],
            ['C','9','6','3','.'],
            ['/','x','-','+','=']]

Calculator(columns)
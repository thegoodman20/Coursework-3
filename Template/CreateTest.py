from tkinter import *
from Response import Response
from tkinter import messagebox
import csv
class Create_Test(Frame):
# GUI Setup
    def __init__ (self, master):
# Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.grid()
        self.createTest()
        self.createButtons()
    def createTest(self):
        lblQuestion = Label(self, text = 'Question 1', font=('MS', 8,'bold'))
        lblQuestion.grid(row=3, column= 4, rowspan=2)
        self.Question = Text(self, height=3,width=40)
        scroll = Scrollbar(self, command=self.Question.yview)
        self.Question.configure(yscrollcommand=scroll.set)
        self.Question.grid(row=12, column=2,columnspan=5, sticky=E)
        scroll.grid(row=12, column=7, sticky=W)
        self.Question.insert(END, "INPUT QUESTION HERE")
        lblAnswer = Label(self, text = 'Choice 1', font=('MS', 8,'bold'))
        lblAnswer.grid(row=13, column= 4, rowspan=2)
        #rename this
        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB1)
        CB1.grid(row=13, column=5, columnspan=1, sticky=W)
        self.Answer1 = Text(self, height=1,width=40)
        self.Answer1.grid(row=16, column=2,columnspan=5, sticky=E)
        self.Answer1.insert(END, "INPUT FIRST CHOICE HERE")
        lblAnswer = Label(self, text = 'Choice 2', font=('MS', 8,'bold'))
        lblAnswer.grid(row=17, column= 4, rowspan=2)
        #rename this
        self.varCB2 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB2)
        CB1.grid(row=17, column=5, columnspan=1, sticky=W)
        self.Answer2 = Text(self, height=1,width=40)
        self.Answer2.grid(row=20, column=2,columnspan=5, sticky=E)
        self.Answer2.insert(END, "INPUT SECOND CHOICE HERE")
        lblAnswer = Label(self, text = 'Choice 3', font=('MS', 8,'bold'))
        lblAnswer.grid(row=21, column= 4, rowspan=2)
        #rename this
        self.varCB3 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB3)
        CB1.grid(row=21, column=5, columnspan=1, sticky=W)
        self.Answer3 = Text(self, height=1,width=40)
        self.Answer3.grid(row=24, column=2,columnspan=5, sticky=E)
        self.Answer3.insert(END, "INPUT THIRD CHOICE HERE")
        lblAnswer = Label(self, text = 'Choice 4', font=('MS', 8,'bold'))
        lblAnswer.grid(row=25, column= 4, rowspan=2)
        #rename this
        self.varCB4 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB4)
        CB1.grid(row=25, column=5, columnspan=1, sticky=W)
        self.Answer4 = Text(self, height=1,width=40)
        self.Answer4.grid(row=28, column=2,columnspan=5, sticky=E)
        self.Answer4.insert(END, "INPUT FOURTH CHOICE HERE")

    def createButtons(self):
        butSave = Button(self, text='Save',font=('MS', 8,'bold'))
        butSave['command']=self.saveTest
        butSave.grid(row=30, column=2, columnspan=2)
    def saveTest(self):
        with open('Test1.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([self.Question.get("1.0", "end-1c"),self.Answer1.get("1.0","end-1c"),
                             self.Answer2.get("1.0","end-1c"),self.Answer3.get("1.0","end-1c"),self.Answer4.get("1.0","end-1c")])
    def clearResponse(self):
       self.Question.delete("1.0", END)
       self.Answer1.delete("1.0", END)
       self.Answer2.delete("1.0", END)
       self.Answer3.delete("1.0", END)
       self.Answer4.delete("1.0", END)
        
    
#Main
root = Tk()
root.title("Create Test")
app = Create_Test(root)
root.mainloop()


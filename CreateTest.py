from tkinter import *
from tkinter import messagebox
import csv
questionNumber = 1
create_file = 0
saved_questions=[]
filename=str()
#def createTest():

class Create_Test(Frame):
# GUI Setup
    def __init__ (self, master, filename):
# Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.filename = filename
        self.grid()
        self.createTest()
        self.createButtons()
    def createTest(self):
        global questionNumber
        global saved_questions
        lblQuestion = Label(self, text = 'Question ' + str(questionNumber), font=('MS', 8,'bold'))
        lblQuestion.grid(row=3, column= 4, rowspan=2)
        self.Question = Text(self, height=3,width=40)
        scroll = Scrollbar(self, command=self.Question.yview)
        self.Question.configure(yscrollcommand=scroll.set)
        self.Question.grid(row=12, column=2,columnspan=5, sticky=E)
        scroll.grid(row=12, column=7, sticky=W)
        lblAnswer = Label(self, text = 'Choice 1', font=('MS', 8,'bold'))
        lblAnswer.grid(row=13, column= 4, rowspan=2)
        #rename this
        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB1)
        CB1.grid(row=13, column=5, columnspan=1, sticky=W)
        self.Answer1 = Text(self, height=1,width=40)
        self.Answer1.grid(row=16, column=2,columnspan=5, sticky=E)
        lblAnswer = Label(self, text = 'Choice 2', font=('MS', 8,'bold'))
        lblAnswer.grid(row=17, column= 4, rowspan=2)
        #rename this
        self.varCB2 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB2)
        CB1.grid(row=17, column=5, columnspan=1, sticky=W)
        self.Answer2 = Text(self, height=1,width=40)
        self.Answer2.grid(row=20, column=2,columnspan=5, sticky=E)
        lblAnswer = Label(self, text = 'Choice 3', font=('MS', 8,'bold'))
        lblAnswer.grid(row=21, column= 4, rowspan=2)
        #rename this
        self.varCB3 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB3)
        CB1.grid(row=21, column=5, columnspan=1, sticky=W)
        self.Answer3 = Text(self, height=1,width=40)
        self.Answer3.grid(row=24, column=2,columnspan=5, sticky=E)
        lblAnswer = Label(self, text = 'Choice 4', font=('MS', 8,'bold'))
        lblAnswer.grid(row=25, column= 4, rowspan=2)
        #rename this
        self.varCB4 = IntVar()
        CB1 = Checkbutton(self, text="Correct Question", variable=self.varCB4)
        CB1.grid(row=25, column=5, columnspan=1, sticky=W)
        self.Answer4 = Text(self, height=1,width=40)
        self.Answer4.grid(row=28, column=2,columnspan=5, sticky=E)

        self.isQuestionSaved()

        #print(counter)
        #print(questionNumber)

    def isQuestionSaved(self):
        for number in saved_questions:
            print(number)
            if questionNumber == number:
                self.printTextBox(True)
                return
        self.printTextBox(False)
    
    def printTextBox(self, saved):
        if saved == True:
            with open(self.filename) as test:
                r = csv.reader(test)
                if questionNumber != 1:
                    for i in range(questionNumber - 1):
                        next(r)
                data = next(r)
                self.Question.insert(END, data[0])
                self.Answer1.insert(END, data[1])
                self.Answer2.insert(END, data[2])
                self.Answer3.insert(END, data[3])
                self.Answer4.insert(END, data[4])
        else:
            self.Question.insert(END, "INPUT QUESTION HERE")
            self.Answer1.insert(END, "INPUT FIRST CHOICE HERE")
            self.Answer2.insert(END, "INPUT SECOND CHOICE HERE")
            self.Answer3.insert(END, "INPUT THIRD CHOICE HERE")
            self.Answer4.insert(END, "INPUT FOURTH CHOICE HERE")


    def createButtons(self):
        butNextQuestion = Button(self, text='Next Question',font=('MS', 8,'bold'))
        butNextQuestion['command']=self.nextQuestion
        butNextQuestion.grid(row=30, column=4, columnspan=1)

        butPreviousQuestion = Button(self, text='Previous Question',font=('MS', 8,'bold'))
        butPreviousQuestion['command']=self.previousQuestion
        butPreviousQuestion.grid(row=30, column=2, columnspan=2)

        butSave = Button(self, text='Save',font=('MS', 8,'bold'))
        butSave['command']=self.saveQuestion
        butSave.grid(row=30, column=5, columnspan=2)

        butClear = Button(self, text='Clear',font=('MS', 8,'bold'))
        butClear['command']=self.clearResponse
        butClear.grid(row=30, column=7, columnspan=2)

        """butNextQuestion = Button(self, text='Next Question',font=('MS', 8,'bold'))
        butSave['command']=self.saveTest
        butSave.grid(row=30, column=6, columnspan=2)"""
        
    def nextQuestion(self):
        global questionNumber
        questionNumber += 1
        self.createTest()

    def previousQuestion(self):
        global questionNumber
        if questionNumber == 1:
            return
        questionNumber -= 1
        self.createTest()

    def saveQuestion(self):
        global questionNumber
        global create_file
        global saved_questions
        if create_file != 0:
            r = csv.reader(open(self.filename, 'r'))
            old = list(r)
            if questionNumber > len(old):
                with open(self.filename, mode='a') as csv_file:
                    csv_file.write(self.Question.get("1.0", "end-1c")+",")
                    csv_file.write(self.Answer1.get("1.0","end-1c")+",")
                    csv_file.write(self.Answer2.get("1.0","end-1c")+",")
                    csv_file.write(self.Answer3.get("1.0","end-1c")+",")
                    csv_file.write(self.Answer4.get("1.0","end-1c")+"\n")
                saved_questions.append(questionNumber)
            else:
                old[questionNumber-1][0] = (self.Question.get("1.0", "end-1c"))
                old[questionNumber-1][1] = (self.Answer1.get("1.0", "end-1c"))
                old[questionNumber-1][2] = (self.Answer2.get("1.0", "end-1c"))
                old[questionNumber-1][3] = (self.Answer3.get("1.0", "end-1c"))
                old[questionNumber-1][4] = (self.Answer4.get("1.0", "end-1c"))
                with open(self.filename, 'w') as writer:
                    for i in old:
                        length = 1
                        for x in i:
                            if length < len(i):
                                writer.write(x + ",")
                                length += 1
                            else:
                                writer.write(x)
                        writer.write("\n")
        else:
            with open(self.filename, mode='a') as csv_file:
                csv_file.write(self.Question.get("1.0", "end-1c")+",")
                csv_file.write(self.Answer1.get("1.0","end-1c")+",")
                csv_file.write(self.Answer2.get("1.0","end-1c")+",")
                csv_file.write(self.Answer3.get("1.0","end-1c")+",")
                csv_file.write(self.Answer4.get("1.0","end-1c")+"\n")
            saved_questions.append(questionNumber)
            create_file += 1


    def clearResponse(self):
       self.Question.delete("1.0", END)
       self.Answer1.delete("1.0", END)
       self.Answer2.delete("1.0", END)
       self.Answer3.delete("1.0", END)
       self.Answer4.delete("1.0", END)
        
    def editTest(self, testName):
    #    with open(testName+'csv') as csv_file:
        pass


#Main
"""
root = Tk()
root.title("Create Test")
app = Create_Test(root)
root.mainloop()
"""

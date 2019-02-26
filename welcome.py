from tkinter import *
from tkinter import messagebox
import csv
import login
import CreateTest
#Note for later self: check if a test name with the same name exists when creating a test. Maybe also add a timer so it gets deleted automatically
class Welcome(Frame):
# GUI Setup
    def __init__ (self, master):
# Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.grid()
        self.overView()
        self.createButtons()
    def overView(self):
        lblQuestion = Label(self, text = 'WELCOME '+login.student_name, font=('MS', 8,'bold'))
        lblQuestion.grid(row=0, column= 4, rowspan=2)

        # Create widgets to select a module from a list
        string = ""
        if login.is_teacher:
            string = "Modules you can create an assesment in"
        else:
            string = "Modules you may have assesments in"
        lblModules = Label(self, text=string, font=('MS', 8,'bold'))
        lblModules.grid(row=2, column=0, columnspan=2, sticky=NE)
        
        self.listProg = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)
        self.listProg.grid(row=3, column=0, columnspan=2, sticky=NE)
        scroll.grid(row=3, column=7, sticky=W)
        modules_list = self.retrieveModules()
        for module in modules_list:
            self.listProg.insert(END, module)
            self.listProg.selection_set(END)

        self.listTest = Listbox(self, height= 3)
        scroll = Scrollbar(self, command= self.listTest.yview)
        self.listTest.configure(yscrollcommand=scroll.set)
        self.listTest.grid(row=7, column=0, columnspan=2, sticky=NE)
        scroll.grid(row=7, column=7, sticky=W)
        
    def retrieveModules(self):
        modules_list = []
        with open('user_modules.csv') as csvfile:
            rdr = csv.reader(csvfile)
            for row in rdr:
                if row[0] == login.userID:
                    for i in range(1,6):
                        if row[i]!= "":
                            modules_list.append(row[i])
        return modules_list
    def retrieveTests(self,module):
        test_list = []
        with open('tests_overview.csv') as csvfile:
            rdr = csv.reader(csvfile)
            for row in rdr:
                if row[0] == module:#Might need to add in the fact that a test gets taken
                    test_list.append(row[1])
        return test_list
    def createButtons(self):
        butSubmit = Button(self, text='Check for Tests',font=('MS', 8,'bold'))
        butSubmit['command']=self.checkTest #Note: no () after the method
        butSubmit.grid(row=4, column=0, columnspan=2)
        
        butSubmit = Button(self, text='Take TEST!',font=('MS', 8,'bold'))#rename me to thing depending on whether or not you are a teacher
        butSubmit['command']=self.takeTest
        butSubmit.grid(row=8, column=0, columnspan=2)
    def checkTest(self):
        #get value of selected module
        if self.listProg.curselection() != ():#Check if the user has selected something
            index = self.listProg.curselection()[0]
            strModule = str(self.listProg.get(index))
            #retrieve tests for that module
            test_list = self.retrieveTests(strModule)
            self.listTest.delete(0,END)
            for test in test_list:
                self.listTest.insert(END, test)
                self.listTest.selection_set(END)
        else:
            messagebox.showwarning("ERROR","Please select a module")
    def takeTest(self):
        CreateTest.createTest()
#Main
if login.userID != "":
    root = Tk()
    root.title("HOME "+ str(login.userID))
    app = Welcome(root)
    root.mainloop()

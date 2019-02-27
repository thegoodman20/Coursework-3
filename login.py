from tkinter import *
#from Response import Response
from tkinter import messagebox
import csv
#initilize variables needed later in the application
userID = ""
#read the courses the student is enrolled in
courses = []
is_teacher = False
student_name = ""
class Questionnaire(Frame):
# GUI Setup
    def __init__ (self, master):
# Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.grid()
        self.createLogin()
        self.createButtons()
    def createLogin(self):
        self.entUsername = Entry(self)
        self.entUsername.grid(row=0, column=4, columnspan=2, sticky=E)
        self.entPassword = Entry(self, show='*')
        self.entPassword.grid(row=2, column=4, columnspan=2, sticky=E)
        
        lblCmnt = Label(self, text='Username', font=('MS', 8,'bold'))
        lblCmnt.grid(row=0, column = 0,rowspan = 2, sticky = E)
        lblCmnt = Label(self, text='Password',font=('MS', 8,'bold'))
        lblCmnt.grid(row=2, column = 0)
    def createButtons(self):
        butSubmit = Button(self, text='Log-in',font=('MS', 8,'bold'))
        butSubmit['command']=self.Login #Note: no () after the method
        butSubmit.grid(row=16, column=2, columnspan=2)
        butClear = Button(self, text='Clear',font=('MS', 8,'bold'))
        butClear['command']=self.clearResponse
        butClear.grid(row=16, column=4, columnspan=2)
    def clearResponse(self):
        self.entUsername.delete(0, END)
        self.entPassword.delete(0, END)
    def Login(self):
        dontprint= 0
        uname = self.entUsername.get()
        pword = self.entPassword.get()
        with open('users.csv') as csvfile:
            rdr = csv.reader(csvfile)
            for row in rdr:
                if row[0] == uname and row[1] == pword:
                    global userID
                    global student_name
                    global is_teacher
                    userID = uname
                    student_name = row[3]
                    if row[2] == "student":
                        is_teacher = False
                    else:
                        is_teacher = True
                    root.destroy()#close the login page
                    dontprint = 1
            if dontprint == 0:
                print("LOGIN FAILED")
                self.clearResponse()
    
#Main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()

from tkinter import *
import csv

userID = str()


isTeacher = False
name = str()

class LogIn(Frame):
	"""docstring for LogIn"""
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createLogin()


	def createLogin(self):
		butSubmit = Button(self, text='Log-in',font=('MS', 8,'bold'), command = self.validateUser)
		butSubmit.grid(row=16, column=2, columnspan=2)
		butClear = Button(self, text='Clear',font=('MS', 8,'bold'), command = self.clearResponse)
		butClear.grid(row=16, column=4, columnspan=2)
		self.entuserID = Entry(self)
		self.entuserID.grid(row=0, column=4, columnspan=2, sticky=E)
		self.entPassword = Entry(self, show='*')
		self.entPassword.grid(row=2, column=4, columnspan=2, sticky=E)
		lblCmnt = Label(self, text='userID', font=('MS', 8,'bold'))
		lblCmnt.grid(row=0, column = 0,rowspan = 2, sticky = E)
		lblCmnt = Label(self, text='Password',font=('MS', 8,'bold'))
		lblCmnt.grid(row=2, column = 0)

	def clearResponse(self):
		self.entuserID.delete(0, END)
		self.entPassword.delete(0, END)

	def validateUser(self):
		failed = 1
		global userID
		userID = self.entuserID.get().upper()
		#print(userID)
		password = self.entPassword.get()
		#print(len(password) * '*')
		with open('users.csv') as csvfile:
			rdr = csv.reader(csvfile)
			for row in rdr:
				#print(row[1] == userID)
				#print(row)
				if row[0] == userID and row[1] == password:
					failed = 0
					global name
					name = row[3]
					if row[2] == 't':
						global isTeacher
						isTeacher = True
					print('Welcome')
					root.destroy()
			if failed == 1:	
				print("LOGIN FAILED")
				self.clearResponse()


#log = Toplevel()
root = Tk()
app = LogIn(root)
root.title('Log In')
root.mainloop()
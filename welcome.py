from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import login
import csv

class createMenu(Frame):
	"""docstring for menu"""
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.view()
		self.createButtons()

	def view(self):
		lblQuestion = Label(self, text = 'WELCOME '+login.name+"!", font=('MS', 8,'bold'))
		lblQuestion.grid(row=0, column= 4, rowspan=2)
		string = ""
		if login.isTeacher:
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

	def createTest(self):
		if self.listProg.curselection() != ():
			index = self.listProg.curselection()[0]
			strModule = str(self.listProg.get(index))
			print(strModule)
			name = login.name
			testName = simpledialog.askstring("Input", "Enter test name")
			if testName: #if testName isn't None or isn't an empty str
				print('Teacher: {0:20}Test Name: {1:10}'.format(name, testName))
				import Test
				t1 = Toplevel()
				t1.title("Test")
				Test.test_file(t1, testName, strModule, name)
			else:
				messagebox.showwarning("ERROR", "You must provide a test name")

	def checkTest(self):
		""" This function appends the tests available for a give 
				module to the Listbox listTest
		"""

		if self.listProg.curselection() != ():#Check if the user has selected something
			index = self.listProg.curselection()[0]
			strModule = str(self.listProg.get(index))
			#retrieve tests for that module
			test_list = self.retrieveTests(strModule)
		# i.e. if retrieveTests doesn't return -1
			if test_list != -1:
				self.listTest.delete(0,END)
				for test in test_list:
					self.listTest.insert(END, test)
					self.listTest.selection_set(END)
			else:
				#clear list box and show message
				self.listTest.delete(0,END)
				messagebox.showwarning("Note!","There are no tests for that module. ")
		else:
			messagebox.showwarning("ERROR","Please select a module")

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

	def retrieveTests(self, module):

		test_list = []
		with open('tests_overview.csv') as csvfile:
			rdr = csv.reader(csvfile)
			for row in rdr:
				if row[0] == module:#Might need to add in the fact that a test gets taken
					test_list.append(row[1])
		if len(test_list) == 0:
            # rather than return empty list, return -1
			return -1
		else:
			return test_list
		
	def createButtons(self):

		butCheck = Button(self, text='Check for Tests',font=('MS', 8,'bold'), command=self.checkTest)
		butCheck.grid(row=4, column=0, columnspan=2)
		if login.isTeacher:
			butCreate = Button(self, text='Create TEST!',font=('MS', 8,'bold'), command=self.createTest)
			butCreate.grid(row=8, column=0, columnspan=2)
			butEdit = Button(self, text='Edit Test', font=('MS', 8,'bold'), command=self.editTest)
			butEdit.grid(row = 8, column = 3, columnspan=2)
		else:
			butTake = Button(self, text='Take TEST!',font=('MS', 8,'bold'), command = self.takeTest)#rename me to thing depending on whether or not you are a teacher
			butTake.grid(row=8, column=0, columnspan=2)

	def editTest(self):
		import CreateTest
		t1 = Toplevel()
		t1.title("Test")
		if self.listTest.curselection() != ():
			index = self.listTest.curselection()[0]
			testfile = str(self.listTest.get(index))
			edit = CreateTest.Create_Test(t1, testfile+'.csv')
		

	def takeTest(self):
		pass

#main

print(login.userID)
print(login.name)
print("Teacher:", login.isTeacher)

if login.userID:
	root = Tk()
	root.title('Menu')
	app = createMenu(root)
	root.mainloop()
	

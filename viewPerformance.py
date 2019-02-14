from tkinter import *
import csv

""" The lecturer can view student performance on summative assessments. 
	For example; summary of marks for all students, performance for a 
	specific student. """

class viewPerformance(Frame):

	def __init__(self, master):
		# Initialise viewPerformance class

		Frame.__init__(self, master)
		self.grid()
		self.chooseStudent()

	def chooseStudent(self):
		lblStudent = Label(self, text = 'View a student\'s results', font = ('MS', 8,'bold'))
		lblStudent.grid(row = 0, column = 0, columnspan = 2, sticky=NE)



root = Tk()
root.title("Cohort Results")
app = viewPerformance(root)
root.mainloop()
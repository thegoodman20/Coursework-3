from tkinter import *

class assessment(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.text()
        self.buttonPlace()

    def init_window(self):

        self.master.title("Question")
        self.grid()
        self.entName = Entry(self)
        self.entName.grid(column=2,row=2,padx =10, pady= 10)

    def client_exit(self):
        print("Hi")

    def text(self):
        text = Label(self, text="Question number place holder",font="bold")
        text.grid(row=0,column=2,pady=5)
        text2 = Label(self, text="Question content place holder")
        text2.grid(row=1,column=2,pady=2)

    def buttonPlace(self):
        nextButton = Button(self, text="Next", command=self.client_exit)
        nextButton.grid(column = 3,row = 3)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.grid(column=1,row=3)


root = Tk()
app = assessment(root)
root.mainloop()

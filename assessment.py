from tkinter import *

class assessment(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Question")

        self.grid(padx = 100, pady = 100)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.grid(column = 0,row = 0)

    def client_exit(self):
        print("Hi")


root = Tk()
app = assessment(root)
root.mainloop()

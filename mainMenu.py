import tkinter as tk
import os

class mainMenu(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.Prompt = tk.Label(self,text="Please Select an Option")
        self.Prompt.grid()
        self.inputButton = tk.Button(self, text = 'Input', command = self.inputEvent)
        self.queryButton = tk.Button(self,text = 'Query',command = self.queryEvent)
        self.inputButton.grid()
        self.queryButton.grid()

    def inputEvent(self):
        os.system(os.getcwd() + '/classRecordsMongo.py')

    def queryEvent(self):
        return

app = mainMenu()
app.master.title('Main Menu')
app.mainloop()
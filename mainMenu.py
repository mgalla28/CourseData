import tkinter as tk
import os
import subprocess
import sys
class mainMenu(tk.Tk):
    def __init__(self,master=None):
        tk.Tk.__init__(self,master)
        subprocess.Popen('C:/\"Program Files\"/MongoDB/Server/4.0/bin/mongod.exe',shell=True)
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
        subprocess.call(os.getcwd() + '/classRecordsMongo.py')
        self.destroy()

    def queryEvent(self):
        self.destroy()
        sys.exit(0)

app = mainMenu()
app.title('Main Menu')
app.mainloop()
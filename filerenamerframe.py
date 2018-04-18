"""
File filerenamerframe.
Defines class FileRenamerFrame.
"""
# Cem Yesilyurt
# 4/3/18
# Python 3.6.2

from tkinter import Frame, Label, Entry, Button

class FileRenamerFrame(Frame):
    """
    One object of this class is one frame for the File Renamer program.
    """
    
    def __init__(self, controller):
        Frame.__init__(self)        
        self.grid()        
        self.controller = controller
        
        # Title Label
        self.titleLabel = Label(master=self, height=2, width=54)
        self.titleLabel["text"] = "Description: This program renames files by" \
            + " their dates.\nThe format after renaming is: " \
            + " Prefix_fileNumber_YYYY_MM_DD.ext"
        self.titleLabel.grid(row=0,column=0,columnspan=2)                                                                
        
        # Prefix Entry Label
        self.prefixEntryLabel = Label(master=self, height=3, width=54)
        self.prefixEntryLabel["text"] = "Enter the prefix you would" \
            + " like each file to start with:"
        self.prefixEntryLabel.grid(row=1,column=0,columnspan=2)        
        
        # Prefix Entry
        self.prefixEntry = Entry(master=self, width = 10)        
        self.prefixEntry.grid(row=2,column=0,columnspan=2)        
        
        # File Number Label
        self.fileNumberLabel = Label(master=self, height=3, width=54)
        self.fileNumberLabel["text"] = "(The file numbers are generated automatically.)"
        self.fileNumberLabel.grid(row=3,column=0,columnspan=2)
        
        # Path Entry Label
        self.pathEntryLabel = Label(master=self, height=3, width=54)
        self.pathEntryLabel["text"] = "Enter the path to the folder where the files" \
            + " are located:"
        self.pathEntryLabel.grid(row=4,column=0,columnspan=2)
        
        # Path Entry
        self.pathEntry = Entry(master=self, width = 54)        
        self.pathEntry.grid(row=5,column=0,columnspan=2)        
        
        # Empty Line Label 2
        self.emptyLineLabel2 = Label(master=self, width=54)
        self.emptyLineLabel2.grid(row=6,column=0,columnspan=2)        
        
        # Run Button
        self.runButton = Button(master=self, text="Run")       
        self.runButton["command"] = self.controller.runButtonPressed
        self.runButton.grid(row=7,column=0)    
        
        # Quit Button
        self.quitButton = Button(master=self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.grid(row=7,column=1)      

        # Empty Line Label 3
        self.emptyLineLabel3 = Label(master=self, width=54)
        self.emptyLineLabel3.grid(row=8,column=0,columnspan=2)        
'''
if __name__ == "__main__":
    root = tkinter.Tk()
    f = PhotoRenamerFrame()
    f.mainloop()
    root.destroy()
'''        
        

        
        
        
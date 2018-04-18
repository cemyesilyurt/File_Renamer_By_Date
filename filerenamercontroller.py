"""
File filerenamercontroller.
Defines class FileRenamerController.
"""
# Cem Yesilyurt
# 4/3/18
# Python 3.6.2

from tkinter import Tk, Toplevel, Label, Button
import filerenamerscript     # the MODEL
import filerenamerframe      # the VIEW

class FileRenamerController:
    """
    One object of this class is one controller for the Photo Renamer program.
    """
    
    def __init__(self):    
        root = Tk()
        root.title('File Renamer by Date')
        # model object not needed since model is a script with run function
        self.view = filerenamerframe.FileRenamerFrame(controller=self)
        self.view.mainloop()
        root.destroy()
    
    def runButtonPressed(self):
        """
        Event handler for "run" button in frame.
        """
        mypath = self.view.pathEntry.get()
        myprefix = self.view.prefixEntry.get()
        flag = filerenamerscript.runOperation(mypath, myprefix)
        if flag >= 1: 
            msg = "File name conversion for " + str(flag) \
                + " files successfully completed!"
        elif flag == -1:
            msg = "Path entered is invalid."
        elif flag == -2:
            msg = "Prefix cannot contain any of the following characters:\n" \
                + "/ \\ : * ? \" < > |"
        elif flag == -3:
            msg = "No files are in this directory.\n" \
                + "Sub-directories are not counted."
        elif flag.endswith('could not be copied'):
            msg = flag
        else:
            msg = 'Unknown error.'
            
        self.displayMessageBox(msg)
                
        
    def displayMessageBox(self, msg):
        """
        Displays message in top level box.
        """
        messageBox = Toplevel()
        mlabel = Label(master = messageBox, text = msg, height=2, width=54)
        mlabel.pack()            
        button = Button(master = messageBox, text = 'Ok')        
        button.pack()
        button['command'] = messageBox.destroy    
         
         
if __name__ == "__main__":        
    c = FileRenamerController()

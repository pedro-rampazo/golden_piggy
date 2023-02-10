from tkinter import *
from entry_page import *


class App:
    def __init__(self):
        self.root = Tk()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.width, self.height))
        EntryPage(self.root, self.width, self.height)
        self.root.mainloop()


if __name__ == "__main__":
    App()

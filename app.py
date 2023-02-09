from tkinter import *
from entry_page import *


class App:
    def __init__(self):
        self.root = Tk()
        EntryPage(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    App()

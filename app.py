from tkinter import *
from entry_page import *
from competition_page import *


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Golden Piggy')
        EntryPage(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    App()

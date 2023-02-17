from tkinter import *


class MainWindow:
    def __init__(self, master):
        self.master = master

        self.mainframe = Frame(
            self.master,
            width=self.master.winfo_screenwidth(),
            height=self.master.winfo_screenheight(),
            background='red'
        )
        self.mainframe.grid(
            column=1,
            row=1
        )
        self.mainframe.grid_propagate(False)
        self.mainframe.columnconfigure(1, weight=2)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.columnconfigure(3, weight=1)
        self.mainframe.columnconfigure(4, weight=2)

        self.button1 = Button(
            self.mainframe,
            text='Button 1'
        )
        self.button1.grid(
            column=1,
            row=1,
            sticky=EW
        )

        self.button2 = Button(
            self.mainframe,
            text='Button 2'
        )
        self.button2.grid(
            column=2,
            row=1,
            sticky=EW
        )

        self.button3 = Button(
            self.mainframe,
            text='Button 3'
        )
        self.button3.grid(
            column=3,
            row=1,
            sticky=EW
        )

        self.button4 = Button(
            self.mainframe,
            text='Button 4'
        )
        self.button4.grid(
            column=4,
            row=1,
            sticky=EW
        )


if __name__ == '__main__':
    root = Tk()
    MainWindow(root)
    root.mainloop()

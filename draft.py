from tkinter import *


class PageTwo:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(root, width=500, height=500, background='dark green')
        self.frame.pack()

        label = Label(self.frame, text='Page Two', font=('Roboto Slab', 30), background='dark green', foreground='white')
        label.grid(column=1, row=1, padx=20, pady=20)

        button = Button(self.frame, text='Home Page', command=self.change_frame)
        button.grid(column=1, row=2, padx=20, pady=20)

    def change_frame(self):
        self.frame.pack_forget()
        MainWindow(self.master)


class MainWindow:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(root, width=500, height=500, background='dark blue')
        self.frame.pack()

        self.label = Label(self.frame, text='Home Page', font=('Roboto Slab', 30), background='dark blue', foreground='white')
        self.label.grid(column=1, row=1, padx=20, pady=20)

        self.button = Button(self.frame, text='Page 2', command=self.change_frame)
        self.button.grid(column=1, row=2, padx=20, pady=20)

    def change_frame(self):
        self.frame.pack_forget()
        PageTwo(self.master)


if __name__ == '__main__':
    root = Tk()
    MainWindow(root)
    root.mainloop()

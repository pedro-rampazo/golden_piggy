import tkinter
from tkinter import *


def change_page(frame, _class, parent):
    frame.grid_forget()
    _class(parent)


def background_frame(parent, background):
    background = Frame(
        parent,
        background=background,
        width=parent.winfo_screenwidth(),
        height=parent.winfo_screenheight()
    )
    background.grid(
        column=1,
        row=1
    )
    return background


def label_style1(label):
    label['font'] = ('Roboto Slab', 24)
    label['background'] = '#063D25'
    label['foreground'] = '#F5F4F3'


def button_style1(button):
    button['font'] = ('Roboto Slab', 18)
    button['background'] = '#F5F4F3'
    button['foreground'] = '#063D25'
    button['relief'] = FLAT
    button['activebackground'] = '#00F084'
    button['activeforeground'] = '#063D25'


def button_green_style(parent, text, column, row, paddx, paddy, sticky):
    button = Button(
        parent,
        text=text,
        font=('Roboto Slab', 18),
        background='#00F084',
        foreground='#063D25',
        relief=FLAT,
        activebackground='#006437',
        activeforeground='#F5F4F3'
    )
    button.grid(
        column=column,
        row=row,
        padx=paddx,
        pady=paddy,
        sticky=sticky
    )
    return button


def button_style(button):
    button['font'] = ('Roboto Slab', 18)
    button['background'] = '#00F084'
    button['foreground'] = '#063D25'
    button['relief'] = FLAT
    button['activebackground'] = '#006437'
    button['activeforeground'] = '#F5F4F3'


def listbox_style1(parent, width, height, column, row, padx=0, pady=0):
    listbox = Listbox(
        parent,
        width=width,
        height=height,
        background='#F5F4F3',
        font=('Roboto Slab', 16),
        foreground='#363636',
        selectbackground='#00F084'
    )
    listbox.grid(
        column=column,
        row=row,
        padx=padx,
        pady=pady
    )
    return listbox

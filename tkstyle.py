import tkinter
from tkinter import *


def change_page(frame, _class, parent):
    frame.grid_forget()
    _class(parent)


# FRAME

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

# LABEL


def label_style1(label, size):
    label['font'] = ('Roboto Slab', size)
    label['background'] = '#063D25'
    label['foreground'] = '#F5F4F3'

# BUTTON


def button_style1(button, size):
    button['font'] = ('Roboto Slab', size)
    button['background'] = '#F5F4F3'
    button['foreground'] = '#063D25'
    button['relief'] = FLAT
    button['activebackground'] = '#00F084'
    button['activeforeground'] = '#063D25'


def button_green_style(button, size):
    button['font'] = ('Roboto Slab', size)
    button['background'] = '#00F084',
    button['foreground'] = '#063D25',
    button['relief'] = FLAT
    button['activebackground'] = '#006437'
    button['activeforeground'] = '#F5F4F3'


def button_red_style(button, size):
    button['font'] = ('Roboto Slab', size)
    button['background'] = '#B01900'
    button['foreground'] = '#F5F4F3'
    button['relief'] = FLAT
    button['activebackground'] = '#640E00'
    button['activeforeground'] = '#F5F4F3'


def button_yellow_style(button, size):
    button['font'] = ('Roboto Slab', size)
    button['background'] = '#F0AA18'
    button['foreground'] = '#A37108'
    button['relief'] = FLAT
    button['activebackground'] = '#A37108'
    button['activeforeground'] = '#755426'


def button_white_style(button, size):
    button['font'] = ('Roboto Slab', size)
    button['background'] = '#F5F4F3'
    button['foreground'] = '#363636'
    button['relief'] = FLAT
    button['activebackground'] = '#FFFFFF',
    button['activeforeground'] = '#363636'

# LISTBOX


def listbox_style1(listbox, size):
    listbox['background'] = '#F5F4F3'
    listbox['font'] = ('Roboto Slab', size)
    listbox['foreground'] = '#363636',
    listbox['selectbackground'] = '#00F084'

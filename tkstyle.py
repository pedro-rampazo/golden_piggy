from tkinter import *


def label_style1(parent, text, column, row, paddx=0, paddy=0):
    Label(
        parent,
        text=text,
        font=('Roboto Slab', 24),
        background='#063D25',
        foreground='#F5F4F3'
    ).grid(
        column=column,
        row=row,
        padx=paddx,
        pady=paddy
    )


def button_style1(parent, text, column, row, paddx=0, paddy=0):
    Button(
        parent,
        text=text,
        font=('Roboto Slab', 18),
        background='#F5F4F3',
        foreground='#063D25',
        relief=FLAT,
        activebackground='#00F084',
        activeforeground='#063D25'
    ).grid(
        column=column,
        row=row,
        padx=paddx,
        pady=paddy
    )

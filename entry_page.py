from tkinter import *

from tklib import get_image
from tkstyle import label_style1, button_style1


class EntryPage:
    def __init__(self, master, width, height):
        self.master = master
        self.master.title("Golden Piggy")

        self.mainframe = Frame(
            self.master,
            background='#063D25',
            width=width,
            height=height,
        )
        self.mainframe.grid(column=1, row=1)

        self.content_frame = Frame(
            self.mainframe,
            background='#063D25'
        )
        self.content_frame.grid(column=1, row=1)
        self.content_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.logo_image = get_image(
            self.content_frame,
            'images/icon_golden_piggy.png',
            250,
            250
        )
        self.logo_image.grid(
            column=1,
            row=1
        )
        self.logo_image['background'] = '#063D25'

        label_style1(self.content_frame, 'Golden Piggy', 1, 2)
        button_style1(self.content_frame, 'Start', 1, 3, 0, 20)

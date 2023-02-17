from tkinter import *

from tklib import get_image
from tkstyle import label_style1, button_style1, background_frame, change_page
from competition_page import *


class EntryPage(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        self.mainframe = background_frame(self.master, '#063D25')

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

        self.title = Label(
            self.content_frame,
            text='Golden Piggy'
        )
        self.title.grid(
            column=1,
            row=2
        )
        label_style1(self.title, 24)

        self.start_button = Button(
            self.content_frame,
            text='Start',
            command=lambda: change_page(self.mainframe, CompetitionPage, self.master)
        )
        self.start_button.grid(
            column=1,
            row=3,
            padx=0,
            pady=20
        )
        button_style1(self.start_button, 18)

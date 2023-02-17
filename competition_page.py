from tkinter import *

from tkstyle import *
from hunch_match_page import *


class CompetitionPage(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        self.mainframe = background_frame(self.master, '#063D25')
        self.mainframe.grid_propagate(0)

        self.title = Label(
            self.mainframe,
            text='Competitions'
        )
        self.title.grid(
            column=1,
            row=1,
            padx=20,
            pady=20
        )
        label_style1(self.title, 24)

        self.competition_list = Listbox(
            self.mainframe,
            width=30,
            height=10
        )
        self.competition_list.grid(
            column=1,
            row=2,
            padx=20
        )
        listbox_style1(self.competition_list, 16)
        for x in range(8):
            self.competition_list.insert(END, f'Competition {x}')

        self.ok_button = Button(
            self.mainframe,
            text='OK',
            width=10,
            command=lambda: change_page(self.mainframe, HunchMatchPage, self.master)
        )
        self.ok_button.grid(
            column=2,
            row=3,
            padx=30,
            pady=30
        )
        button_style1(self.ok_button, 18)

        self.new_button = Button(
            self.mainframe,
            text='New',
            width=10
        )
        self.new_button.grid(
            column=1,
            row=3,
            padx=20,
            pady=30,
            sticky=W
        )
        button_green_style(self.new_button, 18)

        self.remove_button = Button(
            self.mainframe,
            text='Remove',
            width=10
        )
        self.remove_button.grid(
            column=1,
            row=3,
            padx=20,
            pady=30,
            sticky=E
        )
        button_red_style(self.remove_button, 18)

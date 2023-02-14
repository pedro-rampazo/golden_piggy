from tkinter import *

from tkstyle import *


class CompetitionPage(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        self.mainframe = background_frame(self.master, '#063D25')
        self.mainframe.grid_propagate(0)

        label_style1(self.mainframe, 'Competitions', 1, 1, 20, 20)

        self.competition_list = listbox_style1(self.mainframe, 30, 10, 1, 2, 20)
        for x in range(8):
            self.competition_list.insert(END, f'Competition {x}')

        self.ok_button = button_style1(self.mainframe, 'OK', 2, 3, 30, 30)
        self.ok_button['width'] = 10

        self.new_button = button_green_style(self.mainframe, 'New', 1, 3, 20, 30, 'W')
        self.new_button['width'] = 10

        self.remove_button = Button(
            self.mainframe,
            text='Remove'
        )
        self.remove_button.grid(
            column=3,
            row=3,
            padx=30,
            pady=30
        )
        button_style(self.remove_button)

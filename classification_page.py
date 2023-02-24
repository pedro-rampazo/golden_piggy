from tkinter import *

from tklib import get_image
from tkstyle import *
from hunch_match_page import HunchMatchPage


class ClassificationPage(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        self.mainframe = background_frame(self.master, '#063D25')
        self.mainframe.grid_propagate(0)
        self.mainframe.columnconfigure(1, weight=1)

        self.title = Label(
            self.mainframe,
            text='Classification'
        )
        self.title.grid(
            column=1,
            row=1,
            padx=20,
            pady=20
        )
        label_style1(self.title, 24)

        self.hunch_match_button = Button(
            self.mainframe,
            text='Hunch-Match',
            command=lambda: change_page(self.mainframe, HunchMatchPage, self.master)
        )
        self.hunch_match_button.grid(
            column=1,
            row=1,
            padx=20,
            sticky=W
        )
        button_style1(self.hunch_match_button, 18)

        self.classification_frame = Frame(
            self.mainframe,
            background='#063D25'
        )
        self.classification_frame.grid(
            column=1,
            row=2,
            padx=20,
            sticky=NSEW
        )

        for x in range(1, 8):
            self.classification_frame.columnconfigure(x, weight=1)

        # HEADER CLASSIFICATION

        self.header_list = [
            [1, 'self.position_label', 'Position'],
            [2, 'self.status_label', 'Status'],
            [3, 'self.player_name_label', 'Player'],
            [4, 'self.player_score_label', 'Player Score'],
            [5, 'self.accurate_hunch_label', 'Accurante Hunch'],
            [6, 'self.hunch_quantity_label', 'Hunch Quantity'],
            [7, 'self.zero_points_label', 'Zero Points']
        ]

        for index, variable, text in self.header_list:
            variable = Label(
                self.classification_frame,
                text=text
            )
            variable.grid(
                column=index,
                row=1
            )
            label_style1(variable, 18)

        # CLASSIFICATION VALUES

        self.classification_value_list = [
            [1, 'self.position_value', '1º'],
            [3, 'self.player_name_value', 'User'],
            [4, 'self.player_score_value', '0 Pts.'],
            [5, 'self.accurate_hunch_value', '3'],
            [6, 'self.hunch_quantity_value', '7'],
            [7, 'self.zero_points_value', '5']
        ]

        for x in range(2, 10):
            for index, variable, text in self.classification_value_list:
                variable = Label(
                    self.classification_frame,
                    text=text
                )
                variable.grid(
                    column=index,
                    row=x,
                    pady=10
                )
                label_style1(variable, 14)

                self.status_icon = get_image(
                    self.classification_frame,
                    'images/icon_up.png',
                    32,
                    32
                )
                self.status_icon.grid(
                    column=2,
                    row=x
                )
                self.status_icon['background'] = '#063D25'

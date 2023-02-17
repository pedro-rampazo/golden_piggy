from tkinter import *

from tkstyle import *
from tklib import get_image


class HunchMatchPage(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        self.mainframe = background_frame(self.master, '#063D25')
        self.mainframe.grid_propagate(0)
        self.mainframe.columnconfigure(1, weight=2)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.columnconfigure(3, weight=1)
        self.mainframe.columnconfigure(4,  weight=2)

        self.title = Label(self.mainframe, text='Hunch-Match')
        self.title.grid(
            column=2,
            row=1,
            padx=20,
            pady=20,
            columnspan=2
        )
        label_style1(self.title, 24)

        self.competition_button = Button(self.mainframe, text='Competition')
        self.competition_button.grid(
            column=1,
            row=1,
            padx=20,
            pady=20,
            sticky=W
        )
        button_style1(self.competition_button, 18)

        self.classification_button = Button(self.mainframe, text='Classification')
        self.classification_button.grid(
            column=4,
            row=1,
            padx=20,
            pady=20,
            sticky=E
        )
        button_style1(self.classification_button, 18)

        # MATCH WIDGETS

        self.match_title = Label(self.mainframe, text='Matches:')
        self.match_title.grid(
            column=1,
            row=2,
            padx=20,
            sticky=W
        )
        label_style1(self.match_title, 18)

        self.match_button_frame = Frame(self.mainframe, background='#063D25')
        self.match_button_frame.grid(
            column=1,
            row=3,
            padx=20,
            sticky=EW,
            columnspan=2
        )
        self.match_button_frame.columnconfigure(1, weight=1)
        self.match_button_frame.columnconfigure(2, weight=1)
        self.match_button_frame.columnconfigure(3, weight=1)

        self.add_match_button = Button(self.match_button_frame, text='Add')
        self.add_match_button.grid(
            column=1,
            row=1,
            sticky=EW
        )
        button_green_style(self.add_match_button, 14)

        self.edit_match_button = Button(self.match_button_frame, text='Edit')
        self.edit_match_button.grid(
            column=2,
            row=1,
            padx=20,
            sticky=EW
        )
        button_yellow_style(self.edit_match_button, 14)

        self.remove_match_button = Button(self.match_button_frame, text='Remove')
        self.remove_match_button.grid(
            column=3,
            row=1,
            sticky=EW
        )
        button_red_style(self.remove_match_button, 14)

        self.match_listbox = Listbox(self.mainframe)
        self.match_listbox.grid(
            column=1,
            row=4,
            padx=20,
            pady=20,
            sticky=NSEW,
            columnspan=2
        )
        listbox_style1(self.match_listbox, 14)
        for x in range(8):
            self.match_listbox.insert(END, f'Home X Away')

        # MATCH VIEWER

        self.match_viewer = Frame(self.mainframe, background='#063D25')
        self.match_viewer.grid(
            column=1,
            row=5,
            padx=20,
            sticky=NSEW,
            columnspan=2
        )
        self.match_viewer.columnconfigure(1, weight=1)
        self.match_viewer.columnconfigure(2, weight=1)
        self.match_viewer.columnconfigure(3, weight=1)

        self.home_team_label = Label(self.match_viewer, text='Palmeiras')
        self.home_team_label.grid(
            column=1,
            row=1
        )
        label_style1(self.home_team_label, 12)

        self.away_team_label = Label(self.match_viewer, text='Grêmio')
        self.away_team_label.grid(
            column=3,
            row=1
        )
        label_style1(self.away_team_label, 12)

        self.home_team_emblem = get_image(self.match_viewer, 'embelms/palmeiras.png', 100, 100)
        self.home_team_emblem.grid(
            column=1,
            row=2
        )
        self.home_team_emblem['background'] = '#063D25'

        self.away_team_emblem = get_image(self.match_viewer, 'embelms/gremio.png', 100, 100)
        self.away_team_emblem.grid(
            column=3,
            row=2
        )
        self.away_team_emblem['background'] = '#063D25'

        self.result_label = Label(self.match_viewer, text='4 X 2')
        self.result_label.grid(
            column=2,
            row=2
        )
        label_style1(self.result_label, 24)

        self.date_label = Label(self.match_viewer, text='02/15/2023')
        self.date_label.grid(column=2, row=3)
        label_style1(self.date_label, 12)

        self.local_label = Label(self.match_viewer, text='Allianz Parque')
        self.local_label.grid(
            column=2,
            row=4
        )
        label_style1(self.local_label, 12)

        self.championship_label = Label(self.match_viewer, text='Campeonato Brasileiro')
        self.championship_label.grid(
            column=2,
            row=5
        )
        label_style1(self.championship_label, 12)

        # HUNCH WIDGETS

        self.hunch_title = Label(self.mainframe, text='Hunches:')
        self.hunch_title.grid(
            column=3,
            row=2,
            padx=20,
            sticky=W
        )
        label_style1(self.hunch_title, 18)

        self.hunch_button_frame = Frame(self.mainframe, background='#063D25')
        self.hunch_button_frame.grid(
            column=3,
            row=3,
            padx=20,
            sticky=EW,
            columnspan=2
        )
        self.hunch_button_frame.columnconfigure(1, weight=1)
        self.hunch_button_frame.columnconfigure(2, weight=1)
        self.hunch_button_frame.columnconfigure(3, weight=1)

        self.add_hunch_button = Button(self.hunch_button_frame, text='Add')
        self.add_hunch_button.grid(
            column=1,
            row=1,
            sticky=EW
        )
        button_green_style(self.add_hunch_button, 14)

        self.edit_hunch_button = Button(self.hunch_button_frame, text='Edit')
        self.edit_hunch_button.grid(
            column=2,
            row=1,
            padx=20,
            sticky=EW
        )
        button_yellow_style(self.edit_hunch_button, 14)

        self.remove_hunch_button = Button(self.hunch_button_frame, text='Remove')
        self.remove_hunch_button.grid(
            column=3,
            row=1,
            sticky=EW
        )
        button_red_style(self.remove_hunch_button, 14)

        self.hunch_listbox = Listbox(self.mainframe)
        self.hunch_listbox.grid(
            column=3,
            row=4,
            padx=20,
            pady=20,
            sticky=NSEW,
            columnspan=2
        )
        listbox_style1(self.hunch_listbox, 14)
        for x in range(8):
            self.hunch_listbox.insert(END, f'Hunch {x}')

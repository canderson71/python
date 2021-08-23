#******************************
#
# NAME      : tk_common.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/22/2021
# PURPOSE   : This file contains all the common database modules
#
#******************************

# Imports
from logging import log
from modal_form import app as mf
from tkinter import *
from tkinter import messagebox as msgbx

import tkinter as tk
import sys
import os

class tkcommon:
    def tk_btn(self, btn_text, function, cmd):
        btn = tk.Button(self, text=btn_text, command=cmd)
        btn.pack()
        return btn

    def tk_createTopMenu(self, menubar, menuLabel):
        menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label=menuLabel, menu=menu)
        return menu

    def disable_screenresize(self):
        # Disable screen resizing
        self.resizable(False, False)  # This code helps to disable windows from resizing

    def tk_geoemtry(self, window_height, window_width):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def tk_init(self):
        tkform = tk.Tk.__init__(self)

    def tk_label(self, label_text, font2use=("Arial Italic", 40)):
        label_widget = tk.Label(self, text=label_text, font=font2use, justify="left")
        return label_widget

    def tk_msgbxAskOkCancel(msg, level):
        bxtitle = level
        okCancel = msgbx.askokcancel(bxtitle.capitalize(), msg, default='cancel', icon=level)
        return okCancel

    def tk_title(self, appTitle, Version):
        spacing = ' ' * 20
        self.title('%s%s%s'%(appTitle,spacing, Version))
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)
        return self.menubar
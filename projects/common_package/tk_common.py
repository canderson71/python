#******************************
#
# NAME      : tk_common.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/22/2021
# PURPOSE   : This file contains all the Common database modules
#
#******************************

# Imports
from logging import log
from modal_form import app as mf
from tkinter import *
from tkinter import messagebox as msgbx
import tkinter.ttk as ttk

import tkinter as tk
import sys
import os

class TKCommon:
    def _disable_screenresize(self):
        # Disable screen resizing
        self.resizable(False, False)  # This code helps to disable windows from resizing

    def _tkbtn(self, btn_text, function, cmd):
        btn = ttk.Button(self, text=btn_text, command=cmd)
        btn.pack()
        return btn

    def _tkcreateTopMenu(self, menubar, menuLabel):
        menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label=menuLabel, menu=menu)
        return menu

    def _tkgeoemtry(self, window_height, window_width):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def _tkinit(self):
        tkform = tk.Tk.__init__(self)

    def _tklabel(self, label_text, font2use=("Arial Italic", 40)):
        label_widget = tk.Label(self, text=label_text, font=font2use, justify="left")
        return label_widget

    def _tkmsgbxAskOkCancel(msg, level):
        bxtitle = level
        okCancel = msgbx.askokcancel(bxtitle.capitalize(), msg, default='cancel', icon=level)
        return okCancel

    def _tktitle(self, appTitle, Version):
        spacing = ' ' * 20
        self.title('%s%s%s'%(appTitle,spacing, Version))
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)
        return self.menubar
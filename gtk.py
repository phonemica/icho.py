# Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# general functions
import uuid # new document IDs
from threading import Timer
import time

# custom functions and classes. should be UI-agnostic
from functions import * # general functions

global variables
language = set_language('muishaung')
entries = []
sorting = False

class IchoDict(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Icho Dictionary")

        self.lexicon = Gtk.Box()
        self.lexicon.set_border_width(10)
        self.add(self.lexicon)

        self.box = Gtk.Box(spacing=5)
        self.lexicon.add(self.box)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.box.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

win = IchoDict()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

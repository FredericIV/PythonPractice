#!/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ChessWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Chess")

        self.grid = Gtk.Grid.new()
        self.grid.set_baseline_row(8)
        self.grid.set_column_homogeneous(True)
        self.label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.grid.attach(self.button, 0, 0, 1, 1)
        self.grid.attach(self.label, 0, 1, 1, 1)
        self.add(self.grid)

    def on_button_clicked(self, widget):
        print("Hello World")


window = ChessWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
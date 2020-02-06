# Description: Set spaces between lines
# Authors: Hamad Al Marri <hamad.s.almarri@gmail.com>
# Copyright: Copyright (C) 2020 Hamad Al Marri
# Website: https://github.com/hamadmarri

from gi.repository import GObject, Gtk, Gedit

class LineSpacing(GObject.Object, Gedit.ViewActivatable):
	__gtype_name__ = "LineSpacing"
	view = GObject.property(type=Gedit.View)
	pixels = 4 # <<-- set this (default = 0, it can be negative)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		if self.view:
			self.view.set_pixels_below_lines(self.pixels)


	def do_deactivate(self):
		if self.view:
			self.view.set_pixels_below_lines(0)




        
        

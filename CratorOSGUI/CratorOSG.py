import gi
from gi.repository import Gtk
## add a new image
image_area = Gtk.Box()
image = Gtk.Image()
image.set_from_file('Crator2.png')
image_area.add(image)
image_area.show_all()
gi.require_version('Gtk', '3.0')
win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.add(image_area)
win.show_all()
Gtk.main()

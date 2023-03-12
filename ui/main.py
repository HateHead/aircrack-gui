import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk


class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layoutParent = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(layoutParent)

        self.headerBar = Adw.HeaderBar()

        self.viewSwitcher = Adw.ViewSwitcherBar()
        self.viewStack = Adw.ViewStack()

        self.viewStack.add()

        layoutParent.append(self.headerBar)
        layoutParent.append(self.viewSwitcher)
        layoutParent.append(self.viewStack)


class InterfacePage(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

import sys
import gi

# pylint: disable=wrong-import-position

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gio, GLib, Adw

# pylint: enable=wrong-import-position

from ui.window import MainWindow


class Application(Adw.Application):
    """Application entrypoint"""

    def __init__(self, **_kwargs):
        """App init"""

        super().__init__(
            application_id="com.cod3ddot.aircrack-gui",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )
        GLib.set_application_name("aircrack-gui")

    def do_activate(self):  # pylint: disable=arguments-differ
        """Runs on app start"""

        win = self.props.active_window  # pylint: disable=no-member
        if not win:
            win = MainWindow(application=self)

        win.present()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)

import asyncio
import pyrcrack
import gi

# pylint: disable=wrong-import-position

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk

# pylint: enable=wrong-import-position


async def scan_for_targets():
    """Scan for interfaces"""
    airmon = pyrcrack.AirmonNg()

    return [a["interface"] for a in await airmon.interfaces]  # type: ignore


@Gtk.Template(filename="data/ui/compiled/interface.ui")
class InterfacePage(Gtk.Box):
    """Interface Page"""

    __gtype_name__ = "InterfacePage"

    interfaces: list = []

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        interfaces = asyncio.run(scan_for_targets())
        print(interfaces)

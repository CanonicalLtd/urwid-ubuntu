""" Represents a Single Juju service UI widget
"""

from urwid import Text
from ubuntui.widgets.juju.unit import UnitWidget
import q


class ServiceWidget:
    def __init__(self, name, service):
        """ Init

        Params:
        machine: Juju Service Class
        """
        self.Name = Text(name)
        self.Icon = Text("")
        self.Units = []
        for n, unit in service['Units'].items():
            q(n)
            w = UnitWidget(n, unit)
            self.Units.append(w)

# -*- coding: utf-8 -*-
from taipy.gui import Gui, navigate
from pages.locations.atkins import atkins_md

city = ""

locations_md = """

Select a location to view graph

<|{city}|toggle|lov= Atkins; Baton Rouge|city|>
<|{city}|>

"""


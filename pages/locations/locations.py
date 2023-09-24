# -*- coding: utf-8 -*-
from taipy.gui import Gui, navigate
#from pages.locations.atkins import atkins_md
#from pages.locations.baton_rouge import baton_rouge_md
### {[('atkins_md', "Atkins"), ("baton_rouge_md", "Baton Rouge")]}
###  Atkins; Baton Rouge
city = ""
cityinfo = """placeholder"""

locations_md = """

<|{city}| toggle| lov = {[('atkins_md', "Atkins"), ("baton_rouge_md", "Baton Rouge")]}| on_action=on_menu|>

"""



baton_rouge_md = """

things will go here

"""




atkins_md = """
Image should go here

"""
def on_toggle(state):
    if state.city == "Atkins":
        state.cityinfo = atkins_md
        
def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)


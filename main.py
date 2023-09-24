from taipy.gui import Gui, navigate
from pages.about import about_md
from pages.locations.locations import *
from pages.locations.atkins import atkins_md
from pages.locations.baton_rouge import baton_rouge_md


# Definition of the page
# Add a navbar to switch from one page to the other
root_md = """

# HydrOracle: Flood Data Visualization 
<|navbar|>


"""
     
def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)
    

pages = {
    "/": root_md,
    "About": about_md,
    "Atkins": atkins_md,
    "Baton-rouge": baton_rouge_md
    
}
gui = Gui(pages=pages)


partial_atkins = gui.add_partial(atkins_md)

gui.run()
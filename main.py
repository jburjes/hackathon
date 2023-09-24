from taipy.gui import Gui, navigate
from pages.about import about_md
from pages.locations.locations import *
from pages.locations.atkins import atkins_md
from pages.locations.baton_rouge import baton_rouge_md
from pages.locations.belle_chase import *
from pages.locations.brooklyn_park import *
from pages.locations.chester import *
from pages.locations.clinton import *
from pages.locations.grand_rapids import *
from pages.locations.memphis import *
from pages.locations.royalton import *
from pages.locations.st_louis import *


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
    "Baton-rouge": baton_rouge_md,
    "Belle-Chase": belle_chase_md,
    "Brooklyn-Park": brooklyn_park_md,
    "Chester": chester_md,
    "Clinton": clinton_md,
    "Grand-Rapids": grand_rapids_md,
    "Memphis": memphis_md,
    "Royalton": royalton_md,
    "St-Louis": st_louis_md 
    
}
gui = Gui(pages=pages)


partial_atkins = gui.add_partial(atkins_md)

gui.run()
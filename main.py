from taipy.gui import Gui
from pages.about import about_md
from pages.locations.locations import locations_md


# Definition of the page
# Add a navbar to switch from one page to the other
root_md = """
<center>
# Flood Data Visualization </center>

<|navbar|>


"""

page2_md = """



"""

pages = {
    "/": root_md,
    "About": about_md,
    "Locations": locations_md
}
Gui(pages=pages).run()
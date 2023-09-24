__name__ == '__main__'
from taipy.gui import Gui
from pages.about import about_md
 

# Definition of the page
# Add a navbar to switch from one page to the other
root_md = """

# HydrOracle: Flood Data Visualization 
<|navbar|>


"""
import VarianceCalc
from load_data import load_data


file_pathAtkins=r"Atkins data.csv"
nums0= load_data(file_pathAtkins)
result0=(VarianceCalc.findSD(nums0))
data0 = {"Year":[x for x in result0.keys()], "Standard deviation of discharge":[y for y in result0.values()]}
atkins_md= """
<|{data0}|chart|x=Year|y=Standard deviation of discharge|>    
    
"""
file_pathbaton_rouge=r"Baton Rouge data.csv"
nums1= load_data(file_pathbaton_rouge)
result1=(VarianceCalc.findSD(nums1))
data1 = {"Year":[x for x in result1.keys()], "Standard deviation of discharge":[y for y in result1.values()]}
baton_rouge_md="""
<|{data1}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_belle_chase=r"Belle Chase data.csv"
nums2= load_data(file_path_belle_chase)
result2=(VarianceCalc.findSD(nums2))
data2 = {"Year":[x for x in result2.keys()], "Standard deviation of discharge":[y for y in result2.values()]}
belle_chase_md="""
<|{data2}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_brooklyn_park=r"Brooklyn park data.csv"
nums3= load_data(file_path_brooklyn_park)
result3=(VarianceCalc.findSD(nums3))
data3 = {"Year":[x for x in result3.keys()], "Standard deviation of discharge":[y for y in result3.values()]}
brooklyn_park_md="""
<|{data3}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_chester=r"Chester data.csv"
nums4= load_data(file_path_chester)
result4=(VarianceCalc.findSD(nums4))
data4 = {"Year":[x for x in result4.keys()], "Standard deviation of discharge":[y for y in result4.values()]}
chester_md="""
<|{data4}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_clinton=r"Clinton data.csv"
nums5= load_data(file_path_clinton)
result5=(VarianceCalc.findSD(nums5))
data5 = {"Year":[x for x in result5.keys()], "Standard deviation of discharge":[y for y in result5.values()]}
clinton_md="""
<|{data5}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_Grand_Rapids=r"Grand rapids data.csv"
nums6= load_data(file_path_Grand_Rapids)
result6=(VarianceCalc.findSD(nums6))
data6 = {"Year":[x for x in result6.keys()], "Standard deviation of discharge":[y for y in result6.values()]}
grand_rapids_md="""
<|{data6}|chart|x=Year|y=Standard deviation of discharge|>  
""" 
file_path_memphis=r"Memphis data.csv"
nums7= load_data(file_path_memphis)
result7=(VarianceCalc.findSD(nums7))
data7 = {"Year":[x for x in result7.keys()], "Standard deviation of discharge":[y for y in result7.values()]}
memphis_md="""
<|{data7}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_royalton=r"Royalton data.csv"
nums8= load_data(file_path_royalton)
result8=(VarianceCalc.findSD(nums8))
data8 = {"Year":[x for x in result8.keys()], "Standard deviation of discharge":[y for y in result8.values()]}
royalton_md="""
<|{data8}|chart|x=Year|y=Standard deviation of discharge|>  
"""
file_path_st_louis=r"St Louis data.csv"
nums9= load_data(file_path_st_louis)
result9=(VarianceCalc.findSD(nums9))
data9 = {"Year":[x for x in result9.keys()], "Standard deviation of discharge":[y for y in result9.values()]}
st_louis_md="""
<|{data9}|chart|x=Year|y=Standard deviation of discharge|>  
"""                 
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

gui.run()

if __name__ == '__main__':
    main()

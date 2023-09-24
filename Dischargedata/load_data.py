# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:55:22 2023

@author: jburj
"""

import csv
datalist = []
yearlist = []
def load_data(filepath):
    datalist = []
    yearlist = []
    with open(filepath, newline="\n") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data=row[0]
            data= data.split(",")
            data=[data[2], data[3]]
            yearlist.append(data)
            if "12/31" in data[0]:
                datalist.append(yearlist)
                yearlist=[]
                if "9/22/2023" in data[0]:
                    datalist.append(yearlist)
    return datalist

import statistics
import math
def findSD(datalist):
    SD={}
    vals=[]
    for i in range(len(datalist)):
        days=0
        for j in range(len(datalist[i])):
            days+=1
            try:
                vals.append(int(datalist[i][j][1]))
            except:
                continue
        SD[2013+i] = math.sqrt(statistics.variance(vals))
        vals=[]
    return SD

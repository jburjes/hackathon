def findVariance(datalist):
    Variances={}
    vals=[]
    for i in range(len(datalist)):
        days=0
        for j in range(len(datalist[i])):
            days+=1
            try:
                vals.append(int(datalist[i][j][1]))
            except:
                continue
        Variances[2013+i] = statistics.variance(vals)
        vals=[]
    return Variances

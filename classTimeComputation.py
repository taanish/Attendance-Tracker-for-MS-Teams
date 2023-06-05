import csv
import json
from textwrap import indent
import csvReformat

timeList, nameList, actionNameDict , timeNameDict = csvReformat.reformatCSV('demoAttendance.csv')

def computeJoinTimeList (timeList):
    joinTimeList= []
    for i in timeList:
        l= len(i)
        joinTime= 0
    
        for j in range (1, l):
            if (j%2==1):
                joinTime+= i[j] - i[j-1]
            
        joinTimeList.append(joinTime)

        
    tempNameTime = [{n:jTime} for n, jTime in zip(nameList,joinTimeList)]
    
    return tempNameTime






    





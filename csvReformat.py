import csv
import json

endTime = 800 #demo value for class endtime 

def timeStampProcessor(ts):
    date, time = ts.split(' ', 1)  #Seperates date and time from timeStamp variable
    half = time[-2:] #PM or AM
    time = time[:-2] #Time of day in 12Hr format

    hour, min, sec = time.split(':') #Seperates time variable into hour, min, and second

    hour, min, sec = int(hour), int(min), int(sec) 

    if half == 'PM': #Converts initialHour from 12Hr format to 24Hr format
        if hour < 12:
            hour = hour + 12 

    tempTime = (hour*60) + min
    return tempTime


def addEndTime (timeList, endTime):  #A) Ensures that every element in timeList is even    B) Every item in timeList ends with the time they left the class
    for i in timeList:
        l= len(i)

        if (l%2==1):
            i.append(endTime)
    
    return timeList


def removeDuplicateNames(nameList):
    uniqueNames = []
    for name in nameList:
        if name not in uniqueNames:
            uniqueNames.append(name)
    
    return uniqueNames



def reformatCSV (Attendance):
    actionData = {}
    timeData = {}
    nameList= [] 
    timeList= [] 
    with open (Attendance, 'r', encoding= 'utf-16') as f:
        reader = csv.reader(f, delimiter = '\t')

        next(reader)

        for row in reader:
            name= row[0]
            nameList.append(name)
            action= row[1]
            timeStamp= timeStampProcessor(row[2])

            if name in actionData:
                actionData[name].append(action)
                timeData[name].append(timeStamp)
            else:
                actionData[name]= [action]
                timeData[name]= [timeStamp]
    
    
    actionNameDict = [{name: actions} for name, actions in actionData.items()]
    timeNameDict= [{name: timeStamp} for name, timeStamp in timeData.items()]
    
    
    for dict in timeNameDict:
        for val in dict.values():
            timeList.append(val)
    
    timeList = addEndTime(timeList, endTime)
    nameList = removeDuplicateNames(nameList)


    return timeList, nameList, actionNameDict, timeNameDict


    
 
# timeList, nameList, actionNameDict , timeNameDict = reformatCSV("demoAttendance.csv")

# print(timeList)
# print(nameList)
# print(json.dumps(actionNameDict))
# print(json.dumps(timeNameDict))



    



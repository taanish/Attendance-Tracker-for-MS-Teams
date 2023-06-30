import csv
import json


def getClassTimings():

    print("You will now be prompted to enter the class start and end times. Your input needs to be in this format (12hr) --> HH:MM AM/PM \nHere's a sample valid input--> 08:20 AM")
    classStartTime = int(
        input("Enter the class start time in the format specified: "))
    classEndTime = int(
        input("Enter the class start time in the format specified: "))

    classStartTime = timeStampProcessor(classStartTime)
    classEndTime = timeStampProcessor(classEndTime)
    classDuration = classEndTime - classStartTime

    return classStartTime, classEndTime, classDuration


# Note: implement functtionality for processing class starttime and class endtime in timeStampProcessor

def timeStampProcessor(ts):
    parts = ts.split(' ')
    if len(parts) == 3:  # Timestamp has a date part
        date, time, half = parts
    elif len(parts) == 2:  # Timestamp doesn't have a date part
        time, half = parts

    # Seperates time variable into hour, min, and second
    hour, min = time.split(':')

    hour, min = int(hour), int(min)

    if half == 'PM':  # Converts initialHour from 12Hr format to 24Hr format
        if hour < 12:
            hour = hour + 12

    tempTime = (hour*60) + min
    return tempTime


# A) Ensures that every list in timeList has even number of items    B) Every item in timeList ends with the time they left the class
def addEndTime(timeList, endTime):
    for i in timeList:
        l = len(i)

        if (l % 2 == 1):
            i.append(endTime)

    return timeList


def removeDuplicateNames(nameList):
    uniqueNames = []
    for name in nameList:
        if name not in uniqueNames:
            uniqueNames.append(name)

    return uniqueNames


def reformatCSV(Attendance):
    actionData = {}
    timeData = {}
    nameList = []
    timeList = []
    with open(Attendance, 'r', encoding='utf-16') as f:
        reader = csv.reader(f, delimiter='\t')

        next(reader)

        for row in reader:
            name = row[0]
            nameList.append(name)
            action = row[1]
            timeStamp = timeStampProcessor(row[2])

            if name in actionData:
                actionData[name].append(action)
                timeData[name].append(timeStamp)
            else:
                actionData[name] = [action]
                timeData[name] = [timeStamp]

    actionNameDict = [{name: actions} for name, actions in actionData.items()]
    timeNameDict = [{name: timeStamp} for name, timeStamp in timeData.items()]

    for dict in timeNameDict:
        for val in dict.values():
            timeList.append(val)

    timeList = addEndTime(timeList, classEndTime)
    nameList = removeDuplicateNames(nameList)

    return timeList, nameList, actionNameDict, timeNameDict

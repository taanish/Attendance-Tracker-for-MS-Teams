import csv

# Inputs class timings, computes class length


def getClassTimings():

    print("You will be prompted to enter the class start and end times. Your input needs to be in this format (12hr) --> HH:MM AM/PM \nHere's a sample valid input--> 08:20 AM")
    classStartTime = (
        input("Enter the class start time in the format specified: "))
    classEndTime = (
        input("Enter the class end time in the format specified: "))

    classStartTime = timeStampProcessor(classStartTime)
    classEndTime = timeStampProcessor(classEndTime)
    classDuration = classEndTime - classStartTime

    return classEndTime, classDuration


# Processes timestamps from getClassTimings() and from csvProcessor()
def timeStampProcessor(ts):
    parts = ts.split(' ')
    if len(parts) == 3:  # Timestamp has a date part
        date, time, half = parts
        time = time[:-3]
    elif len(parts) == 2:  # Timestamp doesn't have a date part
        time, half = parts

    hour, min = time.split(':')

    hour, min = int(hour), int(min)

    if half == 'PM':  # Converts initialHour from 12Hr format to 24Hr format.
        if hour < 12:
            hour = hour + 12

    tempTime = (hour*60) + min
    return tempTime


# Ensures that every list in timeList has even number of items and ends with the time they left the class.
def addEndTime(timeList, endTime):
    for i in timeList:
        l = len(i)

        if (l % 2 == 1):
            i.append(endTime)

    return timeList

# Removes duplicate names, returns a list of unique names.


def removeDuplicateNames(nameList):
    uniqueNames = []
    for name in nameList:
        if name not in uniqueNames:
            uniqueNames.append(name)

    return uniqueNames


# Generates timeList and nameList.
    # timeList contains timeStamps for each user action (joining or leaving).
    # nameList contains each unique name from the CSV File.
def csvProcessor(Attendance, classEndTime):
    timeData = {}
    nameList = []
    timeList = []
    with open(Attendance, 'r', encoding='utf-16') as f:
        reader = csv.reader(f, delimiter='\t')

        next(reader)

        for row in reader:
            name = row[0]
            nameList.append(name)
            timeStamp = timeStampProcessor(row[2])

            if name in timeData:
                timeData[name].append(timeStamp)
            else:
                timeData[name] = [timeStamp]

    timeNameDict = [{name: timeStamp} for name, timeStamp in timeData.items()]

    for dict in timeNameDict:
        for val in dict.values():
            timeList.append(val)

    timeList = addEndTime(timeList, classEndTime)
    nameList = removeDuplicateNames(nameList)

    return timeList, nameList

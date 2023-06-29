import csv
import json
from textwrap import indent
import csvReformat

timeList, nameList, actionNameDict, timeNameDict = csvReformat.reformatCSV(
    'demoAttendance.csv')


# Takes raw timeList with all timestamps and parses it to extract total joinTimes and returns it via joinTimeList
def computeJoinTimeList(timeList):
    joinTimeList = []
    for i in timeList:
        l = len(i)
        joinTime = 0

        for j in range(1, l):
            if (j % 2 == 1):
                joinTime += i[j] - i[j-1]

        joinTimeList.append(joinTime)

    return joinTimeList


# Combines nameList (unique) and joinTimeList to generate a final attendance report
def attendanceStatus():
    attendanceReport = []

    joinTimeList = computeJoinTimeList(timeList)
    timeThreshold = int(input("Out of the %s mins of class time, how many minutes should a student attend in order to get a present mark?" % (
        csvReformat.classDuration)))

    for i in range(len(joinTimeList)):
        if (joinTimeList[i] >= timeThreshold):
            attendanceReport.append([nameList[i], 'Yes'])
        else:
            attendanceReport.append([nameList[i], 'No'])

    return attendanceReport


print(attendanceStatus())

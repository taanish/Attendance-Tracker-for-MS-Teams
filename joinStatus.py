# Takes raw timeList with all timestamps and parses it to extract total joinTimes and returns it via joinTimeList
def computeTotalJoinTimeList(timeList):
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
# Uses timeList, nameList, classDuration
def attendanceReportGenerator(timeList, nameList, classDuration):
    attendanceReport = []

    joinTimeList = computeTotalJoinTimeList(timeList)
    timeThreshold = int(input("Out of the %s mins of class time, how many minutes should a student attend in order to get a present mark?" % (
        classDuration)))

    for i in range(len(joinTimeList)):
        if (joinTimeList[i] >= timeThreshold):
            attendanceReport.append([nameList[i], 'Present'])
        else:
            attendanceReport.append([nameList[i], 'Absent'])

    return attendanceReport

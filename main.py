import csvReformat
import joinStatus
import sheetsEditor


def main():
    # Input file name
    fileName = input(
        "Enter the Microsoft generated CSV File Name. Enter 'Default' to use the demoAttendance.csv file located in this dir. ")

    if (fileName == 'Default'):
        fileName = 'demoAttendance.csv'

    # Fetch class timings
    classEndTime, classDuration = csvReformat.getClassTimings()

    # Reformat the CSV
    timeList, nameList = csvReformat.csvProcessor(
        fileName, classEndTime)

    # Generate attendance report
    attendanceReport = joinStatus.attendanceReportGenerator(
        timeList, nameList, classDuration)

    # Update Google Sheets
    sheetsEditor.googleSheetsUpdater(attendanceReport)


if __name__ == "__main__":
    main()

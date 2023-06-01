import csv
def reformatCSV (Attendance.csv):
    data = {}
    with open (Attendance.csv, 'r') as f:
        reader = csv.reader(f)
    
    next(reader)

    for row in reader:
        name= row[0]
        action= row[1]
        timeStamp= row[2]

        if name in data:
            data[name].append(action)
        else:
            data[name]= action

    newData = [{name: actions} for name, actions in data.items()]
    return newData

    



import csv
import json
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



def reformatCSV (Attendance):
    actionData = {}
    timeData = {}
    with open (Attendance, 'r', encoding= 'utf-16') as f:
        reader = csv.reader(f, delimiter = '\t')

        next(reader)

        for row in reader:
            name= row[0]
            action= row[1]
            timeStamp= timeStampProcessor(row[2])

            if name in actionData:
                actionData[name].append(action)
                timeData[name].append(timeStamp)
            else:
                actionData[name]= [action]
                timeData[name]= [timeStamp]

    action = [{name: actions} for name, actions in actionData.items()]
    time= [{name: timeStamp} for name, timeStamp in timeData.items()]
    
    
    return action, time
 
tempAction , tempTime = reformatCSV("demoAttendance.csv")

print(json.dumps(tempAction, indent=4))
print(json.dumps(tempTime, indent=4))

    



import json
import os
files = os.listdir("employee_slots")
files.sort()
edicts = list()
for file in files:
    with open("employee_slots/"+file) as f:
        e_dict = dict()
        e_dict = json.load(f)
        edicts.append(e_dict)

enames = []
edates = []
eschedules = []
easlots = []

for emp_dict in edicts:
    emp_name = list(emp_dict.keys())[0]
    enames.append(emp_name)
    emp_date = list(emp_dict[emp_name].keys())[0]
    edates.append(emp_date)
    emp_schedule = emp_dict[emp_name][emp_date]
    eschedules.append(emp_schedule)

for i in range(len(enames)):
    avail = []
    avail.append(["9:00AM", "9:00AM"])
    for duration in eschedules[i]:
        se = duration.split(' -')
        if not(se[0] == se[1]):
            avail.append(se)
    avail.append(["5:00PM", "5:00PM"])
    easlots.append(avail)
f = open("output.txt", "a")
f.write("Available Slots :\n")
count = 0
for avail in easlots:
    for i in range(1, len(avail)):
        avail[i-1][1] = avail[i-1][1].replace(avail[i-1][1], avail[i][0])
        avail[i][0] = avail[i][0].replace(avail[i][0], avail[i][1])
    try:
        avail.remove(['5:00PM', '5:00PM'])
    except:
        print("")
    emp_available_slots_output = list()
    for slot in avail:
        if (slot[0] != slot[1]):
            string = str(slot).replace('\'', '')
            string.replace('[', '').replace(']', '')
            string.replace(', ', ' - ')
            string.replace('\"', '\'')
            emp_available_slots_output.append(string)
    f.write(enames[count])
    f.write(": ")
    f.write(str(emp_available_slots_output))
    f.write("\n")
    count += 1
f.close()

common = list()
flag = True
for i in range(0, 480, 1):
    common.append(False)


def abs_time(time):
    pm = False
    if (time[-2:] == "PM"):
        pm = True
    time = time[:-2]
    hrmin = time.split(':')
    abst = int(hrmin[0])*60 + int(hrmin[1])
    if ( pm and int(hrmin[0]) != 12):
        abst += 12*60
    return abst

def time_str(time):
    pm= False
    hr = int(time/60)
    if hr > 12:
        hr -= 12
        pm = True
    if (hr == 12):
        pm = True
    if pm:
        return  (str(hr) + ":"+str(time % 60)+" PM")
    else:
        return  (str(hr) + ":"+str(time % 60)+" AM")

for schedule in eschedules:
    for slot in schedule:
        duration = slot.split(' -')
        for i in range(abs_time(duration[0]) - 540, abs_time(duration[1]) - 539, 1):
            common[i-1] = True
window = int(float(input())*60) - 2
f = 0
r = window
if flag:
    while common[f] == True:
        f += 1
    while f < (480-window) and flag:
        r = f+window
        if not(common[f] or common[r]):
            for i in range(f, r+1, 1):
                if common[i] == True:
                    flag = False
                    break
            if flag:
                break
        f += 1
if flag:
    outdict = dict()
    outdict[edates[0]] = [str(time_str(f+540) + " - " + time_str(r+542))]
    f = open("output.txt", "a")
    f.write("Slot Available:\n")
    f.write(str(outdict))
    f.close()
else:
    f = open("output.txt", "a")
    f.write("Slot not available")
    f.close()

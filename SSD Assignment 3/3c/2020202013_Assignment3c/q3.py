import json
with open('Employee1.txt') as f1:
  emp_dict1 = json.load(f1)
with open('Employee2.txt') as f2:
  emp_dict2 = json.load(f2)

emp_name = list()
emp_name.append(list(emp_dict1.keys())[0])
emp_name.append(list(emp_dict2.keys())[0])

dates = list()
dates.append(list(emp_dict1[emp_name[0]].keys())[0])
dates.append(list(emp_dict2[emp_name[1]].keys())[0])


e1_tlist = emp_dict1[emp_name[0]][dates[0]]
e2_tlist = emp_dict2[emp_name[1]][dates[1]]


print(e1_tlist)
e1_available = list()
e1_available.append(["9:00AM", "9:00AM"])

e2_available = list()
e2_available.append(["9:00AM", "9:00AM"])

for duration in e1_tlist:
    start_end = list()
    start_end = duration.split(' -')
    e1_available.append(start_end)

e1_available.append(["5:00PM", "5:00PM"])

for duration in e2_tlist:
    start_end = list()
    start_end = duration.split(' -')
    e2_available.append(start_end)
e2_available.append(["5:00PM", "5:00PM"])

for i in range(1, len(e1_available)):
    e1_available[i-1][1] = e1_available[i-1][1].replace(e1_available[i-1][1], e1_available[i][0])
    e1_available[i][0] = e1_available[i][0].replace(e1_available[i][0], e1_available[i][1])
try:
    e1_available.remove(['5:00PM', '5:00PM'])
except:
    print("")

for i in range(1, len(e2_available)):
    e2_available[i-1][1] = e2_available[i -1][1].replace(e2_available[i-1][1], e2_available[i][0])
    e2_available[i][0] = e2_available[i][0].replace(e2_available[i][0], e2_available[i][1])
try:
    e2_available.remove(['5:00PM', '5:00PM'])
except:
    print("")

e1_available_output = list()
e2_available_output = list()
for i in e1_available:
    e1_available_output.append(str(i).replace('\'', '').replace('[', '').replace(']', '').replace(', ', ' - ').replace('\"', '\''))
for i in e2_available:
    e2_available_output.append(str(i).replace('\'', '').replace('[', '').replace(']', '').replace(', ', ' - ').replace('\"', '\''))

print(e1_available_output)
print(e2_available_output)

f = open("output.txt", "a")
f.write(emp_name[0])
f.write(": ")
f.write(str(e1_available_output))
f.write("\n")
f.write(emp_name[1])
f.write(": ")
f.write(str(e2_available_output))
f.close()

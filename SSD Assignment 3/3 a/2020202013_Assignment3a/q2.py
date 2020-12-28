file1 = open('date_calculator.txt', 'r') 
count = 1
month_dict = {
    'Jan' : 0,
     1 : 0,
    'Feb' : 31,
    2 : 31,
    'Mar' : 59,
    3 : 59,
    'Apr' : 90,
    4 : 90,
    'May' : 120,
    5 : 120,
    'Jun' : 151,
    6 : 151,
    'Jul' : 181,
    7: 181,
    'Aug' : 212,
    8 : 212,
    'Sep' : 243,
    9 : 243,
    'Oct' : 273,
    10 : 273,
    'Nov' : 304,
    11 : 304,
    'Dec' : 334,
    12 : 304
    }

def abs_date(day, month, year):
  yd = (year-1)*365 + int(year/4) - int(year/100) + int(year/400)
  leap= 0
  md = month_dict[month]
  if (year % 4 == 0):
    if(year % 100 == 0):
      if(year % 400) == 0:
        leap = 1
      else:
         leap = 1
    else:
      leap= 1
  else:
    leap = 0
  if (month != 'January' and month != 'February' ):
    md += leap
  return ( yd + md + int(day) )


day = []
month = []
year = []
date_list = []


while True:
  line = file1.readline()
  if line :
    line = line[7:]
    if count == 1:
        line = line[:-1]
    print(line)
    if line[2] == '/' or line[1] == '/':
      date_list = line.split('/')
      day.append(int(date_list[0]))
      month.append(int(date_list[1]))
      year.append(int(date_list[2]))
    elif line[1] == '-' or line[2] == '-':
      date_list = line.split('-')
      day.append(int(date_list[0]))
      month.append(int(date_list[1]))
      year.append(int(date_list[2]))
      print(date_list)
    else:
      year.append(int(line[-4:]))
      line = line[:-6]
      if (line[0:2].isdigit()):
        day.append(line[0:2])
        line = line[4:]
      else:
        day.append(line[0:1])
        line = line[3:]
      month.append(line[:3])
    count = count+1

  else :
    break

day_difference = abs( abs_date(day[0],month[0],year[0]) - abs_date(day[1],month[1],year[1]) )
#print("Date Difference: "day_difference)
f = open("output.txt", "a")
f.write("Date Difference: ")
f.write(str(day_difference))
f.close()

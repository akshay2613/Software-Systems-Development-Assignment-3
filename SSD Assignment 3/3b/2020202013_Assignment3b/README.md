# 2020202013_Assignment3b

## Q1

A python program to find common leader of any two employees in an organization.
User can input any two employees’ Emp No. used input() function for it and user will get common leader (Emp ID) as an output.
Employee Number format is of type integer for e.g.: [001-999].

Assumptions Made -
The "org.json" will be a valid json file.
If the leader of the organisation is given as input then the program will output : "Invalid Output".
If the leader exists then output will be printed along with difference in number of levels with each employee.
changes :
4-8 : Used a list to store employee ids 
30-51 : Changed the logic by using a common path.


## Q2

A python program to find difference between given dates.

Assumptions Made -
The "date_calculator.txt" file will contain only one Date1 and one Date2.
The date format will contain only one Date1 and one Date2.
The "output.txt" file the will have output in the number of days.

changes :
56 - 64 : generalized initialization for formats other than string
used sys.argv to handle command line argumnents



## Q3

A python program that will search for all free slots for the given two employees and reserve the first available common slot.

list() constructor is used.
Python dictionary is used.
The append() method is used to append an element to the end of the list.

Assumptions Made - 
The input format will be as follows :
{"Employee1": {"5/10/2020":["10:00AM - 11:00AM", "12:30PM - 1:00PM", "4:00PM - 5:00PM"]}}


In the "output.txt" pprints will print the available slots.
2-10: reading files form a directory
17 - 58: finding available slots for all the employees in a for loop
60-121 : Finds the common slot

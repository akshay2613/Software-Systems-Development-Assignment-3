import json
with open('org.json') as f:
  json_object = json.load(f)
emp_count = int(input())
employee=[]
for i in range(emp_count):
  x  = input()
  employee.append(x)
x = dict()
i=0
root=""
for level in json_object:
  for dict_node in json_object[level]:
    if not("parent" in dict_node):
      root = dict_node["name"]
      dict_node["parent"] = None
    y = [dict_node["parent"],i]
    x[ dict_node["name"] ] = y
  i+=1

def path_to_root(key):
  path_list = []
  path_list.append(key)
  iter = key
  while iter != root :
    parent = x[iter][0]
    path_list.append(parent)
    iter = parent
  return path_list[::-1]
final_path = path_to_root(employee[0])
task_done = False

common_leader= ""
for emp in employee:
  if not ( task_done):
    if (emp == root):
      task_done = True
      print("Invalid input")
      break
    else:
      path = path_to_root(emp)
      for i in range(len(final_path)):
        if (final_path[i] != path[i]) :
          final_path[i] = None
        common_leader = final_path[i-1]
        common_leader_depth =i-1

if not(task_done):
  print("Common Leader is : ", common_leader)
for emp in employee :
  print("Leader ", common_leader, "is ", abs(x[common_leader][1] - x[emp][1]), " levels above ", emp)
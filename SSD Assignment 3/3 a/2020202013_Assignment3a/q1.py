import json
with open('org.json') as f:
  json_object = json.load(f)
x = dict()
i=0
root=""
for level in json_object:
  for dict_node in json_object[level]:
    if "parent" not in dict_node:
      root = dict_node["name"]
      dict_node["parent"] = "NA"
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

print(json_object)
print(x)
input1 = input()
input2 = input()
task_done = False
if ( input1 == root or input2 == root) :
  task_done = True
  print("Invalid input")

if task_done == False:
  path1 = path_to_root(input1)
  path2 = path_to_root(input2)
  for i in range(min(len(path1),len(path2))):
    if path1[i] != path2[i]:
      task_done = True
      print(path1[i-1])
      break
  if task_done == False:
    print(path1[i-1])

print("THE ", path1[i-1], "is " , abs(x[path1[i-1]][1] - x[input1][1]), " levels above ", input1)
print("THE ", path1[i-1], "is " , abs(x[path1[i-1]][1] - x[input2][1]), " levels above ", input2)
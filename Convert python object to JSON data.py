# Q.2 Python object ko json data main convert karne ka program likho?

# import json
# x={
#     "Name":"Kavitha",
#     "Age":30,
#     "City":"Hyderabad"
# }
# y=json.dumps(x)
# print(y)
# print(y)



import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)
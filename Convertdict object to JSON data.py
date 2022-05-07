# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
# Input :-                         
#  {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
# }

# Output:-
# JSON data:

# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }
import json
x= {'4': 5, '6': 7, '1': 3, '2': 4, '3':3}
# print("Original String:")
# print(j_str)
# print("\nJSON data:")
print("JSON data:")
print(json.dumps(x, sort_keys=True, indent=3))
# print("JSON data:")
# print(json.dumps(x,sort_keys="True"))
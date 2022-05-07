# Q.3 Python object ko json string mai convert karne ka program likho?

import json
print(json.dumps({"Name":"Kavitha","Age":30}))
print(json.dumps(["Apple","Banana"]))
print(json.dumps(("Apple","Banana")))
print(json.dumps("Hello"))
print(json.dumps(43))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
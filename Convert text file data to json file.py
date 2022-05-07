# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# Input :-
# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

# Output:-
# Json_file.json:-
# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }

import json
def convert() :
    f = open("log_events.log", "r")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent :
        pipesplit = line.split(' | ')
        print(pipesplit)
        with open("json_log.json", 'a') as fout:
            json.dump(pipesplit, fout, indent=4)
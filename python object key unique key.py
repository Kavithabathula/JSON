# # Q6.Python object key unique key value ko access karne ka program likho?

# # Input :-
# # '{
# #  "a":  1,
# #  "a":  2,
# #  "a":  3, 
# #  "a": 4,   
# #  "b": 1, 
# #  "b": 2
# #  }'

# # Output:-
# # Unique Key in a JSON object:-
# # {'a': 4, 'b': 2}
# # import json
# # a={
# #  "a":  1,
# #  "a":  2,
# #  "a":  3, 
# #  "a": 4,   
# #  "b": 1, 
# #  "b": 2
# #  }
# # b=json.dumps(a)
# # print(b)


import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("combobox")
root.geometry("600x600")

ttk.Label(root,text="Python life",background="Blue",foreground="white",
        font=("Times New Roman",15)).grid(row=0,column=1)

# # combolife
n=tk.StringVar()
course=ttk.Combobox(root,width=27,textvariable=n)
course['values']=("python",
                  "django",
                  "machine learning")
course.grid(column=1,row=5)
course.current()

root.mainloop()
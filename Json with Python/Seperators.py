import json
dic_data = {
"name" : "Jenny",
"age" : 25,	
"profession" : "developer"}
print(json.dumps(dic_data, indent=3,separators=(". ", " = ")))
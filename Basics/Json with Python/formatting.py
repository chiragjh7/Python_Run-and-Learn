import json
dic_data = {
"name" : "Jenny",
"age" : 25,	
"profession" : "developer"}
print(json.dumps(dic_data))
print(json.dumps(dic_data, indent=2))
print(json.dumps(dic_data, indent=4))
print(json.dumps(dic_data, indent=6))
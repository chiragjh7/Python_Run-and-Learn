# To convert the data into JSON format in python, we use the dumps() method. To convert into JSON, the data must be in JSON strings.
import json
dic_data = '{"name":"Jenny","age":25,"profession":"developer"}' 
json_data = json.dumps(dic_data)	
print(json_data)
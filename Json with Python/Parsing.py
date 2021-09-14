# the loads() method is used to parse the JSON in python. Once the JSON file is parsed, it is stored in the form of dictionary.

import json
# some json data
json_data = '{"name":"Jenny","age":25,"profession":"developer"}'
dic_data = json.loads(json_data)
print(dic_data["age"])

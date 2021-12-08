import json
dic_data = {
            "name" : "Jenny",
            "age" : 25,	
            "profession" : "developer",
            "skill set" : ("C" ,"CPP", "JAVA", "PYTHON"),
            "previous experience" : None,
            "academic details" : [
                                  {"qualification" : "UG" , "score" : 7.5 },
                                  {"qualification" : "HSC" , "score" : 90}
                                  ]
            }
json_data = json.dumps(dic_data)
print(json_data)
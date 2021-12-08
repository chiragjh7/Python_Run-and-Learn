import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())
print(df)

dataa = {
    "duration" : {
        "0" : "60",
        "1" : "50",
        "2" : "20",
        "3" : "90",
        "4" : "49",
        "5" : "53",
        "6" : "100"
    },
    "calories": {
        "0" : "120.2",
        "1" : "333.1",
        "2" : "145.5",
        "3" : "346.4",
        "4" : "233.3",
        "5" : "333.3",
        "6" : "533.3"
    } 
}
dff = pd.DataFrame(dataa)
print(dataa)
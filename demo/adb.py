import json
data = {
    'name' : 'myname',
    'age' : 100,
}
json_str = json.dumps(data)
print(json_str)
print(json_str.encode("utf-8"))

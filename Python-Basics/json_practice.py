import json

person = {
    "name": "Dawood",
    "age": 22,
    "skills": ["Python", "React", "Laravel"]
}

json_string = json.dumps(person)
print(type(json_string))  
print(json_string)

print("---")

json_back=json.loads(json_string)
print(type(json_back))
print(json_back["name"])  
print(json_back["skills"])
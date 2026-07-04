user_info={
    "name":"dawood",
    "age":22,
    "city":"Sheikhupura",
    "skills": ['MERN', 'Laravel', 'Python']
}

for key, value in user_info.items():
    print(f"{key} : {value}")

skill_name = input("Please enter the skill name: ")

user_info["skills"].append(skill_name)

print(f"Updated skills: {user_info['skills']}")
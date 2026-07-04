class Developer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{skill} added successfully")  # no return

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            print(f"{skill} removed successfully")
        else:
            print("Skill not found")

    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")
        if self.skills:  # check if skills list is not empty
            skills_string = ", ".join(self.skills)
            print(f"I know: {skills_string}")
        else:
            print("No skills added yet.")
        print(f"Total skills: {len(self.skills)}")


# First developer
developer_one = Developer("Dawood", 22)
developer_one.add_skill("React")
developer_one.add_skill("n8n")
developer_one.add_skill("Next js")
developer_one.introduce()
developer_one.remove_skill("React")
developer_one.introduce()

print("---")  # separator

# Second developer
developer_two = Developer("Ali", 21)
developer_two.add_skill("Python")
developer_two.add_skill("Django")
developer_two.introduce()
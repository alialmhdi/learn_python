class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.user_id()

    def user_id(self):
        user_id = self.name[0].upper() + self.last_name + str(self.birth_year)
        print(user_id)


user_name = input()
user_last_name = input()
user_birth = input()
s = Student(user_name, user_last_name, user_birth)

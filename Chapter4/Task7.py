class Student:
    def __init__(self, full_name, age, major):
        self.full_name = full_name
        self.age = age
        self.major = major

    def __str__(self):
        return f'<name: {self.full_name}, age: {self.age}, major: {self.major}>'


bob = Student('Bob Bobikov', 18, 'Programmer')
steve = Student('Steve Jobs', 19, 'Programmer')
tony = Student('Tony Stark', 20, 'Programmer')
print(steve)
print()
print(bob)
print()
print(tony)
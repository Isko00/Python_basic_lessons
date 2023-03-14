class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
        # return self.name + '(' + str(self.age) + ')'

    def print_name(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

print(p1)
p1.print_name()

p1.age = 40
print(p1.age)

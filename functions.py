class Name:
    def __init__(self, name, age,location):
        self.name = name
        self.age = age
        self.location=location
    def __str__(self):
       return f' My name is {self.name} \n I am {self.age} years old \n I live in {self.location}'


p1 = Name("Harshil Buch", 19,"Pune")
print(str(p1))
# print(p1.name)
# print( p1.age)
# print(p1.location)

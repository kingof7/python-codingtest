class Person:
    def __init__(self, name, age): # self는 객체 자기 자신, 인스턴스화에 필요한 변수, 자기 자신의 정보를 가져오는 역할
        self.name = name
        self.age = age
    def talk(self):
        print(f"{self.name} is talking. Hi, I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.talk()
print(person1, person1.name, person1.age)


person2 = Person("Bob", 25)
person2.talk()
print(person2, person2.name, person2.age)


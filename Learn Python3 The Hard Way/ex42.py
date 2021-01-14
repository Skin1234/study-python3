#Animal is a class
class Animal(object):
    pass

#Dog is a Animal
class Dog(Animal):

    def __init__(self,name):
        #Dog has a name
        self.name = name


class Cat(Animal):

    def __int__(self,name):
        #Cat has a name
        self.name = name

#Person is a class
class Person(object):

    def __init__(self,name):
        #Person has a name
        self.name = name
        #Person has a pet
        self.pet = None

#Employee is a Person
class Employee(Person):

    def __init__(self,name,salary):
        #初始化父类，否则Employee没有name
        super(Employee,self).__init__(name)
        #Employee has salary
        self.salary = salary

#Fish is a class
class Fish(object):
    pass

#Salmon is a Fish
class Salmon(Fish):
    pass

#Halibut is a Fish
class Halibut(Fish):
    pass

#Rover is a Dog
rover = Dog("Rover")

#Satan is a Cat
satan = Cat("Satan")

#Mary is a Person
marry = Person("Mary")

#marr has a pet is satan
marry.pet = satan

frank = Employee("Franl",120000)

#frank has a pet is rover
frank.pet = rover

#flipper is a Fish
flipper = Fish()

#crouse is a Salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()
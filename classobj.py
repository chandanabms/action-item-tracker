#program on class amd objectclass Person:
class car:
	def __init__(self,modelname, year): #constructor
		self.modelname = modelname
		self.year = year
	def display(self): #method
		print(self.modelname,self.year)
c1 = car("toyoto",2016) #object1
c2 = car("bajaj", 2017) #object2
c1.display()
c2.display()

# python program on inheritance

class employee1(): #/This is a parent class
	def __init__(self, name, age, salary):
		self.name =  name
		self.age = age
		self.salary = salary
class childemployee(employee1): #/This is a child class
	def __init__(self, name, age, salary,id):
		self.name = name
		self.age = age
		self.salary = salary
		self.id = id
emp1 = employee1('chandu mahi',22,10000)
print(emp1.name)
print(emp1.age)
print(emp1.salary)

#python progarm on polymorphism

class music:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am musician. My name is {self.name}. I wrote {self.age} song.")

    def make_sound(self):
        print("guitar")


class musician:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a musician. My name is {self.name}. I wrote {self.age} song.")

    def make_sound(self):
        print("piano")


music1 = music("arjun janya", "kempegowda ")
musician1 = musician("hamsalekha", "ramachari")

for i in (music1, musician1):
    i.make_sound()
    i.info()
    i.make_sound()


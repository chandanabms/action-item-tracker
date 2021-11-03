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

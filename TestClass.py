#!/use/bin/env python3
# -*- conding:UTF-8 -*-


class Employee:
	'''员工类 '''
	""" 员工类 """
	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		print("Employee类被创建了")

	def displayCount(self):
		print("Total Employee %d" % Employee.empCount)

	def displayEmployee(self):
		print("Name:",self.name,", Salary:",self.salary)




print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)


print("\n==================================================\n")





"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp2.displayCount()
emp2.displayEmployee()





print("\n==================================================\n")


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

class Animal: # parent
    
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    
    def toString(self):
        print("monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey calls overriding method

# %%
class Rectangle():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
class Square(Rectangle):
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
	def getArea(self):
		print(self.side*self.side," is area of square")
s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()
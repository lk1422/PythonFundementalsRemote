'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math
class circle():
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		x = self.radius**2
		area = math.pi * x
		return area
	def circumference(self): #ignore my spelling lol
		circum = 2*self.radius*math.pi
		return circum
class rectangle():
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.width*self.length
	def circumference(self):
		return 2*self.length + 2*self.width
'''
circl1 = circle(3)
print(circl1.area(),circl1.circumference())
rect1 = rectangle(3,4)
print(rect1.area(), rect1.circumference())
'''
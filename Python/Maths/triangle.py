#THIS IS A SOLUTION OF ONE OF THE PROBLEMS OF THE PCAP STUDY RESOURCES
#Here we are constructing a triangle with three points in a plane with the Cartesian coordinate system
#Then we are defining a method to get the perimeter of the triangle
import math

class Point:
	def __init__(self, x: float, y: float):
		self.__x = x
		self.__y = y
	
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def getPointsDistance(self, x: float, y: float):
		a = self.__x - x
		b = self.__y - y
		return math.hypot(a, b)
	
	def getPointsDistance1(self, point: object):
		a = self.__x - point.__x
		b = self.__y - point.__y
		return math.hypot(a, b)

class Triangle:
	def __init__(self, point1: object, point2: object, point3: object):
		self.__point1 = point1
		self.__point2 = point2
		self.__point3 = point3

	def perimeter(self):
		return self.__point1.getPointsDistance1(self.__point2) + self.__point2.getPointsDistance1(self.__point3) + self.__point3.getPointsDistance1(self.__point1)



if __name__ == '__main__':
	point1 = Point(0, 0)
	point2 = Point(1, 0)
	point3 = Point(0, 1)
	triangle = Triangle(point1, point2, point3)
	print(f"\033[1;36;40mPerimeter of triangle: {triangle.perimeter()}\033[0m")

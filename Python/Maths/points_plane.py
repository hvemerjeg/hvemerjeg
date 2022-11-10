#THIS CODE IS A SOLUTION OF A PROBLEM OF THE PCAP STUDY RESOURCES
#In this problem we are constrcuting points in a plane with the Cartesian coordinate system and computing the distance between points.
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
	#This method does the same as the one above. The only difference is the format of the parameters we are getting. In this case we accept and object.
	def getPointsDistance1(self, point: object):
		a = self.__x - point.__x
		b = self.__y - point.__y
		return math.hypot(a, b)

if __name__ == '__main__':
	point = Point(2, 0)
	point1 = Point(1, 1)
	print(point1.getPointsDistance(0, 0))
	print(point.getPointsDistance1(point1))

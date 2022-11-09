#THIS IS AN OOP EXERCISE THAT APPEARS IN THE PCAP STUDY RESOURCES
#This code is for displaying days of the week in a specific format and also adding or subtracting days to that day.
class Weeker:
	__weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
	def __init__(self, day: str):
		assert day in Weeker.__weekdays, "\033[1;31;40mThe day is not in the right format or that day does not exist!\033[0m"
		self.__day = day

	def __str__(self):
		return f"\033[1;36;40m{self.__day}\033[0m"

	def addDays(self, n: int):
		self.__day = Weeker.__weekdays[(Weeker.__weekdays.index(self.__day) + n) % len(Weeker.__weekdays)]
	
	def subtractDays(self, n: int):
		self.__day = Weeker.__weekdays[(Weeker.__weekdays.index(self.__day) - n) % len(Weeker.__weekdays)]

if __name__ == '__main__':
	weekday = Weeker('Mon')
	print(weekday)
	weekday.addDays(8)
	print(weekday)
	weekday.subtractDays(1)
	print(weekday)

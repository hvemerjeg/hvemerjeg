#THIS IS AN OOP EXERCISE THAT APPEARS IN THE PCAP STUDY RESOURCES
#This code is for displaying a time in a specific format and also adding or subtracting one second to that time.
class Timer:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds

	def __str__(self):
		string_hours = str(self.__hours)
		string_minutes = str(self.__minutes)
		string_seconds = str(self.__seconds)
		if len(str(self.__hours)) == 1:
			string_hours = '0' + str(self.__hours)
		if len(str(self.__minutes)) == 1:
			string_minutes = '0' + str(self.__minutes)
		if len(str(self.__seconds)) == 1:
			string_seconds = '0' + str(self.__seconds)
		return f"\033[1;36;40m{string_hours}:{string_minutes}:{string_seconds}\033[0m"

	def nextSecond(self):
		self.__seconds = (self.__seconds + 1) % 60
		if self.__seconds == 0:
			self.__minutes = (self.__minutes + 1) % 60
			if self.__minutes == 0:
				self.__hours = (self.__hours + 1) % 24

	def previousSecond(self):
		self.__seconds = (self.__seconds - 1) % 60
		if self.__seconds == 59:
			self.__minutes = (self.__minutes - 1) % 60
			if self.__minutes == 59:
				self.__hours = (self.__hours - 1) % 24

if __name__ == '__main__':#As you know, any module named __main__ is actually not a module, but the file currently being run.
    time = Timer(2, 0, 59)
	print(time)		
	time.nextSecond()
	print(time)
	time.previousSecond()
	print(time)

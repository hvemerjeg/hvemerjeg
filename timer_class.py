#THIS IS AN OOP EXERCISE THAT APPEARS IN THE PCAP STUDY RESOURCES
class Timer:#Here we define our class Timer and we specify some attributes.
    def __init__(self, hours: int, minutes: int, seconds: int):#Our class will have three attributes. 
#All the objects created using this class will share the attributes, but we can create
#new attributes for just one object outside the class.
        assert hours < 24 and minutes < 60 and seconds < 60, "Sorry, there is an error in your input"
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def show_time(self):#This is a method. Is a function that our objects will be able to use.
#This method in concrete will display the time in the following format: hh:mm:ss
#using military time.
        self.hours, self.minutes, self.seconds = str(self.hours), str(self.minutes), str(self.seconds)
        if len(self.hours) != 2:
            self.hours = "0" + self.hours
        if len(self.minutes) != 2:
            self.minutes = "0" + self.minutes
        if len(self.seconds) != 2:
            self.seconds = "0" + self.seconds
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):#This method will add a second to the time provided.
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        ####TRANSFORMING
        if int((self.seconds + 1) % 60 ) == 0:
            self.minutes = int(self.minutes + (self.seconds + 1 ) / 60) % 60
            self.seconds = int((self.seconds + 1) % 60 )
            if self.minutes == 0:
                self.hours = int(self.hours + 1) % 24
        else:
            self.seconds = int((self.seconds + 1) % 60 )

        print(self.show_time())
        
    def prev_second(self):#This method will substract a second to the time provided.
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        ####TRANSFORMING
        self.seconds = (self.seconds - 1) % 60
        if self.seconds == 59:
            if self.minutes == 0:
                self.minutes = 59
                self.hours = (self.hours - 1) % 24
            else:
                self.minutes = (self.minutes - 1) % 60
        print(self.show_time())

if __name__ == '__main__':#As you know, any module named __main__ is actually not a module, but the file currently being run.
    n = int(input("Insert number of times: "))
    for _ in range(n):
        the_input = list(map(int, input().split(" ", 2)))
        horas, minutos, segundos = the_input[0], the_input[1], the_input[2]
        time = Timer(horas, minutos, segundos)
        print("\n" + time.show_time())
        time.next_second()
        time.prev_second()

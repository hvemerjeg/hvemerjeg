#STACK DATA STRUCTURE
class Stack:
    def __init__(self):
        self.__stack_list = []
        self.top = -1
    
    def push(self, valor: int):
        if self.isfull() == True:
            return "Stack is full"
        self.__stack_list.append(valor)
        self.top += 1
        return self.__stack_list
    
    def pop(self):
        if self.isempty() == True:
            return "Stack already empty"
        del self.__stack_list[-1]
        self.top -= 1
        return self.__stack_list
    
    def isfull(self):
        return self.top == 9

    def isempty(self):
        return self.top == -1
        

#SOME TESTS
if __name__ == '__main__':
    stack1 = Stack()
    for numero in range(12):
        print(stack1.push(numero))
    for numero in range(11):
        print(stack1.pop())
    print(stack1.isfull())
    print(stack1.isempty())
    print(stack1.push(1))

#THIS CODE IS A SOLUTION OF THE PROBLEM VALIDATE SUBSEQUENCE.
#Prompt: Given two arrays or tuples, determine if the second list/tuple is a subsequence of the first one.
#The first condition that the second list/tuple needs to meet to be a subsequence
#of the first tuple/list, is that it must be a subset of the first list/
#tuple. The second condition that the second list/tuple needs to meet, is that the
#elements appear in the same order as they appear in the main list/tuple.
#EXAMPLE the_array = 5, 1, 22, 25, 6, -1, 8, 10 and the_sequence = 1, 6, -1, 10. In this case we should
#display true because the_sequence is a subsequence of the the_array.
def valid_subsequence(tupla: tuple, sequence: tuple):#I decided to use tuples instead of list
#since we are not manipulating the elements.
    indx = 0
    indx1 = 0
    while indx < len(tupla) and indx1 < len(sequence):
        if sequence[indx1] == tupla[indx]:
            indx1 += 1
        indx += 1#So, we iterate through the tuple an check if an element is equal to the first element of 
#the sequence. If they are equal, we need to compare the second element of the sequence, so in this case
#indx1 += 1. 
    return indx1 == len(sequence)#If indx1 equals the length of the sequence means that not only
#all the elements in the sequence appears in the main array, but also they appear in order.


#THERE EXIST DIFFERENTS WAYS OF SOLVING THIS PROBLEM, BUT THE FIRST APPROACH IS EFFICIENT ENOUGH.
#SECOND APPROACH:
#This is an efficient approach too.
def valid_s_bsequence(tupla: tuple, sequence: tuple):#I decided to use tuples instead of list
#since we are not manipulating the elements.
    indx1 = 0
    for indx in range(len(tupla)):
        if tupla[indx] == sequence[indx1]:
            indx1 += 1
        if indx1 == len(sequence):
            return indx1 == len(sequence)
    return indx1 == len(sequence)

#THIRD APPROACH:
#This approach is not an efficient one, but I have a special place in my heart to this one, because this is one of 
#the first solutions that I came to when I started in python.
def valid_s_b_quence(arr: list, s: tuple):#In this case I need to manipulate the elements inside the main
#list, thats the reason why I am using a list in this case.
    x = []
    y = []
    for i in s:
        try:
            x.append(arr.index(i))
            y.append(arr.index(i))
            arr.insert(arr.index(i), 'A')#This nonsense swap, is because the function .index() gets the
#index of the first coincidence. So if we a have repeated values we will have troubles.
            arr.remove(i)
        except ValueError:
            return False#This means that the sequence s, is not a subset of the main list arr.
    x.sort()#To check if the values appeared in order we try to apply the sort function to one of our 
#created lists.
    if x != y:#If this list changes when the sort is applied that means it was not ordered in first place.
#So we return False
        return False
    else:
        return True
    
if __name__ == '__main__':
    the_array = tuple(map(int, input().split()))
    the_sequence = tuple(map(int, input().split()))  
    print(valid_subsequence(the_array, the_sequence))
    print(valid_s_bsequence(the_array, the_sequence))
    the_array = list(the_array)
    print(valid_s_b_quence(the_array, the_sequence))
	

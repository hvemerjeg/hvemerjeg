#THIS CODE IS A SOLUTION FOR A WELL KNOWN CODING PROBLEM CALLED "IS PALINDROME".
#The task is to check if a string is palindrome.
#A palindrome is a string which reads the same backwards and forwards.
#We need to return true if the string is palindrome and false if not.


#FIRST APPROACH
#This is the first approach to the problem. Is the more intuitive(normally the first approach 
#to a problem is the intuitive one), but not the more efficient.
#Here we create other variable that is going to store the reversed string and then we check if the
#original string and the reversed string are the same.
def isPalindrome1(cadena: str):
    reversed_cadena = cadena[::-1]#Reversing the original string.
    if cadena == reversed_cadena:#Checking if the strings are the same.
        return True
    return False

#SECOND APPROACH
#The second approach is interesting. We do not need to reverse the whole string and neither to store
#the whole string reversed in another variable. With this approach we make less comparisons.
#The procedure is to check if the first character is the same as the last, and the second is the same as
#the second to last. We keep comparing this way until we arrive to the middle of the string.
def isPalindrome(cadena: str):#This is the main function.
    l = 0
    r = len(cadena) - 1
    while l < r:
        if cadena[l] == cadena[r]:#If the character at index l is the same as the character at index
#r we sum one to l and subtract one to r.
            l += 1
            r -= 1
        else:#Otherwise if those characters are not the same then we know that the string is not
#palindrome.
            return False
    return True#If we are done making comparisons then we know that the string is palindrome.

if __name__ == '__main__':
    my_string = 'aba'
    print(isPalindrome1(my_string))
    print(isPalindrome(my_string))

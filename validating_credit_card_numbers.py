#THIS CODE IS THE SOLUTION FOR A HACKERRANK PROBLEM CALLED "VALIDATING CREDIT CARD NUMBERS"
#The problem is the following:
"""A valid credit card has the following characteristics:

1. It must start with a 4, 5 or 6.
2. It must contain exactly 16 digits.
3. It must only consist of digits (0-9).
4. It may have digits in groups of 4, separated by one hyphen "-".
5. It must NOT use any other separator like ' ' , '_', etc.
6. It must NOT have 4 or more consecutive repeated digits.
EXAMPLE:
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
4123356789123456 : Valid
51-67-8912-3456 : Invalid, consecutive digit 3 is repeating 4 times.
5123 -- 4567 -- 8912 -- 3456 : Invalid, because space '  ' and - are used as separators."""
#I found this problem interesting because of the need to know RegEx and the applications of this knowledge through
#a module called re. More information about this module in the oficial documentation of python: 
# https://docs.python.org/3/library/re.html
import re#We import the module necessary to make use of RegEx

n = int(input())
for _ in range(n):#This line of code is due to the need to get diferent credit card numbers.
    contador = 0#We are going to use this contador variable to make sure that we print "Valid" only if we 
#finished to iterate through all the elements of the credit card number.
    credit_card_number = input()
    pattern = "^[4-6]{1}[0-9]{15}$"#This pattern is for validating credit card numbers without a hyphen
    pattern2 ="^[4-6]{1}[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"#This pattern is for validating credit card 
#numbers with a hyphen
    if len(credit_card_number) == 16:
        x = 3#Because we need to validate that we do not have more than 3 consecutive repeated digits. So we try from i to i + x for every element i in the credit card number.
    elif len(credit_card_number) == 19:
        x = 5#In this case, when we are validating credit card numbers with hyphen is necessary that the x value is higher. Example: 5133-3367-8912-3456. Note that we have 
    #the number three repeated more than three times, but we have a hyphen between this repeated numbers. If we count only from lets say i to i + 3 we will miss the fact
    # that the number three is repeated more than three times consecutive.
    if re.search(pattern, credit_card_number) or re.search(pattern2, credit_card_number):#If one of the patterns is matched, then we make the following.
                
        for i in range(len(credit_card_number)):#We iterate through every element not taking the element but the index of the element.
            if credit_card_number[i: i + x].count(credit_card_number[i]) > 3:#We try to find if there is a number consecutive repeated more than three times. If this is the case
                #we print invalid and we stop this case.
                print("Invalid")
                break
            elif contador == (len(credit_card_number) -1):#If we finished the iteration through each element of the credit card number and no invalid has been found, then we print
                #valid
                    print("Valid")
            else:#We can not print valid yet neither invalid because we are not finished trying every element of the credit card number.
                contador += 1
    else:
        print("Invalid")#No pattern has been found, then we print invalid.

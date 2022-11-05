#THIS CODE IS A SOLUTION FOR A WELL KNOWN CODING PROBLEM CALLED "SORTED SQUARED ARRAYS"
#The task is to, taking a non-empty array/list of integers that are sorted in ascending order, return a new array of the same length
#with the squares of the original integers also sorted in ascending order
#For example given the next list: [-3, 1, 2]
#We need to output: [1, 4, 9]
def sortedSquaredArray(arr: list):
    result = [] #This is our empty list where we are going to store the result 
    #To solve this problem efficiently you need to think that even if the input array is sorted the squared array may
    #not be sorted because of the presence of negative numbers.
    #What are the greater values in the array? Those to the right side since it is sorted in ascending order, but when a number is raised to two
    #it is going to result in a positive number.
    #If we take the absolute value in case of negative numbers we are going to see that the greater values are not necessarily those in the right side of
    #the array. So, since every number squared is a positive number, then we do not care if the number is negative.
    #Take a look at the code:
    l = 0 
    r = len(arr) - 1 
    while l <= r: #We are going to take the absolute value of the number at index l and compare it to the number at index r
        if abs(arr[l]) >= arr[r]: #In case that the absolute value of the number at index l is grater or equal to the number at index r
            #We are going to insert into the result array the value of the number at index l raised to two and add 1 to l
            result.insert(0, arr[l] ** 2)
            l += 1
        else: #In the other case, we are going to insert the number at index r in the result array and subtract 1 to r
            result.insert(0, arr[r] ** 2)
            r -= 1
    return result

if __name__ == '__main__':
    #TESTS
    dictionary_tests = {(1, 2, 3, 5, 6, 8, 9): [1, 4, 9, 25, 36, 64, 81], (0,): [0], tuple(): [], (-3, 1, 2): [1, 4, 9]}
    for test in dictionary_tests:
        if dictionary_tests[test] != sortedSquaredArray(list(test)):
            print(f"\033[1;31;40m[+] Not passed:\033[0m {list(test)}")
        else:
            print(f"\033[1;32;40m[+] Passed!:\033[0m {list(test)}")

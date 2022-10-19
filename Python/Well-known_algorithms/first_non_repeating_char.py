#THIS CODE IS A SOLUTION FOR A WELL KNOWN CODING PROBLEM CALLED "First non repeating character"
#The task is to find the first non repeting character in a given non empty string and return the index of that character
#If there is not a single character that is only once in the string, we need to return -1
def firstNonRepeatingCharacter(string: str):
    dict_frequency = {}#We create and empty dictionary that we are going to use to keep track of repeating characters

    for character in string:#First of all we iterate through the string to store in dict_frequency which characters are repeated
        if character not in dict_frequency:
            dict_frequency[character] = False#If the character is not repeated we set the value False
        else:
            dict_frequency[character] = True#if repeated we set the value to True
    
    for indx in range(len(string)):#We iterate once again through the string and looking into the dictionary if the value associated with that
#character is False.
        if dict_frequency[string[indx]] == False:#if the value associated that character is false we reuturn the index and end the execution of the function
            return indx
    return -1#If there is not a single character that occurs only once in the string we return -1
    
if __name__ == '__main__':
    #TESTS
    test_dictionary = {"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz": -1, "abcdcaf": 1, "lco": 0, "jjkkooas": 6}
    for test in test_dictionary:
        if test_dictionary[test] != firstNonRepeatingCharacter(test):
            print(f"\033[1;31;40m[+] Not passed:\033[0m {test}")
        else:
            print(f"\033[1;32;40m[+] Passed!:\033[0m {test}")

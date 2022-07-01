#THIS CODE IS THE IMPLEMENTATION OF AN EASY WELL-KNOWN SORT ALGORITHM CALLED BUBBLE SORT.
#More information about the Bubble Sort algorithm:https://en.wikipedia.org/wiki/Bubble_sort
#There are functions in different programming languages that helps you to sort an array/list and 
#there is a sort algorithm behind those functions.
#For example, behind the .sort() function in python the Timsort algorithm is applied.
def bubblesort(arr):#This is our main function that will hold our bubble sort implementation.
    número_de_comparaciones = (len(arr) - 1)#In the first pass we will need to make n - 1 comparisons, where n is the length of the list. This number is decreasing since 
#after the first pass we have the highest number in the correct position. So after the first pass we will need to make n - 2 comparisons, after the third n - 3 comparisons etc..
    swap = True#We will make use of this variable to check if there is a swap. If in one whole pass there has been no change we will know that our elements are ordered correctly. 
    while número_de_comparaciones > 0 and swap == True:#So if there has been no change in a whole pass meaning that swap equals false or the number of comparisons is not higher
#than 0 we know that we are done.
        swap = False
        for i in range(número_de_comparaciones):
            while arr[i] > arr[i + 1]:#We compare the element in the position i with the element in the position i + 1. If the element in the position i is higher than the
#element in the position i + 1 we swap them.
                arr[i], arr[i + 1] = arr[i + 1], arr[i]#swaping them if the above condition is met.
                swap = True#Setting swap to true because there has been a swap.
        número_de_comparaciones -= 1#As I said before, after one whole pass through the array we have the highest number in the correct position, so we will need to make
#one less comparison.
    print(arr)#Getting our ordered list.



if __name__ == '__main__':
    my_array = list(map(int, input().split()))#Getting a list as input and converting the elements inside the list to integers.
    bubblesort(my_array)#Calling the function.

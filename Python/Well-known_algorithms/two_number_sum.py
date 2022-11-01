#TWO TARGET SUM IS A WELL-KNOWN CODING PROBLEM
#The task of this problem is, given an array of distinct integers and a target which is an integer too, to return two numbers of the array that sum up to the target.
#If no two numbers sum up to the target integer then we need to return False 

#First approach
#The first approach that probably we are going to think about is a brute-force apporach. We will use two for loops and try every posibility. If two numbers sum up to target then we return those numbers. 
#Lets code it
def twoNumberSum(arr: list, target: int):
	for num in range(len(arr) -1):
		for num2 in range(num + 1, len(arr)):
			if arr[num] + arr[num2] == target:
				return [arr[num], arr[num2]]
	return False

#Second approach
#This is approach is more efficient than the first. In this case we are going to use a set where we are going to store the values already seen. 
def twoNumberSum1(arr: list, target: int):
	nums_seen = set()
	for num in arr:
		if target - num in nums_seen:
			return [num, target - num]
		nums_seen.add(num)
	return False 	

#Third approach
#In this approach we will start by sorting the given array. Then we will take advantage of the fact that the array is already sorted.
def twoNumberSum2(arr: list, target: int):
	arr.sort()
	l = 0
	r = len(arr) - 1
#We start by checking if the biggest number in the array + the lowest number in the array sum up to the target. If our sum is higher than the target we need to decrement r by one, if our sum is 
#lesser than the target we need to increment l by one.
	while l < r:
		if arr[l] + arr[r] == target:
			return [arr[l], arr[r]]
		elif arr[l] + arr[r] < target:
			l += 1
		else:
			r -= 1
	return False

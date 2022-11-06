#THREE NUMBER SUM
#This problem is a little bit more difficult than the two number sum problem
#Here we are given a unordered non-empty array of integers and a target(int) and we are asked to fidn three numbers that sum up to target
def threeNumberSum(arr: list, target: int):
	result = []
	arr.sort() #In this problem we are going to start by sorting the array in ascending order
	for indx in range(len(arr) - 2): #We are going to iterate through the elements of the array starting at index 0 to index -3
	#The next pattern is well known. 
		l = indx + 1
		r = len(arr) - 1
		while l < r:
			if arr[indx] + arr[l] + arr[r] == target:
				result.append([arr[indx], arr[l], arr[r]])
				l += 1
				r -= 1
			elif arr[indx] + arr[l] + arr[r] < target:
				l += 1
			else:
				r -= 1
	return result




if __name__ == '__main__':
	#TEST
	the_array = [12, 3, 1, 2, -6, 5, 100]
	print(threeNumberSum(the_array, 0))

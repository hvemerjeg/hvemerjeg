def insert_sort(arr: list):
    for indx in range(1, len(arr)):
        indx1 = indx
        swap = False
        while arr[indx1 - 1] > arr[indx] and indx1 > 0:
            indx1 -= 1
            swap = True
        if swap:
            arr.insert(indx1, arr[indx])
            del arr[indx + 1]
    return arr
    



if __name__ == '__main__':
    my_array = [i for i in range(4, -1, -1)]
    print(insert_sort(my_array))

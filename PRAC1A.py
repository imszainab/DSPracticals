'''a. Write a program to store the elements in 1-D array and provide an option to 
perform the operations like searching, sorting, merging, reversing the elements.'''

#1) searching
def binarySearch(arr, low, high, key): 

  

    if (high < low): 

        return -1

    mid = (low + high)/2

  

    if (key == arr[int(mid)]): 

        return mid 

  

    if (key > arr[int(mid)]): 

        return binarySearch(arr, 

           (mid + 1), high, key) 

  

    return (binarySearch(arr, low, 

           (mid -1), key)) 


arr = [5, 6, 7, 8, 9, 10] 

n = len(arr) 

key = 10

print("Index:", int(binarySearch(arr, 0, n, key) ))



#2) Sorting

numbers = [1, 3, 4, 2] 
# Sorting list of Integers 
numbers.sort() 
print(numbers)


#3) Merging
def mergeArrays(arr1, arr2, n1, n2): 

    arr3 = [None] * (n1 + n2) 

    i = 0

    j = 0

    k =0

    while i < n1 and j < n2: 

        if arr1[i] < arr2[j]: 

            arr3[k] = arr1[i] 

            k = k + 1

            i = i + 1

        else: 

            arr3[k] = arr2[j] 

            k = k + 1

            j = j + 1 

    while i < n1: 

        arr3[k] = arr1[i]; 

        k = k + 1

        i = i +1

    while j < n2: 

        arr3[k] = arr2[j]; 

        k = k + 1

        j = j + 1

    print("Array After Merging") 

    for i in range(n1 + n2): 

        print(str(arr3[i]), end = " ") 

  

arr1 = [1, 3, 5, 7] 

n1 = len(arr1) 
arr2 = [2, 4, 6, 8] 

n2 = len(arr2) 
mergeArrays(arr1, arr2, n1, n2);



#4) reverse
def reverseList(A, start, end):

    while start < end:

        A[start], A[end] = A[end], A[start]

        start += 1

        end -=1

A = [1, 2, 3, 4, 5, 6]

print(A)

reverseList(A, 0, 5)

print("Reversed List is")

print(A)

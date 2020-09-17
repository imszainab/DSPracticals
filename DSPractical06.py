#Code Block To Perform Selection Sort
def SelectionSort(A):  
    for i in range(len(A)): 
        small = i 
        for j in range(i+1, len(A)): 
            if A[small] > A[j]: 
                small = j 
        A[i], A[small] = A[small], A[i] 
  

#Code Block To Perform Insertion Sort
def InsertionSort(arr): 

    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  

#Code Block Perform Bubble Sort
def SubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

A = [64, 25, 12, 22, 11]   
opt = input("Search By Entering I,B or S ")
if opt == 'I' :
    BubbleSort(A) 
    print("This Is Insertion Sort")
    print(A)
elif opt == 'B':
    InsertionSort(A)
    print ("This Is Bubble Sort")
    print(A)
elif opt == 'S':
    SelectionSort(A)
    print ("This Is Selection Sort") 
    print(A)

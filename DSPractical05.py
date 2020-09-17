def LinearSearch(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 

def BinarySearch(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1

        elif arr[mid] > x: 
            high = mid - 1
  
        else: 
            return mid 
  
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  

opt = input("Search By Entring L Or B")
if opt == "B":
    result= BinarySearch(arr,x)
    print("Binary Search")
    print(result)
    
elif opt == "L":
    result= LinearSearch(arr,x)
    print("Linear Search")
    print(result)

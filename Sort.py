def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
n = input("Enter the elements of the list seperated with space: ")
arr = n.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
bubble_sort(arr)
print("Sorted array:", arr)

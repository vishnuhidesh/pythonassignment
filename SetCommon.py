n1 = input("Enter the elements of the first list seperated with space: ") 
n2 = input("Enter the elements of the second list seperated with space: ")
l1 = n1.split(" ")
l2 = n2.split(" ")
set1 = set(l1)
set2 = set(l2)
n = len(set1.intersection(set2)) > 0
if n:
    print("Both the lists have atleast one common element")
else:
    print("Neither of the lists have even one common element")


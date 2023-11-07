# Print all the common elements of two lists

l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l2 = [2,4,6,8,10,20,30,40]
set1 = set(l1)
set2 = set(l2)
sa = set1.intersection(set2)
print("The common elements in the three lists are",list(sa))
# Check if two lists have at least one common element 
# 2) using list comprehension

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [i for i in l1 if i in l2]
n = len(l3) > 0
if n:
    print("Both the lists have atleast one common element")
else:
    print("Neither of the lists have even one common element")

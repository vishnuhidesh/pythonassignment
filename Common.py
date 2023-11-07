l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l2 = [2,4,6,8,10,20,30,14]
l3 = [2,6,8,10,12,14,15,16,17,18,19,20]
set1 = set(l1)
set2 = set(l2)
set3 = set(l3)
sa = set1.intersection(set2)
sb = list(sa.intersection(set3))
print("The common elements in the three lists are",sb)
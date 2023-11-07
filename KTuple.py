# Find maximum and minimum k elements in a tuple of numbers

t1 = (5,9,7,2,3,6,4,1,8)
t2 = sorted(t1)
t2r = list(reversed(t2))

k = int(input("Enter K "))
print("Maximum",k,"numbers ")
for i in range(k):
    print(t2[i],end=" ")

print("")
print("Minimum",k,"numbers ")
for i in range(k):
    print(t2r[i],end=" ")
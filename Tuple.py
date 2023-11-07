# Create a list of tuples from a given input input list having numbers, find its square and
# cube in subsequent tuples

n = input("Enter the numbers seperated by space: ")
l1 = n.split(" ")
for i in range(len(l1)):
    l1[i] = int(l1[i])
l2 = [(num, num**2, num**3) for num in l1]
print(l2)
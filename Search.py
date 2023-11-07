n = input("Enter the list elements seperated by space ")
li = n.split(" ")
e = input("Enter the element to be searched in the list ")
flag = False
for i in range(0,len(li)):
    if li[i] == e:
        flag = True
        break
if flag:
    print(e,"is found at position",i+1)
else:
    print(e,"is not found in the list")
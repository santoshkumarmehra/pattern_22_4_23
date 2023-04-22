num = input("enter odd number like: 12345 : ")
length = len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(num[i], end=" ")
        else:
            print(" ", end=' ')
    print()
# output
# 1       1 
#   2   2
#     3
#   4   4
# 5       5

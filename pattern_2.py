num = input("enter odd number like: 12345 : ")
length = len(num)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(num[j], end=" ")
        else:
            print(" ", end=' ')
    print()

# output
# 1       5 
#   2   4
#     3
#   2   4
# 1       5

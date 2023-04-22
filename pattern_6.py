num = int(input("enter number: "))
for i in range(num):
    k = 111
    k = k*(i+1)
    for j in range(num-i-1):
        print(format(" ", "<5"), end="")
    for j in range(i+1):
        print(format(k, "<5"), end="")
        k -= 111
    print()

# output
# enter number: 5
#                     111  
#                222  111
#           333  222  111
#      444  333  222  111  
# 555  444  333  222  111


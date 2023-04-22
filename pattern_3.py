num = int(input("enter number: "))
for i in range(num):
    k = 111
    for j in range(i+1):
        print(format(k, "<5"), end="")
        k += 111
    print()

# output
# enter number: 5
# 111  
# 111  222
# 111  222  333
# 111  222  333  444
# 111  222  333  444  555
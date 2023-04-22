num = int(input("enter number: "))
k = 111
for i in range(num):
    for j in range(i+1):
        print(format(k, "<5"), end="")
        k += 111
    print()

# output
# enter number: 5
# 111  
# 222  333  
# 444  555  666  
# 777  888  999  1110      
# 1221 1332 1443 1554 1665 

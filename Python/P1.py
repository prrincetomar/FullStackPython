n = int(input("Enter the value of n"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if  j <= n -  i and j >= 1:
            print(" * ", end = "")
        else:
            print(" ",end = "")
    print()

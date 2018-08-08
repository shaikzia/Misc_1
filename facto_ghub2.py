def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)


x = int(input('Enter the Number: '))
y = fact(x)

print("{}! = {}".format(x,y))
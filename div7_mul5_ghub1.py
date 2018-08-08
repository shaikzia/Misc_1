# Practice program 1
'''
Write a program which will find all such numbers
which are divisible by 7 but are not a multiple of
5 between 2000 and 2100 (both included). Print the
numbers in comma separated sequenc in a single line
'''

l = []
for i in range(2000, 2101):
    if (i%7 == 0) and (i%5 != 0):
        l.append(str(i))


print (','.join(l))
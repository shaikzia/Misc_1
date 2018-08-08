num = input('Enter any number: ')

val = int(num)
rev = str(num)[::-1]
if num == str(num)[::-1]:
    print('The given number is Palindrome')
else:
    print('The given number is NOT palindrome')

print(val)
print(rev)

# This is Function defined and used as a Generator
def square_nos(nums):
    for i in nums:
        yield (i*i)

my_nums = square_nos([1,2,3,4,5])

print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
for res in my_nums:
    print(res)

# # The same Function we can use in the List Comprehension
# lc = [x*x for x in [1,2,3,4,5]]
# print(lc)
#
# # When we use parenthes , then it becomes a Generator
# lc_gen = (x*x for x in [1,2,3,4,5])
# print(lc_gen)

def square(nums):
    for i in nums:
        yield i*i

d = square([1,2,3,4])
#print(next(d))
#print(next(d))
#print(next(d))
#print(next(d))

# this is same think we can do the yeild will hold only for 1 variable

for i in d:
    print('This is value',i)
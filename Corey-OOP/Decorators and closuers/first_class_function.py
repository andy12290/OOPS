# This is related to first class function.

def square(x):
    return x * x

f = square
print(square(2))
print(f(3))

#Desinged our own map function

def my_map(func, args_list):
    result = []
    for row in args_list:
        result.append(func(row))
    return result

sq = my_map(square,[1,2,3,4,5])
print(sq)


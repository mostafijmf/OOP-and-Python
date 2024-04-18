doubled = lambda num : num * 2
add = lambda a, b : a + b

# print(doubled(24))
# print(add(24, 50))

numbers = [10,10,20,20,30,30]
doubled_nums = map(doubled, numbers)

print(list(doubled_nums))


data = [
    {'name': 'A', 'age': 20},
    {'name': 'B', 'age': 19},
    {'name': 'C', 'age': 22},
    {'name': 'D', 'age': 24},
    {'name': 'E', 'age': 21},
    {'name': 'F', 'age': 23},
    {'name': 'G', 'age': 18},
    {'name': 'H', 'age': 19}
]

filter_data = filter(lambda d : d['age'] <= 20, data)
print(list(filter_data))
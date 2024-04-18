numbers = [41, 55, 62, 42, 60, 88, 90, 63, 35]
odd=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odd.append(num)

print(odd)

# Shortcut
odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)
numbers = [45, 55, 64, 25, 77, 36, 90, 10, 50]
print(numbers[3], numbers[-5])

# List (start : end)
print(numbers[1:7])

# List (start i-th index : end i-th index : step)
print(numbers[1:7: 1])
print(numbers[1:7: 2])
print(numbers[7:2: -1]) # reverse

# List (start i-th index : till the end default)
print(numbers[2:])
# List (start default : end i-th index)
print(numbers[:5])
# List (all)
print(numbers[:])
print(numbers[::-1]) # reverse
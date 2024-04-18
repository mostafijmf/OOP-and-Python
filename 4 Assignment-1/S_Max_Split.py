# s = LLRRLLLRRR
s = input()

count_L = 0
count_R = 0
new_strings = []
current_s = ''

for char in s:
    current_s += char
    if char == 'L':
        count_L += 1
    elif char == 'R':
        count_R += 1
    if count_L == count_R:
        new_strings.append(current_s)
        current_s = ''

print(len(new_strings))
for substring in new_strings:
    print(substring)
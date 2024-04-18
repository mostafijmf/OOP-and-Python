n = int(input())
val = list(map(int, input().split()))

i = 0
count = 0
stop = 0
while True:
    if i == n:
        i = 0
        count += 1
    if val[i] % 2 != 0:
        break
    val[i] = val[i] / 2
    i += 1

print(count)
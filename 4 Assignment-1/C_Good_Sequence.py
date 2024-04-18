n = int(input())
val = list(map(int, input().split()))

vis = {}
for i, v in enumerate(val):
    if v in vis.keys():
        vis[v] += 1
    else:
        vis[v] = 1

count = 0
for key, val in vis.items():
    # print(key, val)
    if key > val:
        count += val
    elif key < val:
        count += val - key


print(count)
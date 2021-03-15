# 위에서 아래로

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))


arr.sort(reverse=True)

for v in arr:
    print(v, end=' ')

arr = [v for v in arr if v > 19]
print(arr)

# 3
# 13
# 27
# 12

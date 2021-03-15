# 성적이 낮은 순서로 학생 출력하기

n = int(input())

arr = []

for _ in range(n):
    arr.append(input().split())

# 만약 내림차순으로 하고 싶다면 int(x[1]) 대신 -int(x[1]) 이렇게 사용
for v in sorted(arr, key=lambda x: int(x[1])):
    print(v[0], end=' ')

from collections import deque

def process(arr, x, y, n, m):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                
    return arr

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    for v in arr:
        print(v)
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt += 1
                arr = process(arr, i, j, n, m)
    print('answer :', cnt)



'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
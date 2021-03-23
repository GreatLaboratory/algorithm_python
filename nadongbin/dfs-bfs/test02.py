# 음료수 얼려 먹기

def solution(n, m, ice):
    def dfs(x, y):
        # 현재 방문하려는 노드가 범위에 벗어났다면 탈출
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

        # 구멍이 뚫려있다면(현재 방문한 노드가 0이면) 무조건 true를 반환함과 동시에
        if ice[x][y] == 0:
            # 해당 노드를 얼음인 1로 채우고
            ice[x][y] = 1

            # 상하좌우의 노드들을 방문하며 그 노드가 구멍이 뚫려있다면(그 노드가 0이었다면) 얼음(1)로 채운다.
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else:  # 이미 얼음(1)으로 채워져있다면 탈출
            return False

    answer = 0
    for i in range(n):
        for j in range(m):
            # 첫번째 노드인 (0, 0)을 방문했을 때 dfs(0, 0)의 수행이 끝나면 ice배열에서 (0,0), (0,1), (1,0), (1,1), (1,2)은 전부 1로 채워져 있다.
            if dfs(i, j) == True:
                answer += 1
    return answer


print(solution(4, 5, [[0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1],
                      [1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0]]))  # 3

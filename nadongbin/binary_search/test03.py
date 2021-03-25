# 떡볶이 만들기
import sys

n, m = map(int, input().split())
dduckList = list(set(map(int, sys.stdin.readline().rstrip().split())))

dduckList.sort(reverse=True)

longest = dduckList[0]
for i in range(longest, 0, -1):
    tmp = 0
    for dduck in dduckList:
        if dduck > i:
            tmp += (dduck-i)
            if tmp >= m:
                break
        else:
            break
    if tmp >= m:
        print(i)
        break

# 4 6
# 19 15 10 17


start = 0  # 절단기가 가질 수 있는 최솟값
end = max(dduckList)  # 절단기가 가질 수 있는 최댓값

answer = 0
while start <= end:
    mid = (start + end) // 2  # 중간값(절단기) 설정
    total = 0
    for dduck in dduckList:
        if dduck > mid:  # 중간값(절단기)보다 큰 떡만 찾아내어
            total += (dduck - mid)  # 합에 더한다.
    if total < m:
        # 자르고 난 뒤 합친 떡의 양이 부족할 경우 중간값을 왼쪽으로 하여 더 많이 자르기 (왼쪽 부분 탐색)
        end = mid - 1
    else:
        # 자르고 난 뒤 합친 떡의 양이 충분할 경우 중간값을 오른쪽으로 하여 더 조금 자르기 (오른쪽 부분 탐색)
        # 요청한 떡의 길이보다 큰 값을 찾자마자 반복을 종료하는 것이 아니라 계속 진행하여 절단기가 가질 수 있는 최댓값까지 반복한다.
        start = mid + 1
        answer = mid

print(answer)

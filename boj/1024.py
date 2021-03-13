'''
    수열의 합 (https://www.acmicpc.net/problem/1024)

    N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.
    첫째 줄에 N과 L이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.
    만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.
'''

# 순차탐색
n, l = map(int, input().split())

answer = []
while True:
    pivot = n//l
    if l % 2 == 0:
        if pivot - (l//2-1) < 0:
            break
        for i in range(1, l//2+1):
            answer.append(pivot+i)
            answer.append(pivot-(i-1))
            if len(answer) > 100:
                break
    else:
        if pivot - l//2 < 0:
            break
        answer.append(pivot)
        for i in range(1, l//2+1):
            answer.append(pivot+i)
            answer.append(pivot-i)
            if len(answer) > 100:
                break
    if len(answer) > 100 or n == sum(answer):
        break
    answer = []
    l += 1

if len(answer) > 100 or len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for v in answer:
        print(v, end=' ')

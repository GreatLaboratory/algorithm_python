# 124 나라의 숫자
from itertools import product


def solution1(n):  # 시간 초과...
    data = ['1', '2', '4']
    if n <= 3:
        return data[n-1]
    length = 0
    cnt = 0
    combiResult = []
    while length < n:
        cnt += 1
        combiResult = list(product(data, repeat=cnt))
        length += len(combiResult)
    result = combiResult[n + len(combiResult) - length - 1]
    return ''.join([v for v in result])


def solution2(n):  # 반례를 전부 커버하지 못함.
    if n == 1 or n == 2:
        return str(n)
    if n == 3:
        return '4'
    answer = []
    while True:
        key = n % 3
        answer.append(str(key))
        n //= 3
        if n == 0:
            break
    print(answer)
    for i, v in enumerate(answer):
        if v == '0':
            if i == len(answer)-1:
                answer = answer[:-1]
            else:
                answer[i] = '4'
                answer[i+1] = str(int(answer[i+1])-1)

    print(answer)
    return ''.join(list(reversed(answer)))


def solution3(n):  # 성공
    numbers = ['4', '1', '2']
    answer = ''
    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer


print(solution3(12))
print(solution3(15))
print(solution3(17))
print(solution3(20))
print(solution3(21))
print(solution3(30))

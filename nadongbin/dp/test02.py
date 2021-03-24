# 1로 만들기

def solution1(n):  # 틀린 풀이
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 5 == 0:
            n //= 5
        elif n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1
    return cnt


print(solution1(26))  # 3이 아닌 5가 나온다.


# f(26)은 f(25), f(13) 중에 가장 작은 값에 1을 더한 값이다.
# 다시 말해, 구하려는 f(n)은 f(n-1), f(n//5), f(n//3), f(n//2) 중 가능한 값들 중 최솟값에서 1을 더한 값이 된다. (총 연산의 횟수를 최소로 해야하므로)
# 1을 더하는건 연산횟수를 증가시키는 것이다.
# f(26)을 구할 때 사용하는 f(25)와 f(50)을 구할 때 사용하는 f(25)는 항상 같은 값을 갖기에 다이나믹 프로그래밍이 가능하다.
def solution2(x):  # 옳은 풀이
    d = [0] * 30

    # 매 반복마다 각 숫자의 1로 가는 연산 최솟값이 정해진다.
    for i in range(2, x+1):
        # ex) 만약 i가 30이라 f(30)구한다면
        d[i] = d[i-1] + 1  # 1을 빼는 연산은 항상 가능하므로 최초의 d[i]후보는 f(29)가 된다.
        # 30은 5로 나누어 떨어지므로 [f(29)+1, f(6)+1] 중 가장 작은 것을 택한다.
        if d[i] % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
        # 30은 3으로 나누어 떨어지므로 [f(29)+1, f(6)+1, f(10)+1] 중 가장 작은 것을 택한다.
        if d[i] % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        # 30은 2로 나누어 떨어지므로 [f(29)+1, f(6)+1, f(10)+1, f(15)+1] 중 가장 작은 것을 택한다.
        if d[i] % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
    return d[x]


print(solution2(26))  # 3

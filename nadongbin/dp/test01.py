def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(6))  # 8


def fibonacci_recursive_dp(n):
    dp_table = [0] * (n+1)
    if n == 1 or n == 2:
        return 1
    if dp_table[n] == 0:  # 한 번도 하지 않았던 연산이라면
        # 연산을 한다.
        dp_table[n] = fibonacci_recursive_dp(n-1) + fibonacci_recursive_dp(n-2)

    # dp_table[n]에 0이 아닌 수가 이미 들어와있다면 연산이 이미 수행되었으므로
    # fibonacci_recursive_dp(n-1) + fibonacci_recursive_dp(n-2)연산을 다시 하지 않는다.
    return dp_table[n]


print(fibonacci_recursive_dp(6))  # 8


def fibonacci_iterative_dp(n):
    dp_table = [0] * (n+1)
    dp_table[1], dp_table[2] = 1, 1

    # 세번째, 네번째 ... 낮은 인덱스부터 최종 구하려는 인덱스까지 순서대로 값이 정해져서 바텀업
    for i in range(3, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    # dp_table[n]은 위 반복문의 가장 마지막 순회에서 구해지므로 시간 복잡도는 탑다운과 마찬가지로 O(N)이다.
    return dp_table[n]


print(fibonacci_iterative_dp(6))  # 8

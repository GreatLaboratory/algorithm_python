def solution(L):
    numList = L[1]
    M = L[0][0]
    K = L[0][1]

    numList.sort()
    iterableGroup = (M // (K + 1)) * (K * numList[-1] + numList[-2])
    restGroup = (M % (K + 1)) * numList[-1]

    return iterableGroup + restGroup


print(solution([[8, 3], [2, 4, 5, 4, 6]]))  # 46 = 6+6+6+5+6+6+6+5
print(solution([[7, 2], [3, 4, 3, 4, 3]]))  # 28 = 4+4+4+4+4+4+4

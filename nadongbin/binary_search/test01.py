# 재귀적으로 이진탐색 구현
def recursive_binary_search(arr, target, start, end):
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[start] <= target and target < arr[mid]:
        return recursive_binary_search(arr, target, start, mid-1)
    elif arr[mid] < target and target <= arr[end]:
        return recursive_binary_search(arr, target, mid+1, end)
    else:
        return None


print(recursive_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 7, 0, 9))
print(recursive_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 6, 0, 9))
print(recursive_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 66, 0, 9))


# 반복적으로 이진탐색 구현
def iterative_binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[start] <= target and target < arr[mid]:
            end = mid - 1
        elif arr[mid] < target and target <= arr[end]:
            start = mid + 1
        else:
            return None


print(iterative_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 7))
print(iterative_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 6))
print(iterative_binary_search([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 66))


# 순차 탐색
def searchIndex(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return None


print(searchIndex([1, 3, 5, 7, 9, 11, 13, 15], 5))  # 2
print(searchIndex([1, 3, 5, 7, 9, 11, 13, 15], 12))  # None

# 부품 찾기
import sys

n = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

arr1.sort()


def binary_search(arr, target):
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


for v in arr2:
    if binary_search(arr1, v):
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9

arr1 = set(arr1)

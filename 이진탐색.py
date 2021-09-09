def binarysearch(a, target, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    if a[mid] == target:
        return mid
    elif a[mid] > target:
        return binarysearch(a, target, left, mid - 1)
    else:
        return binarysearch(a, target, mid + 1, right)

## n:원소의 개수, target: 찾는 값
n, target = list(map(int, input().split()))

a = list(map(int, input().split()))
result = binarysearch(a, target, 0, n-1)
if result == None:
    print("찾는 값이 존재하지 않음")
else:
    print("인덱스: ", result + 1)

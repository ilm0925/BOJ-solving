def down_search(n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] >= n:
            end = mid - 1
        elif arr[mid] < n:
            start = mid + 1
    return start


def up_serach(n):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] > n:
            end = mid - 1
        elif arr[mid] <= n:
            start = mid + 1
    return start


input()
arr = list(map(int,input().split(" ")))
arr.sort()
input()
serach_arr = list(map(int,input().split(" ")))

for i in serach_arr:
    print(up_serach(i))
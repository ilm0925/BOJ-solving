def binary_search(arr,n,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return binary_search(arr,n,start,mid - 1)
    else:
        return binary_search(arr,n,mid + 1, end)
x = int(input())

arr = list(map(int, input().split(" ")))
arr.sort()

input()
serach_arr = list(map(int, input().split()))

for i in serach_arr:
    search = binary_search(arr,i,0 ,x - 1)
    if search == None:
        print(0)
    else:
        print(1)

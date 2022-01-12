N, M = map(int,input().split(" "))

trees = list(map(int,input().split(" ")))


start = 0
end = max(trees)

result = 0


while start <= end:
    s = 0
    mid = (start+end)//2
    for i in trees:
        if i > mid:
            s += i - mid
    if s >= M: #떡의 개수가 M보다 크다면 높이가 낮다는거니까 높이를 올려줌
        start = mid + 1
    else:
        end = mid - 1
    
print(end)

        

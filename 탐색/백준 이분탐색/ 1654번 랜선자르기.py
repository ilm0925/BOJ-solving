K , N = map(int,input().split(" "))

cable = [int(input()) for _ in range(K)]
start = 1
end = max(cable)



while start <= end:
    s = 0
    mid = (start+end)//2
    for i in cable:
        s += i//mid
    if s >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
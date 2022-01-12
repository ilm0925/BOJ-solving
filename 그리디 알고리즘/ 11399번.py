input()

arr = list(map(int, input().split(' ')))
arr.sort()
sum = 0
temp = 0

for i in range(len(arr)):
    sum += arr[i]
    temp += sum

print(temp)

#https://fast-it.tistory.com/32
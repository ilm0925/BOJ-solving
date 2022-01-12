arr = input().split('-') #50-30+50
sum = 0 
#arr = 50 , 30+50
for x in arr[0].split("+"): #50
    sum += int(x) #sum += 30

#만약에 모든수가 덧셈이면 이 부분을 수행하지않는다 배열의 길이는 0이니까
for i in arr[1:]: #30+50
    for j in i.split("+"):#for문 돌려가며 30빼주고 50빼주고 
        sum -= int(j)
        
print(sum)


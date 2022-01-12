case = int(input())
times = []
count = 1 #한개의 회의는 무조건 할수있으니까 1부터시작 

for i in range(case):
    time = list(map(int,input().split(' ')))
    times.append(time)

times.sort(key = lambda x: (x[1], x[0])) #끝나는시간으로 오름차순정렬 배열안에 배열이 들어있음

endTime = times[0][1] #정렬하고 나서 첫 회의의 끝나는 시간 

for T in range(1,len(times)): #두번째 회의부터 마지막 회의까지
    st = times[T][0] #시작시간
    et = times[T][1] #끝나는 시간
    if st >= endTime: #endTime보다 크거나 같으면 겹치지않는 회의라는거니까
        count += 1 #회의의 갯수 하나 올려줍니다
        endTime = et 
print(count)
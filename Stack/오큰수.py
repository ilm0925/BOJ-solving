
n = int(input()) #4
arr = list(map(int, input().split())) # 3 2 4 5

Oken = [-1] * n #[-1 -1 -1 -1]
stack = [0] #1부터 시작해야해서 처음엔 0



for i in range(1,len(arr)): #stack에 0들어있어서 1부터시작
    if arr[i] > arr[stack[-1]] and stack:  # 2는 3보다 작으니까 스택에 추가  4에서 While 문 시작
        while(stack): #Stack이 빌때까지 수행함 stack = [0 ,1]
            if arr[stack[-1]] < arr[i] :  #2와3은 4보다 작으니 2와 3의 오큰수는 4
                Oken[stack.pop()] = arr[i] #스택에 인덱스를 넣은 이유는 이렇게 오큰수에 자리를 맞추기 위함
            else: 
                break #3이아니라 6같은 수가 들어왔을때는 브레이크를 먹여서 -1 그대로 나둠 오큰수가 없다는거니까
        stack.append(i) #4도 넣어줌 > 반복
    else:
        stack.append(i) #작으면 스택에 index를 넣어줌 
print(*Oken) #4 4 5 -1
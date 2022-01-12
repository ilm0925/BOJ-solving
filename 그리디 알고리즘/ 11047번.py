
case , money = map(int , input().split(' ')) #case는 동전의 종류 money는 우리가 만들어야할 돈
coin = [] #동전들을 담을 배열
temp = count = 0

for i in range(case):
    user_coin = int(input())
    coin.append(user_coin)

for m in reversed(coin): #입력은 오름차순으로 입력된다했죠 근데 최소값을 구하라고하니까 뒤집어서 큰 동전부터 검사합니다
    temp = money//m  #만약에 돈이 5300원이고 동전이 2000원이면 2번 뽑아줄수있죠
    count += temp #동전으로 돈을 나눈 몫을 count에 담아줍니다
    money %= m #돈을 뽑을수있는대로 뽑아줬으면 돈을 동전으로 나눈 나머지로 치환해줍니다

print(count)


n = int(input())

road = list(map(int , input().split(" ")))
price = list(map(int , input().split(" ")))
del price[len(price)- 1]
minprice = min(price)
pricesum = 0

for i in range(n - 1):
    if price[i] == minprice:
        pricesum += price[i]*sum(road[i:])
        break
    else:
        pricesum += price[i]*road[i]

print(pricesum)

#배점 17점 30분

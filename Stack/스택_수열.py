n = int(input())

answer = list()
stack = list()
state = True
i = 0
for _ in range(n):
    num = int(input())
    while i < num:
        i += 1
        stack.append(i)
        answer.append("+")
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        state = False


if state:
    for i in answer:
        print(i)
else:
    print("NO")

# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
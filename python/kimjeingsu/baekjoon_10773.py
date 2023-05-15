# https://www.acmicpc.net/status?user_id=wjdtn8536&problem_id=10773&from_mine=1

stack = []
for i in range(int(input())):
    m = int(input())
    if m==0:
        stack.pop()
    else:
        stack.append(m)

print(sum(stack))


# 시간 3880ms
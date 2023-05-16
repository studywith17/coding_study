# https://www.acmicpc.net/problem/18258

from collections import deque
import sys

n = int(input())
deque_list = deque([])

for i in range(n):
    what = sys.stdin.readline().split()

    if what[0] == 'push':
        deque_list.append(what[1])

    elif what[0] == 'pop':
        if not deque_list:
            print(-1)
        else:
            print(deque_list.popleft())
    elif what[0] == 'size':
        print(len(deque_list))
    elif what[0] == 'empty':
        if not deque_list:
            print(1)
        else:
            print(0)
    elif what[0] == 'front':
        if not deque_list:
            print(-1)
        else:
            print(deque_list[0])
    elif what[0] == 'back':
        if not deque_list:
            print(-1)
        else:
            print(deque_list[-1])


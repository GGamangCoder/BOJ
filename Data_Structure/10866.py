import sys, collections
input = sys.stdin.readline

N = int(input())

deq = collections.deque()
for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif cmd[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
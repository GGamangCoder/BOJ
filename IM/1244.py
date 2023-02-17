# 스위치 켜고 끄기

N = int(input())        # 스위치 갯수 <= 100
lights = list(map(int, input().split()))
num = int(input())      # 사람 숫자
for _ in range(num):
    sex, number = map(int, input().split())
    if sex == 1:        # 남학생
        for i in range(number-1, N, number):       # number의 배수
            if lights[i] == 1:
                lights[i] = 0
            elif lights[i] == 0:
                lights[i] = 1
    else:               # 여학생
        idx = 0
        number -= 1             # 인덱스 맞춰주기 위해
        while (number + idx < N) or (number - idx > 0):
            if lights[number-idx] == lights[number+idx]:    # 양 옆 같으면
                idx += 1        # 증가시키고 비교하게 됨!
                continue
            else:               # 만약 다르면 그만!
                break
        idx -= 1                # 인덱스 맞춰주기
        for i in range(number - idx, number + idx + 1):
            if lights[i] == 1:
                lights[i] = 0
            elif lights[i] == 0:
                lights[i] = 1

for i in range(1, N + 1):
    if i % 20 == 0:  # 20개마다 줄바꿈
        print(lights[i - 1])
    else:
        print(lights[i - 1], end=" ")
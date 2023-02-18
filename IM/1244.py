# 스위치 켜고 끄기

def change(num):
    if lights[num] == 0:
        lights[num] = 1
    else:
        lights[num] = 0
    return

N = int(input())        # 스위치 갯수 <= 100
# 인덱스와 번호를 일치시켜주기 위해서 0번에 -1
lights = [-1] + list(map(int, input().split()))
num = int(input())      # 사람 숫자
for _ in range(num):
    sex, number = map(int, input().split())
    if sex == 1:        # 남학생
        for i in range(number, N+1, number):       # number의 배수
            change(i)
    else:               # 여학생
        change(number)
        for idx in range(N//2):
            # 범위 넘어가면,
            if number + idx > N or number - idx < 1:
                break
            
            # 대칭적으로 같으면 뒤집어주기
            if lights[number + idx] == lights[number - idx]:
                change(number + idx)
                change(number - idx)
            else:
                break        
        
        # 처음 풀이
        # number -= 1             # 인덱스 맞춰주기 위해
        # while (number + idx < N) or (number - idx > 0):
        #     if lights[number-idx] == lights[number+idx]:    # 양 옆 같으면
        #         idx += 1        # 증가시키고 비교하게 됨!
        #         continue
        #     else:               # 만약 다르면 그만!
        #         break
        # idx -= 1                # 인덱스 맞춰주기
        # for i in range(number - idx, number + idx + 1):
        #     change(i)

for i in range(1, N + 1):
    print(lights[i], end=" ")
    if i % 20 == 0:  # 20개마다 줄바꿈
        print()
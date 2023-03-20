# 소수 & 팰린드롬

N = int(input())

def isPalindrome(num):
    word = str(num)
    return word == word[::-1]

# 몰라 걍 틀림
# def find_prime(num):
#     n = 2
#     while num <= 1000000:
#         # 나눠떨어질 때까지 나눠서 소수 찾기
#         if num % n != 0:
#             n += 1
#         # 절반까지 넘어서 안 나눠지면 그건 소수
#         elif n >= num // 2:
#             if palindrome(num):
#                 return num
#             else:
#                 num += 1
#                 n = 2
#         # n이 절반보다 작고 나누어 떨어지면 num+1 후에 다시 시작
#         else:
#             num += 1
#             n = 2

def isPrime(num):
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

# 10^6 에 대해서 반례가 존재
# ans = 0
# for i in range(N, 1000001):
#     if i == 1:      # 예외처리
#         continue
    
#     if isPrime(i) and isPalindrome(i):
#         ans = i
#         break

i = N
while True:
    if i == 1:
        i += 1
        continue
    
    if isPrime(i) and isPalindrome(i):
        ans = i
        break

    i += 1

print(ans)

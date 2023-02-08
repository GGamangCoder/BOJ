T = int(input())
def big(cnt):
    ans = '7' * (cnt%2) + '1' * (cnt//2 - cnt%2)
    return ans

def small(cnt):
    # ans = ''
    # while cnt > 0:
    #     if cnt % 7
    #     if cnt >= 7:
    #         ans = '8' + ans
    #         cnt -= 7
    #     elif cnt == 6:
    #         ans = '6' + ans
    #         cnt -= 6
    #     elif cnt == 5:
    #         ans = '5' + ans
    #         cnt -= 6
    #     elif cnt == 4:
    #         ans = '6' + ans
    #         cnt -= 6
    #     elif cnt == 3:


    pass



for tc in range(1, T + 1):
    N = int(input())

    print(f'{small(N)} {big(N)}')

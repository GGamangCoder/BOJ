def big(cnt):
    ans = '7' * (cnt%2) + '1' * (cnt//2 - cnt%2)
    return ans

def small(cnt):
    ans = ''
    digit_list = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    if 2 <= cnt <= 10:
        ans += str(digit_list[cnt])
        return ans
    while cnt > 7:
            cnt -= 7
            ans += '8'
    if cnt == 1:
        ans = '10' + ans[1:]
    elif cnt == 3:
        ans = '200' + ans[2:]
    elif cnt == 4:
        ans = '20' + ans[1:]
    else:   # 2, 5, 6, 7
        ans = str(digit_list[cnt]) + ans
    return ans

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'{small(N)} {big(N)}')
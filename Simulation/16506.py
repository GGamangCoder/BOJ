# 0 ~ 4 opcode(연산) / 5 = 0 / 6 7 8 - rD / 9~ 11 rA _ 000(mov,movc,not)
# 12~14,15 rB + 0 / #C
            # 16 비트 연산
# ex - opcode rD rA rB / opcode rD(결과저장) rA #C
# 레지스터 rA, rB / 상수 #C



def assembly(input_):
    opcode, rD, rA, rB = input_
    trans = ''
    if opcode in 'ADDC':
        trans += '0000'
    elif opcode in 'SUBC':
        trans += '0001'
    elif opcode in 'MOVC':
        trans += '0010'
    elif opcode in 'ANDC':
        trans += '0011'
    elif opcode in 'ORC':
        trans += '0100'
    elif opcode in 'NOT':
        trans += '0101'
    elif opcode in 'MULTC':
        trans += '0110'
    elif opcode in 'LSFTLC':
        trans += '0111'
    elif opcode in 'LSFTRC':
        trans += '1000'
    elif opcode in 'ASFTRC':
        trans += '1001'
    elif opcode in 'RLC':
        trans += '1010'
    elif opcode in 'RRC':
        trans += '1011'
    
    if 'C' in opcode:
        trans += '10'
    else:
        trans += '00'

    rD = bin(int(rD))[2:]               # 이진수 변환
    rD = (3 - len(rD)) * '0' + rD       # 자릿수 맞춰주기
    trans += rD
    rA = bin(int(rA))[2:]               # 이진수 변환
    rA = (3 - len(rA)) * '0' + rA       # 자릿수 맞춰주기
    trans += rA

    rB = bin(int(rB))[2:]
    if 'C' in opcode:
        rB = (4 - len(rB)) * '0' + rB
        trans += rB
    else:
        rB = (3 - len(rB)) * '0' + rB + '0'
        trans += rB
    
    return trans

N = int(input())        # 명령어 갯수
res = []
for _ in range(N):
    cmd = input().split()
    res.append(assembly(cmd))

print('\n'.join(res))

"""
접근 방법 :deque에 저장 후 rotate

메모리 : 19032kb, 시간 : 136ms
"""


import sys
sys.stdin = open('input.in', 'r')


from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    # 숫자의 개수와 크기
    locker = deque(input())
    n = N//4 # 패턴의 개수 확인

    tmp = []
    for turn in range(n):
        locker.rotate()
        for i in range(0,N,n): # n개씩 묶어서 저장
            check = ''
            for j in range(n):
                check += locker[i+j]
            if check not in tmp:
                tmp.append(check)
    #16진수 형변환
    length_tmp = len(tmp)
    for s in range(length_tmp):
        tmp[s] = int(tmp[s],16)

    # 내림차순 정렬
    tmp.sort(reverse=True)
    if length_tmp >= K-1:
        print(f'#{tc} {tmp[K-1]}')

    else:
        index = (K-1) % length_tmp

        print(f'#{tc} {tmp[index]}')


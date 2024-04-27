import sys
sys.stdin = open('Sample_input.txt','r')

'''
14510. 나무 높이
133 ms
48,984 kb
'''


T = int(input())
for tc in range(T):
    N = int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    h_lim = arr.pop()
    day=0
    while 1:
        arr.sort()
        while arr and arr[-1]==h_lim:
            arr.pop()
        if not arr:
            break
        day+=1
        if day%2==0:                                # 짝수인 날
            if arr[-1]+2==h_lim:                    # 가장 큰 나무 +2 했을 때 최대 높이면
                arr[-1] += 2                        # 가장 큰 나무 성장 종료
            elif arr[0]+2<=h_lim:                   # 아니면
                arr[0] += 2                         # 가장 작은 나무에 +2
        else:                                       # 홀수인 날
            if arr[-1]+1==h_lim:                    # 가장 큰 나무 +2 했을 때 최대 높이면
                arr[-1] += 1                        # 가장 큰 나무 성장 종료
            elif len(arr)<3 and arr[0]+2==h_lim:    # 남은 나무가 2개 이하 and 가장 작은거 +2가 최대 높이
                continue                            # 다음날에 2를 더함으로 한번에 끝 낼 수 있게한다
            elif arr[-1]+2==h_lim and len(arr)!=1:  # 남은 나무가 두개 이상이고 가장 큰 거 +2가 최대 높이
                arr[0]+=1                           # 이 때는 작은거에 1 더해도 됨
            elif arr[-1]+1<=h_lim:                  # 가장 큰 높이에 1 더해도 되면
                arr[-1] += 1
    print(f'#{tc+1} {day}')

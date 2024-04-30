import sys
sys.stdin = open('sample_input.txt','r')


# swea_1952_수영장
# 메모리 : 44,724 kb
# 실행시간 : 105 ms


T = int(input())
for tc in range(T):
    d1,m1,m3,y1 = map(int,input().split())
    arr = list(map(int,input().split()))
    dp=[0]*12
    dp[0]=min(d1*arr[0],m1)             # 1월은 일권 or 월권
    dp[1]=dp[0]+min(d1*arr[1],m1)       # 2월도 동일
    for i in range(2,12):               # 3월부터는 직전달 + (일권 or 월권) or 세달전 + 세달권 중 min값
        dp[i]=min(dp[i-1]+d1*arr[i],dp[i-1]+m1,dp[i-3]+m3)     # i-3이 없는 인덱스인 i=2일때(3월)는 dp[-1]은 0이라 무관!
    print(f'#{tc+1} {min(dp[11], y1)}')
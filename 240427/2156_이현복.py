import sys
sys.stdin = open('sample_input.txt','r')

'''
2156_포도주 시식
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
dp=[0]*N
dp[0]=arr[0]
if N>1:                     # 주어진 N의 범위는 (1 ≤ n ≤ 10,000) 이므로
    dp[1]=arr[0]+arr[1]
if N>2:
    dp[2]=max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,N):
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i],dp[i-1])
print(dp[N-1])

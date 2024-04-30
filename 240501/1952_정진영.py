T = int(input())
for tc in range(1,T+1):
    membership = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    dp = [0] * 12

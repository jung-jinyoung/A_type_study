"""
접근 방법 : DP

매달 접근 -> 1일권, 1달권을 각각 선택한 경우와 비교하여 저장한다.

3월 이하일 때는 3달권 가격만, 이상일 때는 dp[i-3]+3달권 가격과 비교

마지막 1년권과 비교하여 가장 적게 지출하는 비용을 출력한다.

메모리 : 15252 KB
시간 : 100ms

"""





T = int(input())
for tc in range(1,T+1):
    # 인덱스 순서대로 1일권, 1달권, 3달권, 1년권의 가격
    membership = list(map(int,input().split()))
    # 이용 계획
    plan = [0]+list(map(int,input().split()))

    dp = [0]*13 #dp 생성

    for i in range(1,13):
        # 1일권 결제
        day = membership[0] * plan[i]
        # 1달권 결제
        month = membership[1]
        # 3달권 결제
        if i <3:
            three_month = membership[2]
        else:
            three_month = dp[i-3]+membership[2]

        tmp1 = min(day,month) + dp[i-1] # 3달권 결제하기 전 가격
        dp[i] = min(tmp1,three_month) # 모두 비교

    print(f'#{tc} {min(dp[12],membership[3])}') # 1년권 가격과 비교







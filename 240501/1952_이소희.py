'''
메모리 | 52,760 kb
실행시간 | 216 ms
코드길이 | 669
'''
def cost(i, fee):
    global priceTable, minFee
    if i >= 12:
        minFee = min(minFee, fee)
        return
    if fee > minFee:
        return
    
    # 1. 1년치 금액 전부 내기
    cost(i + 12, fee + priceTable[3])
    # 2. 세달치 금액 내기
    if plan[i]:
        cost(i + 3, fee + priceTable[2])
    else:
        cost(i + 1, fee)
    # 3. 한달치 금액 내기
    cost(i + 1, fee + priceTable[1])
    # 4. 일일권
    cost(i + 1, fee + (priceTable[0] * plan[i]) )

T = int(input())
for tc in range(1, T+1):
    priceTable = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    minFee = int(1e9)

    cost(0,0)
    print(f'#{tc} {minFee}')
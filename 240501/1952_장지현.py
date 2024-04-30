'''
지현_1952.수영장

54,632 kb
211 ms

---

1일권 A
한달권 B
세달권 C     -- 10월까지만 계산
일년권 D     -- 1월에 계산하고 끝

1 2 3 4 5 6 7 8 9 10 11 12 (월)  >> 총 idx = 12
D                               >> (idx + 11, 종료)
C     NEW  >> (idx+3, 재귀) w/ 이전값 + (세달권)
B NEW >> (idx+1, 재귀) w/ 이전값 + (한달권)
A NEW >> (idx+1, 재귀) w/ 이전값 + (1일권) * (이용 일수)


처음 생각을 못해낸 이유 )) .. 게을러서 ?
-- 범위를 좀 유연하게 잡아보기 !
'''

def swim(mon, exp):
    global min_exp

    # 종료조건
    if mon > 12:
        if min_exp > exp:
            min_exp = exp
        return
        
    # dfs

    # for idx in range(12):
    ### > days 순회할 필요 x

    # exp는 지금까지 더해온 값
    # 일년권
    swim(mon+12, exp + year)
    
    # 세달권
    swim(mon+3, exp + month3)

    # 한달권
    swim(mon+1, exp + month1)
    ## 해당 월에 사용 일수 0일때 if 처리도 해줘야하나? > 아님
    ## 그런 경우는 days[mon] == 0으로 알아서 처리될 듯

    # 일일권
    swim(mon+1, exp + day*days[mon])



T = int(input())

for tc in range(1, T+1):
    day, month1, month3, year = map(int, input().split())
    days = [0] + list(map(int, input().split()))

    min_exp = 10000000  # > 3000 * 365

    swim(1, 0)
    print(f"#{tc} {min_exp}")

'''
처음 접근 방법)
월 하나하나마다 조건을 계산하고 넘어가려고 했음
ex) 4월 > 1일권 * 4월 날짜
        > 한달권 * 1    >> 이 둘 중 min 구해서 넘어가고 --- greedy?
        > 세달권 ???? 여기서 막힘 --- 앞 조건들을 가져와서 cnt에 넣는 등 ,, 시도 ,, 실패
'''
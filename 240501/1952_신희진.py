def dfs(m, t_mon):
    global res
    # 인덱스 11 > 12월
    # 12월을 넘으면 조건을 비교하고, return해줌
    if m > 11:
        if res > t_mon:
            res = t_mon
        return res
    # 하루 > 하루 가격 *이용 일수를 총 돈에 더해주고 다음달로 넘어감
    dfs(m + 1, t_mon + use[m] * day)
    # 한달 > 한달 가격을 총 돈에 더해주고 다음달로 넘어감
    dfs(m + 1, t_mon + mon)
    # 3달 > 3달 가격을 총돈에 더해주고 3달 후로 넘어감
    dfs(m + 3, t_mon + mon3)
    # 1년 가격이 res에 할당되어 있어서 1년은 따로 할 필요 없음


T = int(input())
for tc in range(T):
    # 하루, 한달, 세달, 1년 별 가격
    day, mon, mon3, year = map(int, input().split())
    # 나의 사용 일수
    use = list(map(int, input().split()))
    # 최종 값을 1년단위로 생성해둠
    res = year
    # 0(1월), 0(0원으로 시작)
    dfs(0, 0)
    print(f'#{tc + 1}', res)
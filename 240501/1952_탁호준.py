def make_min_cost(m, cost):# 달, 요금
    global min_cost
    if min_cost < cost:
        return
    if m >= 12:
        min_cost = min(min_cost, cost)
        return
    
    make_min_cost(m+1, cost+day*schedule[m])
    make_min_cost(m+1, cost+one)
    make_min_cost(m+3, cost+three)

T = int(input())
for tc in range(1, T+1):
    day, one, three, year = map(int,input().split())
    schedule = list(map(int, input().split()))

    min_cost = year
    make_min_cost(0, 0)
    print(f'#{tc} {min_cost}')
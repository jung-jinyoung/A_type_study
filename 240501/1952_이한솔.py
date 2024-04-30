# 수영장

'''
1일 이용권 : 1일 이용 가능, 10원
1달 이용권 : 매달 1일 시작, 40원 
3달 이용권 : 매달 1일 시작, 당 해에만 이어서 사용 가능, 100원
1년 이용권 : 매년 1월 1일 시작, 1년 동안 이용, 300원

가장 저렴하게 이용할 수 있는 방법의 비용

모든 경우의 수를 탐색하는 방법으로, 완전 탐색을 이용해야 하는 줄 알았는데
dfs 로 풀어야 할 것 같다고 생각함

예시 ) 1월에 1일권을 사용하는 경우, 1달권을 사용하는 경우, 
3달권을 사용하는 경우, 1년권을 사용하는 경우를 모두 탐색

메모리 : 52,492 kb  실행시간 : 422 ms
'''

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int,input().split())
    plan = list(map(int,input().split()))
    result = 10000000000

    def dfs(month,sum):
        global result
        if month > 11:
            if result > sum:
                result = sum
            return
        
        dfs(month+1, sum + plan[month]*day)
        dfs(month+1, sum + mon)
        dfs(month+3, sum + mon3)
        dfs(month+12, sum + year)

    dfs(0,0)
    print(f'#{tc} {result}')
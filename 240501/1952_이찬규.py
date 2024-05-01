'''
1952. 수영장

1일 이용권: 1일 이용 가능
1달 이용권: 1달 동안 이용 가능, 1달 이용권은 매달 1일부터 시작
3달 이용권 : 연속된 3달 동안 이용이 가능. 3달은 매달 1일부터 시작
1년 이용권 : 1년 동안 이용 가능, 매년 1월 1일부터 시작

이용 계획은 해당 달에 수영장을 이용할 날수

각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라
'''


# 수영장을 이요하는 최소 비용을 계산하는 함수 cost
# 매개 변수 cost는 새로 이용권을 구매해야하는 월, sub_cost는 현재까지 비용의 구간합
def cost(month, sub_cost):
    # 글로벌 변수 min_cost를 호출
    global min_cost
    # 만약 month가 배열의 인덱스를 넘어섰다면 min_cost와 비교하여 min_cost보다 값이 작으면 min_cost를 갱신
    if month >= 12:
        if min_cost > sub_cost:
            min_cost = sub_cost
        return

    # 만약 현재 월에 이용 계획이 없다면 다음 달로 넘어감
    if plan[month] == 0:
        cost(month+1, sub_cost)
        return

    # 위의 조건에 걸리지 않을 경우, 일 이용권, 월 이용권, 3달 이용권을 구매하고 재귀를 통해 반복
    cost(month+1, sub_cost+plan[month]*fee[0])
    cost(month+1, sub_cost+fee[1])
    cost(month+3, sub_cost+fee[2])


T = int(input())
# 각 테스트케이스별 시행
for tc in range(1, T+1):
    # 앞에서부터 순서대로 일, 월, 3달, 연별 이용권 금액을 담고 있는 리스트 fee
    fee = list(map(int, input().split()))
    # 월별 이용 계획을 담고 있는 리스트 plan
    plan = list(map(int, input().split()))
    # 최소 비용을 저장할 변수 min_cost, 초기값은 연 이용권의 비용
    min_cost = fee[3]
    # 함수를 호출하고 첫째달부터 시작, plan에 인덱스로 접근하기 위해, 매개변수 month는 0, 초기 구간합은 0
    cost(0, 0)
    # 갱신된 min_cost 값을 출력 양식에 맞게 출력
    print(f'#{tc} {min_cost}')
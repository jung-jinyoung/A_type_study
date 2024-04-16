"""
<입력>
가장 첫 줄에는 테스트 케이스의 총 수가 주어진다.
그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 2줄로 구성된다.
각 테스트 케이스의 첫째 줄에는 나무의 개수 N이 주어진다.
다음 줄에는 나무들의 높이가 N개의 자연수로 주어진다.


-----------------
물 주기:
    짝수 날(2) / 홀수 날 (1) // 안 줄 수 있음

모든 나무의 높이가 처음에 가장 큰 나무의 높이가 될 수 있을 대의 최소 날짜의 수를 계산하시오.

접근 방법:
    1. 나무 높이 오름차순 정렬
    2. 물을 안 주는 경우의 수를 최대한 없애는 방법  : 최대한 물을 주는 방법 생각
        1. 현재 가장 작은 나무와 높은 나무를 찾기
        2. 현재 날짜 짝/홀 계산
        3. 가장 높은 나무 부터 높이 차 계산 : 짝/홀 계산 -> 줄 수 있으면 주고 넘어가기
        4. 가장 높은 나무에 줄 수 없으면 가장 작은 나무에 물 주기
        5. 나무 높이 정렬
        5. 인덱스 비교 : target height에 도달했을 경우 인덱스 이동 => L, R 재설정
        6. 1~5 과정 반복
        7. L,R 이 같을 때, 즉 하나의 값만 비교해야 할 경우 조건으로 추가
        8. 정렬 후 index == 0 의 높이가 target height 에 도달햇을 경우 while 문 break

메모리 : 49,052 kb
실행 시간 : 140 ms


"""


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))


    # 목표 나무 높이
    target_height = max(trees)

    # 비교 해야 하는 나무 설정 (가장 작은 나무와 가장 높은 나무 비교)



    day = 1 # 첫째 날부터 시작
    cnt = 0 # 나무에 물을 준 횟수 저장
    L = 0
    R = N-2


    while True:
        # 나무 오름차순 정렬
        trees.sort()

        # 기저 조건 : 가장 작은 나무의 높이가 목표 높이에 도달했을 경우
        if trees[0] == target_height:
            break

        # 인덱스 탐색
        for i in range(L,N-1):
            if trees[i] != target_height:
                L = i
                break

        for i in range(R,-1,-1):
            if trees[i] != target_height:
                R = i
                break

        # 나무 높이 구하기
        left_height = target_height - trees[L]
        right_height = target_height - trees[R]

        # 비교해야 할 나무가 하나 남았을 경우
        if L == R :
            if day % 2 : # 홀수 날
                if left_height == 2 :
                    day += 1
                    cnt += 1
                    continue
                trees[L] +=1
            else: # 짝수 날
                if left_height != 1:
                    trees[L] += 2

            day +=1
            cnt +=1

        else:
            # 가장 높은 나무의 높이 부터 물주기
            if day % 2 : # 홀수 날
                if right_height == 2:
                    trees[L] +=1

                else:
                    trees[R] +=1

            else: # 짝수 날
                if right_height != 1:
                    trees[R] += 2
                else:
                    if left_height != 1:
                        trees[L] += 2
            day +=1
            cnt +=1

    if not cnt:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} {day-1}')

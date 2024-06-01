
"""
예재 => 총 4 개의 식재료를 선택하는 경우의 수

0011
0110
0101
1010
1001
1100

절반을 나누었을 때, 대칭으로 경우의 값들은 같다.

"""
# 두 음식의 맛 차이 절댓값 구하기
def taste():
    global min_result
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j] : # 고른 걸 더하고
                result += arr[i][j]
            elif visited[i] == 0 and visited[j] == 0 : # 안 고른 걸 빼준다.
                result -= arr[i][j]
    min_result = min(min_result, abs(result))
    return


def choice(turn, num) : # 현재 배열 순회를 num 까지한 횟수 turn
    if turn > n // 2 :
        return

    if num == n-1 :
        if turn == n//2 : # 절반만 골랐을 경우
            taste()
        return

    choice(turn,num+1) # 선택하지 않을 경우

    # 재료 선택
    visited[num] = 1
    choice(turn+1,num+1) # 선택하는 경우

    # 초기화
    visited[num] = 0


T = int(input())

for tc in range(1,T+1):
    n = int(input()) # 식재료의 수
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]

    min_result = int(1e9)
    choice ( 0, 0 )
    print(f'#{tc} {min_result}')
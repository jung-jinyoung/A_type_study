"""
16진수 숫자(0~F)가 적혀 있는 보물상자
뚜껑은 시계방향으로 돌릴 수 있음
한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전
각 변에는 동일한 개수의 숫자. 시계방향 순으로 높은 자리 숫자에 해당. 하나의 수를 나타냄.
자물쇠의 비밀번호는 보물상자에 적힌 숫자로 만들 수 있는 모든 수 중,
K번째로 큰 수를 10진수로 만든 수.

"""
from collections import deque

def hex_to_decimal(hex_str):
    return int(hex_str, 16)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(input())
    n = N // 4
    num = deque(nums)
    result_set = set()

    # 회전 및 고유 숫자 수집
    for _ in range(n):
        # deque를 회전하여 새로운 조합 생성
        for i in range(0, N, n):
            # 현재 회전된 시퀀스 추출
            current_number = ''.join(list(num)[i:i+n])
            result_set.add(current_number)

        # deque를 우측으로 회전
        num.rotate(1)

    # 16진수 문자열을 10진수 숫자로 변환
    decimal_numbers = [hex_to_decimal(num_str) for num_str in result_set]

    # 10진수 숫자를 내림차순으로 정렬
    sorted_decimals = sorted(decimal_numbers, reverse=True)

    # K번째로 큰 숫자 찾기
    answer = sorted_decimals[K - 1]


    print(f"#{tc} {answer}")
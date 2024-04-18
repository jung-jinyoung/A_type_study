T = int(input())
for t in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))

    tallest = max(trees)            # 가장 큰 나무의 키
    to_grow = 0                     # 다른 나무가 가장 큰 나무와 키가 같아지려면 자라야 하는 값
    odd = 0                         # 자라야 하는 높이가 홀수인 나무의 개수를 카운팅
    for tree in trees:
        diff = tallest - tree       # 가장 큰 나무와의 키 차이
        to_grow += diff             # to_grow 업데이트
        if diff % 2:                # diff가 홀수이면, odd += 1
            odd += 1

    shortestDays = (to_grow // 3) * 2 + (to_grow % 3)   # trees 모두가 tallest까지 자랄 수 있는 최단기간
    one = shortestDays // 2 + shortestDays % 2          # shortestDays까지 성장이 1인 날
    two = shortestDays // 2                             # shortestDays까지 성장이 2인 날

    if odd <= one:                      # 홀수 높이 차의 나무 갯수 <= 이상적인 최단기간까지 성장이 1인 날의 수
        result = shortestDays           # 답은 이상적인 최단기간
    else:                               # 홀수 높이 차의 나무 갯수 > 이상적인 최단기간까지 성장이 1인 날의 수
        result = 2 * odd - 1            # 답은 odd번째 성장이 1인 날이 나오는 날

    print(f'#{t} {result}')

'''
        a   b  c  d  e  f  g
trees = [1, 3, 3, 5, 5, 5, 6]인 경우 tallest는 6, odd(차가 홀수 인 나무 개수) = 6, to_grow = 14
shortest(이상적인 최단 기간) = (to_grow // 3) * 2 + to_grow % 3
                          = 10
                          그 중 성장이 1인 날 = shortest // 2 + shortest % 2 = 5
                          성장이 2인 날      = shortest //2 = 5
날짜           1 2 3 4 5 6 7 8 9 10
자라는 길이     1 2 1 2 1 2 1 2 1 2
어떤 나무      d b b c c a a a e    | 이상적인 기간의 경우 나무 f가 자라는 1일이 없음
                                    이렇게 odd > 성장이 1인 날인 경우에 result = 2 * odd - 1
'''
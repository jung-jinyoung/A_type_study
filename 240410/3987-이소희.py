'''
3종류, 최대 10개
3 10
4 5 6
-> 52
'''
def combi(start, total, selected):
    global maxsum
    if total > C:
        return
    if total <= C:
        tmp = 0
        for each in selected:
            tmp += each ** 2
        maxsum = max(maxsum, tmp)
    for i in range(start, N):
        combi(i + 1, total + honey[i], selected + [honey[i]])

T = int(input())
for tc in range(1, T+1):
    N, C = map(int, input().split())
    honey = list(map(int, input().split()))
    lst = []
    maxsum = 0
    combi(0, 0, [])
    print(f'#{tc} {maxsum}')


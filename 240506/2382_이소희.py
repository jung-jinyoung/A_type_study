# dir : 1(up) 2(down) 3(left) 4(right)
# micro => i,j,n,d
def move(micro,N):
    i,j,n,d = micro
    if d == 1 :
        if i == 1:                  # 약품을 만나면 
            return (i-1,j,n//2,2)   # 미생물양 절반이 되고, 방향이 바뀜
        else :                      # 아니면 그냥 위치만 바뀜
            return (i-1,j,n,1)
    elif d == 2:
        if i == N-2:
            return (i+1,j,n//2,1)
        else :
            return(i+1,j,n,2)
    elif d == 3:
        if j == 1:
            return (i,j-1,n//2,4)
        else :
            return (i,j-1,n,3)
    else:
        if j == N-2:
            return (i,j+1,n//2,3)
        else :
            return (i,j+1,n,4)

def merge(lst):                                         #  lst = [(i1,j1,n1,d1), (i2,j2,n2,d2), ...]
    biggest = max(lst,key=lambda each:each[2])          # 미생물 수를 기준으로 가장 큰 놈 찾아내기
    microsum = 0
    for each in lst:
        microsum += each[2]
    return (biggest[0],biggest[1],microsum,biggest[3])  # 가장 큰 미생물의 좌표, 합쳐진 미생물 수, 가장 큰 미생물의 방향을 넘긴다

T = int(input())
for t in range(1, 1+T):
    N, M, K = map(int, input().split())
    micro_all = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):                              # M번 반복
        board = [move(micro,N) for micro in micro_all]
        dict = {}
        for i,j,n,d in board:                       # ex_dict = { kej:[value1, value2, value3...] }
            if (i,j) not in dict.keys():            # 해당 좌표가 딕셔너리에 없다면 키를 만들고 값 추가
                dict[(i,j)] = []
                dict[(i,j)].append((i,j,n,d))
            else :                                  # 이미 있다면 키에 값만 추가
                dict[(i,j)].append((i,j,n,d))

        result = []
        for square in dict.items():                 # square = 칸마다의 key, value값
            # print(square)                         # ((0, 1), [(0, 1, 3, 2)])
            if len(square[-1]) == 1:                # value 값이 하나라면 그대로 result에 추가
                result.append(square[-1][0])
            else :                                  # value 값이 여러개라면
                tmp = merge(square[-1])             # 합치기 / (biggest[0],biggest[1],microsum,biggest[3])
                result.append(tmp)

        micro_all = result                          # 전체 값 갱신

    answer = 0
    for micro in micro_all:
        answer += micro[2]

    print(f'#{t} {answer}')
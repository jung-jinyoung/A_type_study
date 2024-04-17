import sys
sys.stdin = open('sample_input.txt','r')

'''
1767. 프로세서 연결하기

가장자리에 있는 코어들까지 리스트에 담은 경우
1,357 ms/82,336 kb
가장자리에 있는 코어들은 리스트에 담지 않은 경우 --> 시간,메모리 상당히 많이 준다
286 ms/53,560 kb
'''


from collections import deque
def fff(core_idx,res,open_cnt):             # core_idx = 코어 번호, res = 현재까지 이용한 전선, open_cnt=개방된 코어 갯수
    global line,open_min
    if open_cnt>open_min:return             # 개방 코어 개수가 더 크면 더 이상 볼 필요 없음
    if core_idx == core_num:                # 코어 인덱스가 코어 갯수와 같아지면 끝!
        if open_min == open_cnt:            # 현재 개방 코어개수가 최소 개방 코어 개수와 같으면
            line = min(line,res)            # 최소길이를 저장
        else:
            open_min = open_cnt             # 현재 코어 개수가 더 작으면 최소 개방 코어 개수 갱신
            line = res                      # res 를 line 값으로
        return

    x,y=core[core_idx][0],core[core_idx][1]     # core 리스트에 저장된 코어의 행,열을 x,y로 받는다
    if x==0 or x==N-1 or y == 0 or y ==N-1:
        fff(core_idx+1,res,open_cnt)            # 가장자리에 있으면 바로 다음 코어로 넘어간다
    stack = deque()
    ##############################################
    cnt = 0                                     # 함수로 만들어서 불러오는 편이 더 깔끔하긴 했을듯 ...
    for k in range(y+1,N):                      # 코어기준 오른쪽
        if visited[x][k]!=0:
            break
        else:
            visited[x][k] = 1
            cnt+=1
            stack.append(k)
    else:
        fff(core_idx+1,res+cnt,open_cnt)
    while stack:
        j = stack.pop()
        visited[x][j]=0
    ##############################################
    cnt = 0
    for k in range(0, y):                       # 코어기준 왼쪽
        if visited[x][k] != 0:                  # 배열에 코어 혹은 전선이 있으면 해당 방향 불가!
            break
        else:                                   # 가능하면
            visited[x][k] = 1                   # 방문 표시
            cnt += 1                            # 전선 사용한 만큼 췍
            stack.append(k)                     # dfs 이기에 방문 지우기 할 때 사용할 인덱스를 append해
    else:
        fff(core_idx + 1, res + cnt,open_cnt)   # for-else구문으로 문제 없으면 다음 코어로!
    while stack:                                # for문에서 break 걸렸을때 그 전까지 체크한 자리 지우기
        j = stack.pop()
        visited[x][j] = 0
    ##############################################
    cnt = 0
    for k in range(x + 1, N):                   # 코어기준 아래
        if visited[k][y] != 0:
            break
        else:
            visited[k][y] = 1
            cnt += 1
            stack.append(k)
    else:
        fff(core_idx + 1, res + cnt,open_cnt)
    while stack:
        i = stack.pop()
        visited[i][y] = 0
    ##############################################
    cnt = 0
    for k in range(0, x):                       # 코어기준 위
        if visited[k][y] != 0:
            break
        else:
            visited[k][y] = 1
            cnt += 1
            stack.append(k)
    else:
        fff(core_idx + 1, res + cnt,open_cnt)
    while stack:
        i = stack.pop()
        visited[i][y] = 0
    ##############################################
    fff(core_idx + 1, res, open_cnt + 1)

T = int(input())
for tc in range(T):
    N=int(input())
    visited = [list(map(int,input().split())) for _ in range(N)]
    core = []
    core_num=0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    continue            # 가장자리에 있는 코어는 지나감
                core_num += 1           # 코어 갯수 체크
                core.append((i,j))      # 코어 좌표 append
    open_min = core_num                 # 개방 코어 갯수는 작아야 하니 최대값인 코어 갯수에서 시작
    line = core_num*N                   # 전선 길이는 작아야 하니 최대값인 (코어 갯수 X N)으로 시작
    fff(0,0,0)                          # dfs 출발
    print(f'#{1+tc} {line}')
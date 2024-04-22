import sys
sys.stdin = open('sample.txt','r')

'''
15685. 드래곤 커브
python3 :  68ms,  32140kb
pypy3   : 152ms, 114876kb

    <일차변환> 
    - 원점을 기준으로 세타만큼 회전을 할 때 사용하는 일차변환을 사용
        >> 회전을 원하는 좌표값에서 회전 축 좌표를 빼고 회전 이후 더해주는 방식 사용
    - 이번 문제에서는 90회전 이었기에 cos,sin 값은 모두 0 아님 +-1이기에 행렬의 곱만 잘 생각해서 좌표를 적어주면 OK
    [[cosθ,-sinθ],[sinθ,cosθ]] -> θ = -pi/2 -> [[0,1],[-1,0]] 에 행렬곱으로 [[r],[c]]를 하면 [[c],[-r]]
    
    
    <32,33 번째 줄에 좌표가 나온 이유?>
        - 위에서 설명 한 바와 같이 r,c를 회전하면 c,-r이 된다
        - 회전축 fx,fy 라 하면 r-fx,c-fy를 회전시켜서 c-fy,fx-r이 나오고 각각에 축 값을 더하면 아래에서 사용한 c-fy+fx,fx-r+fy 됨!
'''

delta = ((0,1),(-1,0),(0,-1),(1,0))
N = int(input())
arr = [[0]*101 for _ in range(101)]
list=[]
temp=[]
for _ in range(N):
    visited=[]
    y,x, d, g = map(int,input().split())
    visited.append((x,y))                                   # 시작점을 가장 먼저 append
    visited.append((x + delta[d][0], y + delta[d][1]))      # 0세대 작업 ㄱ
    arr[x][y]=arr[x + delta[d][0]][y + delta[d][1]] = 1     # 마지막에 정사각형 확인을 위한 array에도 체크
    fixed_x, fixed_y = x + delta[d][0],y + delta[d][1]      # 회전축 설정
    for _ in range(g):                                      # 입력한 세대까지 커브 순회
        for idx in range((len(visited))):
            i,j=visited[idx]                                # visited에 담은 좌표를 다 꺼내서 회전 ㄱㄱ
            visited.append((fixed_x-fixed_y + j ,fixed_x+fixed_y - i))
            arr[fixed_x-fixed_y + j][fixed_x+fixed_y - i] = 1
        fixed_x, fixed_y = fixed_x-fixed_y + visited[0][1] ,fixed_x+fixed_y - visited[0][0]     # 회전축을 갱신
    temp+=visited
list = set(temp)
cnt = 0
for i,j in list:                    # 정사각형 카운트
    if 0<=i+1<101 and 0<=j+1<101 and arr[i+1][j+1] == 1 and arr[i][j+1] == 1 and arr[i+1][j] == 1:
        cnt += 1
print(cnt)
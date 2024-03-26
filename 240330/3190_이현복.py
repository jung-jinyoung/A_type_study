import sys
sys.stdin = open('input1.txt','r')

'''
3190번_뱀
시간 : 156/76ms
메모리 : 114108/34112KB

입력 받은 시간 만큼 해당 방향을 가는줄 알고 문제를 풀고
마지막에 시간의 흐름인거 파악해서 수정하여 다소 난잡
'''

from collections import deque
delta=[(0,1),(1,0),(0,-1),(-1,0)]

def move(cnt):
    for _ in range(X):
        cnt+=1
        i,j=queue.pop()
        queue.append([i,j])
        ni,nj=i+delta[dir][0],j+delta[dir][1]
        if 0<=ni<N and 0<=nj<N and [ni,nj] not in queue:
            queue.append([ni,nj])
            if arr[ni][nj] == 1:
                arr[ni][nj]=0
            else:
                queue.popleft()
        else:
            return cnt*(-1)
    return X

N=int(input())              # N X N 보드
K=int(input())              # 사과 개수
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    arr[r-1][c-1]=1
arr[0][0]+=10               # 뱀 위치는 10
dir = 0                     # 뱀 방향은 delta의 0번 인덱스가 시작 방향
L=int(input())              # 뱀 방향 전환
queue=deque([[0,0]])
res = 0
tmp=[0]
for _ in range(1,1+L):
    x,C = input().split()
    tmp.append(int(x))
    X=tmp[-1]-tmp[-2]
    time_cnt = move(0)
    if time_cnt < 0 :
        res+=(-time_cnt)
        break
    else:
        res+=time_cnt
    if C == 'D': dir=(dir+1)%4
    else: dir=(dir-1)%4
else:
    X=N
    res-=move(0)
print(res)
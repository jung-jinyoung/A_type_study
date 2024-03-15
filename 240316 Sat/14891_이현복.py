
'''
14891_톱니바퀴
메모리 34088KB
시간 68ms
'''

from collections import deque

def rot(idx,turn,check_List):
    # if check_List == [1,1,1,1]:   => 런타임에러
    if check_List[idx] == 1:
        return
    check_List[idx]=1
    if idx+1<4 :
        if arr[idx][2]!=arr[idx+1][6] and not check_List[idx+1]:
            rot(idx+1,turn*(-1),check_List)
        else:
           rot(idx+1,0,check_List)
    if idx-1>=0 :
        if arr[idx-1][2]!=arr[idx][6] and not check_List[idx-1]:
            rot(idx-1,turn*(-1),check_List)
        else:
           rot(idx-1,0,check_List)
    if turn != 0: arr[idx].rotate(turn)

arr=[0]*4
for i in range(4):
    arr[i]=(deque(map("".join,input())))
K = int(input())
score=[[0,0,0,0],[1,2,4,8]]
for _ in range(K):
    gear,direction=map(int,input().split())
    rot(gear-1,direction,[0,0,0,0])
res_score=0
for i in range(4):
    res_score+=score[int(arr[i][0])][i]
print(res_score)

  
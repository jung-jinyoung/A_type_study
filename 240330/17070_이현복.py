import sys
sys.stdin = open('input1.txt','r')

'''
17070번_파이프 옮기기1
시간 : 860ms
메모리 : 115468KB
'''

def fff(x,y,dir):       # dir :  1=가로,2=세로,3=대각
    global res
    if x==N-1 and y==N-1:
        res+=1
        return
    else:
        if 0<=x+1<N and 0<=y+1<N and arr[x+1][y]==arr[x+1][y+1]==arr[x][y+1]==0:
            fff(x+1,y+1,3)
        if  dir!=1 and 0<=x+1<N and arr[x+1][y]==0:
            fff(x+1,y,2)
        if dir!=2 and 0<=y+1<N and arr[x][y+1]==0:
            fff(x,y+1,1)

N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
res = 0
fff(0,1,1)
print(res)
import sys
sys.stdin = open('input1.txt','r')

'''
백준_14888_연산자 끼워넣기
python3
시간 :  52ms
메모리 :  31252kb
'''

def dfs(level,value,add,sub,mul,div):
    global max_v,min_v
    if level == N-1:
        if max_v < value:
            max_v = value
        if min_v > value:
            min_v = value
        return
    if add:
        dfs(level+1,value+A[level+1],add-1,sub,mul,div)
    if sub:
        dfs(level+1,value-A[level+1],add,sub-1,mul,div)
    if mul:
        dfs(level+1,value*A[level+1],add,sub,mul-1,div)
    if div:
        dfs(level+1,int(value/A[level+1]),add,sub,mul,div-1)

N = int(input())
A = list(map(int,input().split()))
a,s,m,d = map(int,input().split())
max_v,min_v=int(-1e9),int(1e9)
dfs(0,A[0],a,s,m,d)
print(max_v)
print(min_v)
'''
백준 14889 스타트와 링크
'''
def di(Alist, Blist): # 차이 구하는 함수
    Asum = Bsum = 0
    for i in range(N//2):
        for j in range(N//2):
            Asum += arr[Alist[i]][Alist[j]]
            Bsum += arr[Blist[i]][Blist[j]]
    return abs(Asum-Bsum)  
      
def team(k, Alist, Blist):
    global mindi
    if mindi == 0:  # 차이가 이미 0이면
        return      # 그게 최소야
    if k == N:      # 다 돌았으면 그 중에서
        if len(Alist) == len(Blist): # 반반으로 나뉜 것 중에
            mindi = min(mindi, di(Alist, Blist)) # 최솟값을 구하라
        return
    team(k+1, Alist+[k], Blist) # k가 Alist로 들어간 경우
    team(k+1, Alist, Blist+[k]) # k가 Blist로 들어간 경우

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mindi = 50 * 50 * 50

team(0, [],[])
print(mindi)

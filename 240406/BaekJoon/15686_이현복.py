import sys
sys.stdin = open('input1.txt','r')

'''
15686_치킨배달
(python/pypy)
 31120/111564kb
 604/172ms
'''

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
bbq=[]                      # 모든 치킨집 위치 저장용
house=[]                    # 모든 집 위치 저장용
res = 2*N*M*2*N             # 치킨거리 최대값으로 2N거리인 집2N개
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:house.append((i,j))
        elif arr[i][j]==2:bbq.append((i,j))
for i in range(1<<len(bbq)):
    if bin(i)[2:].count('1')==M:    # 1이 M개있다면 j를 M개 뽑을 수 있다
        bbq_alive=[]
        for j in range(len(bbq)):
            if i&(1<<j):
                bbq_alive.append(bbq[j])    # 나온 조합 번호를 인덱스로 사용하는 치킨집 좌표 append
        min_v = 0
        for x1,y1 in house:
            temp = 2*N                      # 각 집별 치킨거리 최대 : 2N
            for x2,y2 in bbq_alive:
                temp=min(temp,abs(x1-x2)+abs(y1-y2))    # 더 작은값을 temp에 저장
            min_v+=temp                                 # 모든 집의 치킨거리 합 저장하자
        res=min(res,min_v)              # 각 조합별 치킨거리 총 합 중 작은거
print(res)
import sys
sys.stdin = open('sample_input.txt','r')

'''
15686_치킨 배달
pypy3 : 113124KB/204ms
python3 :32204kb/668ms
'''

def distance(p1,p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])


N,M=map(int,input().split())    # NxN마을, M개의 치킨집만 생존(최대)
arr = [list(map(int,input().split())) for _ in range(N)]    #  0=빈 칸, 1=집, 2=치킨집
bbq=[]
house=[]
cnt = 0 # 치킨집 세는용
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            bbq.append((i,j))
            cnt+=1
        elif arr[i][j]==1:
            house.append([i,j,[]])

bbq_alive = []
if cnt>M:                                   # 0부터 cnt-1 까지에서 M개 뽑자
    for i in range(1<<cnt):                 # 2진수 비트 필터를 1 로 만든다
        if str(bin(i)).count('1') == M:     # 1의 개수가 M개이면
            temp=[]
            for j in range(cnt):        
                if i&(1<<j):                # 필터 통과되면
                    temp.append(bbq[j])     # 임시용 스택인 temp에 append
            bbq_alive.append(temp)          # 살아남은 치킨집 배열에 temp 메ㅔ둥

    res=2*N*len(house)
    for case in bbq_alive:                  # 살아남은 치킨집의 경우를 모두 순회
        for i in range(len(house)):         
            min_v = 2*N 
            for col in case:                # 살아남은 치킨집 하나하나를 순회
                if min_v > distance(house[i][0:2],col):         # min_v 보다 저 작은 값이면 치킨 거리 갱신
                    min_v = distance(house[i][0:2],col)
            house[i][2].append(min_v)                           # house 배열에 치킨 거리 넣어서 갱신

    for i in range(len(bbq_alive)):
        tmp = 0
        for chicken_d in house:             # 살아남은 치킨집 경우 별 치킨거리의 총 합
            tmp+=chicken_d[2][i]
        res=min(tmp,res)
    print(res)

else:           # 주어진 치킨집이 M개 이하일 때는 위쪽 if문 굳이 들어가서 시간 안 끌게 만들어줌
    for i in range(len(house)):
        house[i][2]=2*N
        for position in bbq:
            if house[i][2] > distance(house[i][0:2],position):
                house[i][2] = distance(house[i][0:2],position)
    res = 0
    for chicken_d in house:
        res+=chicken_d[2]
    print(res)




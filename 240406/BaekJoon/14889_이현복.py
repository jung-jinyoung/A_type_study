import sys
sys.stdin = open('input111.txt','r')

'''
14889_스타트와 링크
(pypy/python)
시간 : 1212 ms 7204 ms 
메모리 :111360 kb 31120 kb

 append로 했을때  pypy만 패쓰
시간 : 784 ms
메모리 : 111356 kb

team1 만 다 뽑아도 될듯?
'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
res=100*20
for i in range(1<<N):
    team1, team2 = [0]*(N//2), [0]*(N//2)
    p1=p2=0
    if bin(i)[2:].count('1')==N/2:
        for j in range(N):
            if i&(1<<j):
                team1[p1]=j
                p1+=1
                # team1.append(j)
            else:
                team2[p2]=j
                p2+=1
                # team2.append(j)
    score1=score2=0
    if team1 != [0]*(N//2):
        for x in range(len(team1)-1):
            for y in range(x,len(team1)):
                score1 += (arr[team1[x]][team1[y]]+arr[team1[y]][team1[x]])
                score2 += (arr[team2[x]][team2[y]]+arr[team2[y]][team2[x]])
        tmp = abs(score1-score2)
        if res > tmp:
            res = tmp
print(res)
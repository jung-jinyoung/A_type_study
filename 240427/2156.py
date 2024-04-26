# 포도주

'''
연속으로 놓여있는 3잔을 마실 수는 없다.
최대로 마실 수 있는 포도주의 양

이 문제 소희가 완전히 이해함
소희 박사님 강의 듣기 추천
'''

n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))

d = [0]*n+1
d[1] = wine[1]

if n > 1:
    d[1] = wine[0]+wine[1]

if n > 2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])

print(d[n-1])
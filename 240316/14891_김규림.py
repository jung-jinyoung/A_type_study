from collections import deque

def left(n, dir):
    if n >= 0 and arr[n][2] != arr[n+1][6]:
        left(n-1, -dir)
        arr[n].rotate(dir)

def right(n, dir):
    if n < 4 and arr[n][6] != arr[n-1][2]:
        right(n+1, -dir)
        arr[n].rotate(dir)


arr = [deque(input()) for _ in range(4)]
k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1                # 번호랑 인덱스 맞춰주기
    left(num-1, -dir)       # 왼쪽 톱니바퀴, 방향 반대로
    right(num+1, -dir)      # 오른쪽 톱니바퀴, 방향 반대로
    arr[num].rotate(dir)    # 1이면 오른쪽으로 이동 / -1이면 왼쪽으로 이동


ans = 0
for i in range(4):
	if arr[i][0] == '1':
		ans += 2**i
print(ans)
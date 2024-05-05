# 보물상자 비밀번호

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    data = input()
    arr = []

    for j in range(n//4):
        # 4등분씩 값 입력
        for i in range(0, n, n//4):
            arr.append(data[i:i+(n//4)])
        # 맨 뒤의 값이 맨 앞으로 올 수 있도록
        data = data[-1] + data[:-1]

    # 중복 제거
    arr = list(set(arr))
    arr.sort(reverse=True)

    # k번째 수
    result = arr[(k-1)%len(arr)]

    print(f'#{tc} {int(result, 16)}')
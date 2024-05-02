'''
12 10
1B3B3B81F75E
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    password = input()
    password = password + password
    M = N // 4

    nums = []
    for i in range(N):
        new = password[i:i+M]
        nums.append(new)
    nums = list(set(nums))
    nums.sort(reverse=True)
    print(f'#{tc} {int(nums[K - 1], 16)}')
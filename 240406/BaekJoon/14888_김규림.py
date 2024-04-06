def func(num, i, add, sub, mul, div):
    global max_num
    global min_num

    if i == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if add > 0:
        func(num + nums[i], i+1, add-1, sub, mul, div)
    if sub > 0:
        func(num - nums[i], i+1, add, sub-1, mul, div)
    if mul > 0:
        func(num * nums[i], i+1, add, sub, mul-1, div)
    if div > 0:
        func(int(num / nums[i]), i+1, add, sub, mul, div-1)

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = int(-1e9)           # 1e9 = 1 * 10^9
min_num = int(1e9)            # int형에서 무한대 값을 나타내기 위해 사용

func(nums[0], 1, op[0], op[1], op[2], op[3])

print(max_num)
print(min_num)


'''
백준 14888 연산자 끼워넣기
'''
def dfs(k, result, plus, minus, mul, div):
    global maxnum, minnum
    if k == N:      # 계산이 끝나면 maxnum, minnum 값 바꾸기
        maxnum = max(result, maxnum)
        minnum = min(result, minnum)
        return
    # 계산 중일 때는, 연산자 수가 남아있을 때만 해당 연산자 사용 가능
    if plus > 0:     # + 개수가 남아있을 때만
        dfs(k+1, result+nums[k], plus-1, minus, mul, div)
    if minus > 0:    # - 개수가 남아있을 때만
        dfs(k+1, result-nums[k], plus, minus-1, mul, div)
    if mul > 0:      # * 개수가 남아있을 때만
        dfs(k+1, result*nums[k], plus, minus, mul-1, div)
    if div > 0:      # / 개수가 남아있을 때만
        dfs(k+1, int(result/nums[k]), plus, minus, mul, div-1)

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

minnum, maxnum = int(1e9), int(-1e9)
# k = 1부터. 0은 초기 결과값으로 들어감.
dfs(1,nums[0],plus, minus, mul, div)
print(maxnum)
print(minnum)

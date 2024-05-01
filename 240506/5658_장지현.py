# 보물상자 비밀번호
# 240502
# 44,972 kb / 115 ms


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    s = n // 4  # 한 변 길이

    nums = input()
    nums = nums + nums  # idx 밀어가면서 사용

    pw_list = []     # sliced passwords 담을 리스트
    for r in range(s):  # rotate
        nummm = nums[r:r+n]  # 해당 라운드에서의 숫자열
        for i in range(0, n, s):    # s 간격만큼 slice
            pw_list.append(nummm[i:i+s])
    pw_list = list(set(pw_list))    # 중복제거
    pw_list.sort(reverse=True)
    print(f"#{tc} {int(pw_list[k-1], 16)}")
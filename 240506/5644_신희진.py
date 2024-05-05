def br_t_f(x, y):
    t = [0 for _ in range(A)]
    for n, bc in enumerate(bc_list):
        i, j, c = bc
        distance = abs(i - x) + abs(j - y)
        if c >= distance:
            t[n] = 1
    return t



def max_bc_sum(p1, p2, pw_list):
    p1_max = 0
    p2_max = 0
    half = 0
    for i in range(A):
        if p1[i] == 1 and p2[i] == 1:
            half = pw_list[i] // 2
        elif p1[i] == 1 and p2[i] == 0:
            if p1_max < pw_list[i]:
                p1_max = pw_list[i]
        elif p1[i] == 0 and p2[i] == 1:
            if p2_max < pw_list[i]:
                p2_max = pw_list[i]

    if half != 0:
        if p2_max != 0:
            p1_max = max(p1_max, half * 2)
        elif p1_max != 0:
            p2_max = max(p2_max, half * 2)
        elif p1_max == 0 and p2_max == 0:
            p1_max, p2_max = half, half

    return p1_max + p2_max



T = int(input())
for tc in range(T):
    arr = [[0 for _ in range(10)] for __ in range(10)]
    M,A = map(int,input().split())
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    bc_list = []
    pw_list = []

    for a in range(A):
        i,j,c,p = map(int,input().split())
        bc_list.append([j-1,i-1,c])
        pw_list.append(p)

    # 이동하지 않음, 상, 우, 하, 좌
    di = [0,-1,0,1,0]
    dj = [0,0,1,0,-1]
    p1x, p1y = 0, 0
    p2x, p2y = 9, 9

    res = max_bc_sum(br_t_f(p1x,p1y), br_t_f(p2x,p2y),pw_list)

    for i in range(M):
        p1_r = p1[i]
        p2_r = p2[i]
        if 0 <= p1x+di[p1_r] <10 and 0<= p1y+dj[p1_r]<10:
            p1x,p1y = p1x+di[p1_r],p1y+dj[p1_r]

        if 0 <= p2x+di[p2_r] <10 and 0<= p2y+dj[p2_r]<10:
            p2x, p2y = p2x+di[p2_r], p2y+dj[p2_r]
        # print("몇번째나면 : ",i)
        # print(p1x,p1y)
        # print(p2x,p2y)
        # print(max_bc_sum(br_t_f(p1x, p1y), br_t_f(p2x, p2y),pw_list))
        res += max_bc_sum(br_t_f(p1x,p1y), br_t_f(p2x,p2y),pw_list)

    print(f'#{tc+1}',res)
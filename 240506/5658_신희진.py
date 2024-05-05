from collections import deque
T = int(input())
for tc in range(T):
    # 숫자의 개수, 크기순서
    N,K = map(int,input().split())
    arr = input()
    # 결과를 받을 리스트
    res_list = []
    # 4등분을 했을 때, 한 변에 있을 숫자의 개수
    cut_num = N//4
    # 숫자의 개수만큼 돌아준다.
    for i in range(N):
        # 4등분을 하며 값을 입력받아줌
        for idx in range(0,N,cut_num):
            if arr[idx:idx+cut_num] not in res_list:
                res_list.append(arr[idx:idx+cut_num])
        # 맨 앞의 수가 뒤로 갈 수 있도록 재설정
        arr = arr[1:] + arr[0]
    # 값 정렬 - 내림차순
    res_list.sort(reverse=True)
    # 내림차순 후 K번째에 있는 수 출력
    print(f'#{tc+1}', int(res_list[K-1],16))


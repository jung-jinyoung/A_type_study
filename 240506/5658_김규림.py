T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    password = list(input().strip())

    cnt = N // 4        # 회전 횟수
    arr = []            # 생성된 패스워드 저장할 리스트

    for i in range(cnt):                     # 회전 수 만큼 반복
        for j in range(0, N, cnt):           # 한번 회전할 때마다 cnt씩 이동
            pw = ''.join(password[j:j+cnt])  # 리스트 슬라이싱에서 문자열로 변경
            arr.append(pw)                   # 생성된 패스워드 arr에 추가
        last = password.pop()                # 마지막 문자 꺼내서
        password.insert(0, last)      # 맨 앞에 삽입

    brr = set(arr)      # 중복 제거
    answer = []
    for num in brr:
        answer.append(int(num, 16))          # 각 패스워드 16진수로 변환

    result = sorted(answer, reverse=True)    # 내림차순 정렬
    print(f'#{t+1} {result[K-1]}')

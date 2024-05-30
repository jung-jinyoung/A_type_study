'''
5658. 보물상자 비밀번호

각 변에는 동일한 개수의 숫자 시계방향순으로 높은 자리 수
4개의 변
보물 상자에는 자물쇠, 이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수
N개의 숫자가 입력으로 주어졌을 때, 보물 상자의 비밀번호를 출력하는 프로그램
'''


# 비밀번호를 회전하는 것을 데크의 앞에 숫자를 하나 뽑아 뒤로 집어 넣는 방식으로 구현하려고 함
from collections import deque

T = int(input())
# 각 테스트 케이스별 시행
for tc in range(1, T+1):
    # 주어진 숫자의 개수 N과 K번째로 큰 수를 구하려고 함
    N, K = map(int, input().split())
    # 데큐로 16진수 수들을 입력 받고
    numbers = deque(input())
    # 각각의 회전에서 생성된 암호들을 저장할 데큐 passwords
    passwords = deque()
    # 회전을 진행하려는데 N만큼 회전하면 초기 수와 동일하기 때문에 N-1만큼 수들을 회전해주면 된다.
    for _ in range(N-1):
        # 암호들은 총 4면에 적혀 있으므로 한 번의 회전당 총 4개의 수가 나온다.
        for i in range(4):
            # 암호를 읽어낼 빈 문자열 변수 password
            password = ''
            # 한 면에 적혀 있는 암호의 길이는 전체 길이 N을 4로 나눈 값
            for j in range(N//4):
                # 아래와 같이 작성해서 i와 j 값에 따라 4개의 16진수가 차례대로 읽혀진다.
                password += numbers[i*(N//4)+j]
            # 해당 값을 10진수로 바꿔주고
            password = int(password, 16)
            # 아까 만든 데큐에 넣어준다.
            passwords.append(password)
        # 보물 상자의 비밀번호를 한 칸 회전
        numbers.append(numbers.popleft())
    # 집합으로 중복을 제거해주고
    passwords = set(passwords)
    # 다시 리스트로 만들어주고
    passwords = list(passwords)
    # 내림차순으로 정렬해준다.
    passwords.sort(reverse=True)
    # K번째 수를 인덱스로 접근해서 출력해준다.
    print(f'#{tc} {passwords[K-1]}')

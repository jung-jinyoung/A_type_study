import sys
sys.stdin = open('sample_input.txt','r')


# swea_5658_보물상자 비밀번호
# 메모리 : 111 ms
# 실행시간 : 45,212 kb


T = int(input())
for tc in range(T):
    N,K = map(int,input().split())
    arr = input()
    for i in range(N//4-1):         # 한 숫자를 구성하는 숫자는 N//4 개!
        arr+=arr[i]                 # 슬라이싱으로 숫자 뽑으려 할 때 마지막 부분을 위한 추가
    num_set=[]
    for idx in range(0,N):
        num_set.append(int(arr[idx:idx+N//4],16))   # 슬라이싱으로 뽑은 16진수를 10진수로 바꿔서 append
    num_set=list(set(num_set))                      # 중복 제거를 위한 set 그 이후 sort를 위한 list로
    num_set.sort(reverse=True)                      # 내림차순
    print(f'#{tc+1} {num_set[K-1]}')                # k번째 수 출력

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
 
    tmp = input()
    hex_set = set()     # 16진수 중복을 제거하기 위해 set에 넣을 계획
 
    rotation = N//4     # 4변으로 나눴을 때 개수 = 한변에서의 16진수 = 최대 회전수
 
    for i in range(rotation+1):     # 최대 회전수 만큼 각 변에서 16진수를 뽑아
        for j in range(0, N-(rotation-1), rotation):
            hex_set.add(tmp[j:j+rotation])  # 세트에 넣는다    
        tmp = tmp[-1]+tmp[:N-1]     # 보물상자 뚜껑 회전시킴
 
    result = []
    for str in hex_set:     # 중복 제거된 세트에서
        result += [int(str,16)]     # 10진수로 변환하여 리스트에 넣고
    result.sort(reverse=True)   # 내림차순 정렬
 
    print(f'#{tc}', result[K-1])    # K번째 수 출력

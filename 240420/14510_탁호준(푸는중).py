'''
N개의 나무가 있음. 초기의 각 나무의 키가 주어짐. 하루에 한 나무에 물을 줄 수 있다.
홀수번째 날은 물을 준 나무의 키가 1 자라고, 짝수 번째 날에 물을 준 나무의 키가 2자람.
모든 나무의 키가 처음에 가장 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수를 계산하라.
'''

from math import remainder


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_height = max(trees)     #나무 최대 높이

    #계산 1
    remain = [0,0,0] #더 자라야하는 크기가 0,1,2인 나무 수. 0번째 인덱스는 그냥 크게 신경 안써도 됨
    day = 0 #최소 일 수 
    for tree in trees:
        day += 2*(max_height-tree)//3 #2일연속 나무에 물을 주면 3씩 자라므로 (최대나무높이-현재나무높이)를 3으로 나눈 몫 만큼 날짜를 변경
        remain[tree%3] += 1 #3으로 나눈 나머지의 개수 1개씩 증가
    
    #계산 2
    if remain[1] and remain[2]: #만약 더자라야하는 크기가 1, 2인 나무의 수가 모두 1개 이상이면
        min_cnt = min(remain[1], remain[2])#더 자라야 하는 크기가 1, 2인 나무들 중 더 적은 나무 수
        remain[1] -= min_cnt
        remain[2] -= min_cnt
        day += 2*min_cnt

    #계산 3
    if remain[1]: # 1만큼 더 자라야하는 나무만 존재하는 경우
        '''
        1개면 1일 증가
        2개면 3일 증가
        3개면 5일 증가
        '''

        pass

    elif remain[2]: # 2만큼 더 자라야하는 나무만 존재하는 경우
        '''
        1개면 2일 증가 0 2
        2개면 3일 증가 1 2 1
        3개면 4일 증가 1 2 1 2
        4개면 6일 증가 1 2 1 2 0 2
        5개면 7일 증가 1 2 1 2 1 2 1    
        6개면 8일 증가 1 2 1 2 1 2 1 2
        '''
        
        pass
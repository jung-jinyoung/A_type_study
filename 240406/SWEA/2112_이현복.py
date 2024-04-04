import sys
sys.stdin = open('input1.txt','r')

'''
2112_보호필름
58,260 kb
1,531 ms
'''

def test(array):
    # res = [0]*W               # 이 방식으로 리스트 만들어서 확인하니까 실행시간 14초전도나옴ㄷㄷ
    for j in range(W):
        cnt = 1
        for i in range(D-1):
            if array[i][j]==array[i+1][j]:  # 앞이랑 같은가 확인
                cnt+=1
            else:
                cnt=1
            if cnt ==K:
                # res[j]=1
                break
        else: return False       # 불량 있음
    return True                  # 전부 통과

    # if res == [1]*W:
    #     return True
    # return False 

def dfs(array,idx,level):
    global res
    if idx>D or level >= res: return    # 필요없어진 경우 제거
    if test(array):                     # 검사결과 TRUE이면 res에 저장
        res = level
        return

    for i in range(idx,D):      # 조합이니까 앞에서 선택한거 이후만 순회
        temp = array[i]
        array[i]=[0]*W          # 0으로 도핑
        dfs(array,i+1,level+1)
        array[i]=[1]*W          # 1으로 도핑
        dfs(array,i+1,level+1)
        array[i]=temp           # 도핑 안하는 경우를 위해 복구

T = int(input())
for tc in range(T):
    D,W,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(D)]
    res= D              # 최대 도핑 가능 횟수는 D
    dfs(arr,0,0)
    print(f'#{1+tc} {res}')
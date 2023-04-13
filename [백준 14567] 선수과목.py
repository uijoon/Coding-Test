import sys
input = sys.stdin.readline
    
def main():
    N,M = map(int,input().split())

    dp = [1 for _ in range(N+1)] # 이수 학기를 저장하는 list, 1로 초기화
    arr = [[] for _ in range(N+1)] 
    # 선수과목을 저장하는 list
    # arr[1]은 1번 과목을 선수과목으로 하는 과목들

    for _ in range(M):
        from_,to = map(int,input().split())
        arr[from_].append(to) # arr에 과목 관계를 저장해 줍니다.
    
    for from_,sub in enumerate(arr): # 낮은 과목 번호부터 차례대로 고려해줍니다.
        for to in sub:
            dp[to] = max(dp[to],dp[from_]+1)
            # 선수과목의 이수학기 + 1이 더 크다면 갱신해줍니다.
    print(*dp[1:])
    
main()
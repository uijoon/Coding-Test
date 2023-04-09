import sys
input = sys.stdin.readline

def main() -> int:
    N = int(input())
    honey = list(map(int,input().split()))

    answer = sum(honey[1:-1]) + max(honey[1:-1]) # 가운데에 벌통이 있을 때
    cumsum = 0
    max_cumsum = 0

    for idx in range(2,N):
        cumsum += honey[idx-1]-2*honey[idx]
        max_cumsum = max(cumsum,max_cumsum)
    answer = max(2*sum(honey[2:])+max(0,max_cumsum),answer) # 오른쪽 끝에 벌통

    cumsum = 0
    max_cumsum = 0
    for idx in range(N-3,-1,-1):
        cumsum += honey[idx+1]-2*honey[idx]
        max_cumsum = max(cumsum,max_cumsum)
    answer = max(2*sum(honey[N-3::-1])+max(0,max_cumsum),answer) # 왼쪽 끝 벌통
    
    return answer

print(main())
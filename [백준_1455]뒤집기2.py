import sys

def flip(x): # 동전 뒤집기 함수
    return (x+1)%2

def main():
    N,M = map(int,sys.stdin.readline().split())
    global coin
    coin = []
    for _ in range(N):
        coin.append(list(map(int,list(sys.stdin.readline().rstrip())))) # 입력 int형으로 변경
    cnt = 0
    for r in range(N-1,-1,-1): # 마지막 행 -> 첫번째 행 순서로 진행
        for c in range(M-1,-1,-1): # 해당 행에서 마지막 열 -> 첫번째 열 순서로 진행
            if coin[r][c] == 1: # 뒷면 발견 시 해당 지점에서 동전 뒤집기
                cnt += 1
                for i in range(r,-1,-1): # 뒤집어야 하는 구역 flip 적용
                    coin[i][:c+1] = list(map(flip,coin[i][:c+1]))
    print(cnt)
main()
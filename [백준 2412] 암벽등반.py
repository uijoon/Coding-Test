import sys
from collections import deque
input = sys.stdin.readline
    
def main():
    n,T = map(int,input().split())
    # n : 좌표의 개수
    # T : 정상의 y축 좌표

    dot = set()
    for _ in range(n): # set에 tuple 자료형 좌표 저장
        x,y = map(int,input().split())
        dot.add((x,y))
    
    dq = deque()
    dq.append([0,0,0]) # x, y, 현재 이동거리
    while dq:
        x,y,cnt = dq.popleft()
        if y == T: # 정상에 도착한다면 break
            break
        for i in range(-2,3):
            for j in range(-2,3): # x,y 좌표에서 거리 2 이하의 점들을 탐색
                nx = x + i
                ny = y + j
                if (nx,ny) in dot: # set에 좌표가 들어있다면 dq에 append
                    dot.remove((nx,ny)) # 이미 지나간 좌표는 set에서 제외
                    dq.append([nx,ny,cnt+1])
    if y == T:
        print(cnt)
    else : # 마지막 반복문의 y값이 T가 아니라면 불가능한 경우
        print(-1)
    
main()
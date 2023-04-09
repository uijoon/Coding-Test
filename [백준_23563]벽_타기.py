import sys
from collections import deque

def around(y:int,x:int)->int:
    '''
    주위에 벽이 있는지 확인하는 함수
    있다 : 1, 없다 : 0
    '''
    global MAP
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if MAP[ny][nx] == '#':
            return 1
    return 0

def main():
    inf = 1e8
    H,W = map(int,sys.stdin.readline().split()) # 행, 열 개수
    global MAP
    MAP = [] # 루시우가 뛰어다닐 맵
    cost = [[inf for _ in range(W)] for _ in range(H)]
    # 시작점에서 해당 지점을 가기 위해 필요한 최소 시간
    # 적당히 큰 inf로 초기설정

    dx = [0,0,1,-1]
    dy = [1,-1,0,0] 

    for h in range(H): # 입력받기
        row = list(sys.stdin.readline().rstrip()) # 한 행씩 받음
        MAP.append(row)
        if 'S' in row: # 해당 행에 시작점이 있을 때
            start = (h,row.index('S')) # 시작점 좌표를 start에 저장
            MAP[h][row.index('S')] = '.' # 시작점을 빈 공간으로 바꿔줌
        
        if 'E' in row: # 해당 행에 끝점이 있을 때
            end = (h,row.index('E')) # 끝점 좌표를 start에 저장
            MAP[h][row.index('E')] = '.' # 끝점을 빈 공간으로 바꿔줌

    dq = deque()
    dq.append((start,0)) # (좌표,현재 시간)
    cost[start[0]][start[1]] = 0 # 시작점 cost를 0으로 초기화

    while dq:
        (y,x),sec = dq.popleft() # 왼쪽에서 좌표,시간 정보를 꺼내줌
        wall1 = around(y,x) # 현재 지점 주위에 벽이 있는지 확인
        
        for i in range(4): # 네 방향 확인
            ny,nx = y+dy[i],x+dx[i] # ny,nx에 다음에 이동할 좌표 저장
            wall2 = 0
            if MAP[ny][nx] == '.': # 다음 지점이 빈 공간일 경우
                if wall1:
                    wall2 = around(ny,nx) # 다음 지점 주위에 벽이 있는지 확인

                nsec = sec+1-(wall1&wall2)
                # 벽을 탈 수 있으면 현재 시간 그대로 가져감
                # 아니면 +1

                if cost[ny][nx] > nsec: # 다음 지점 cost가 nsec보다 클 경우
                    cost[ny][nx] = nsec
                    if wall1&wall2 :
                        dq.appendleft(((ny,nx),nsec))
                        # 벽을 탈 수 있다면 왼쪽에 넣어준다(0-1 BFS)
                    else :
                        dq.append(((ny,nx),nsec)) # 벽을 못타면 오른쪽

    print(cost[end[0]][end[1]])

main()
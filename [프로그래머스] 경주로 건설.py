from collections import deque
INF = 1000000

def solution(board):
    N = len(board)

    cost = {i : {j : {k : INF for k in range(4)} for j in range(N)} for i in range(N)}
    # 각 칸에서 방향별로 현재 최소 비용을 저장해야 함
    # cost[y][x][d] : (y,x) 좌표에 d방향으로 들어왔을 때 최소 cost
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    dq = deque()
    dq.append((0,0,0,0)) # cost, 현재 위치로 들어왔던 방향, y, x
    dq.append((0,3,0,0)) # (0,0)에서는 오른쪽, 아래쪽으로 밖에 못 감
    
    cost[0][0][0] = 0
    cost[0][0][3] = 0
    
    while dq:
        ccost, cdir, cy, cx = dq.popleft() # cost, 현재 위치로 들어왔던 방향, y, x
        
        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]
            ncost = ccost + 100 if i==cdir else ccost + 600 # 들어왔던 방향과 다를 경우 코너
            
            if (0<=ny<N)&(0<=nx<N): # 격자 범위 내에 있는지
                if (board[ny][nx]==0)&(cost[ny][nx][i]>ncost): # 빈 칸이고, 저장된 cost보다 낮은지 확인
                    cost[ny][nx][i] = ncost
                    dq.append((ncost,i,ny,nx))
                    
    answer = INF
    for i in range(4):
        answer = min(answer,cost[N-1][N-1][i])
    return answer
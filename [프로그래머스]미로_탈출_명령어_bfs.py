from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = "impossible"
    
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    dstr = ['d','l','r','u'] # d l r u 사전 순서
    
    dq = deque()
    dq.append((x,y,''))
    check_len = -1
    
    while dq:
        cur_x,cur_y,cur_str = dq.popleft()
        
        if len(cur_str) > check_len: # 지나온 거리가 갱신될 때마다 check을 초기화
            check = [[0 for _ in range(m+1)] for _ in range(n+1)]
            check_len += 1
        
        for ddx,ddy,ddstr in zip(dx,dy,dstr): # d l r u 순서로 방문
            next_x = cur_x + ddx
            next_y = cur_y + ddy
            next_str = cur_str + ddstr
            
            if (0<next_x<=n)&(0<next_y<=m):
                if check[next_x][next_y] == 1: # 같은 거리로 왔는데 사전 순서가 앞인 경로가 있으면 방문 x
                    continue
                    
                if len(next_str) < k: # 거리가 k가 안된다면 deque에 넣고 check에 방문 표시
                    dq.append((next_x,next_y,next_str))
                    check[next_x][next_y] = 1
                    
                elif len(next_str) == k: # 거리기 k가 되었다면 정답 여부 확인
                    if (next_x==r) & (next_y==c):
                        answer = next_str
                        return answer
    return answer
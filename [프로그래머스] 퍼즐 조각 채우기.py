from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0] # 상하좌우 이동

def solution(game_board, table):
    answer = 0
    N = len(game_board) # 정사각형 보드판 한 변의 길이
    for y in range(N):
        for x in range(N):
            game_board[y][x] = (game_board[y][x]+1)%2 
    # game_board은 0을 탐색해야 하고, table은 1을 탐색해야 하기 때문에
    # 편의성을 위해 1을 탐색하는 걸로 통일해줍니다.
            
    def bfs(y,x,BorT): 
        cur = game_board if BorT==0 else table # game_board=0, table=1 탐색할 배열을 설정
        minx,miny,maxx,maxy = N-1,N-1,0,0
        dq = deque()

        dq.append((y,x))
        cur[y][x] = 2 # 탐색 완료한 좌표는 2로 바꿈

        while dq: # bfs 탐색
            cy,cx = dq.popleft()             # 현재 좌표
            if cy>maxy: maxy = cy
            if cx>maxx: maxx = cx
            if cx<minx: minx = cx
            if cy<miny: miny = cy            # 퍼즐 한 조각이 담겨있는 직사각형의 범위를 구함
            
            for i in range(4):
                nx = cx+dx[i]
                ny = cy+dy[i]
                if (0<=nx<N)&(0<=ny<N):
                    if cur[ny][nx]==1:
                        cur[ny][nx] = 2       # 탐색 완료한 좌표는 2로 바꿈
                        dq.append((ny,nx))
        result = []
        for i in range(miny,maxy+1):
            result.append(cur[i][minx:maxx+1]) # game_board 또는 table에서 직사각형의 배열을 가져옵니다.
        return result
    
    def rotate(arr):
        result = []
        rotate_arr = arr.copy()
        result.append(rotate_arr)
        for i in range(3):
            temp = []
            maxy = len(rotate_arr)-1
            maxx = len(rotate_arr[0])-1
            for y in range(0,maxx+1):
                temp2 = []
                for x in range(maxy,-1,-1):
                    temp2.append(rotate_arr[x][y])
                temp.append(temp2)
            rotate_arr = temp.copy() # 위 과정을 거치면 시계방향으로 90도 회전한 배열이 나옵니다.
            result.append(rotate_arr)
        return result                # 3번 반복하여, 회전시킨 4개의 퍼즐을 result에 저장합니다.
    
    puzzle = []
    in_table = {}
    for y in range(N):
        for x in range(N):
            if game_board[y][x]==1:
                puzzle.append(bfs(y,x,0))
            if table[y][x]==1:
                in_table[len(in_table)] = rotate(bfs(y,x,1))

    for p in puzzle:
        for key in in_table:
            for arr in in_table[key]:
                if p == arr:                    # 현재 puzzle이 회전한 4개 중 있는지 확인
                    for line in p:
                        answer += line.count(2) # puzzle 조각 수 계산
                    del in_table[key]           # 매칭이 된 퍼즐은 key값에서 삭제해줍니다.
                    break
            if key not in in_table:             # 삭제가 됐다면 확인할 필요 없으므로 break 합니다.
                break
                    
    return answer
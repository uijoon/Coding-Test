def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    result = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for t,r1,c1,r2,c2,degree in skill:
        if t==1:
            degree = -degree
        result[r1][c1] += degree
        result[r2+1][c2+1] += degree
        result[r1][c2+1] -= degree
        result[r2+1][c1] -= degree
    for line in result:
        for x in range(1,M+1):
            line[x] += line[x-1]
    for x in range(M+1):
        for y in range(1,N+1):
            result[y][x] += result[y-1][x]
    for y in range(N):
        for x in range(M):
            if board[y][x]+result[y][x]>0:
                answer += 1
    
    return answer
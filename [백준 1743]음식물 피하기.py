import sys

sys.setrecursionlimit(10**6)

def dfs(y,x):
    global a
    global check
    global d
    global N,M

    check[y][x] = 1

    cnt = 1

    for dy,dx in d:
        ny = y + dy
        nx = x + dx
        if 0<=ny<N and 0<=nx<M and check[ny][nx] == 0 and a[ny][nx] == 1:
            cnt += dfs(ny,nx)
    #print(y,x,cnt)
    return cnt

def main():
    global N,M
    N,M,K = map(int, sys.stdin.readline().split())

    global a
    global check
    global d
    d = [[1,0],[-1,0],[0,1],[0,-1]]
    a = [[0 for _ in range(M)] for _ in range(N)]

    ans = 0

    check = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y,x = map(int, sys.stdin.readline().split())
        a[y-1][x-1] = 1

    #print(check)

    for y in range(N):
        for x in range(M):
            if check[y][x] == 0 and a[y][x] == 1:
                ans = max(ans,dfs(y,x))
    print(ans)
    return 0


main()
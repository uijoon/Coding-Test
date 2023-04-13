import sys
'''
def p(arr):
    r = len(arr)
    c = len(arr[0])

    for i in range(r):
        for j in range(c):
            print(arr[i][j],end = ' ')
        print('\n')
'''
def main():
    C,R = map(int,sys.stdin.readline().split())
    N = int(sys.stdin.readline())

    if N > R*C:
        print(0)
        return
    
    arr = [[0 for _ in range(C)] for _ in range(R)]

    d = [[1,0],[0,1],[-1,0],[0,-1]]

    cnt = 1

    di = 0
    y=0
    x=0

    while cnt <= R*C:
        if cnt == N:
            print("{0} {1}".format(x+1,y+1))
            #p(arr)
            return
        arr[y][x] = cnt
        cnt += 1

        ny = y + d[di][0]
        nx = x + d[di][1]

        if not (0<=ny<R and 0<=nx<C and arr[ny][nx] == 0):
            di = (di+1)%4
            ny = y + d[di][0]
            nx = x + d[di][1]
        
        y = ny
        x = nx
    
    return 0


main()
import sys

def main():
    arr = []

    N,M = map(int,sys.stdin.readline().split())

    ans = 0

    for _ in range(N):
        arr.append(sys.stdin.readline())

    for y in range(N):
        if arr[y][0] == '-': cnt = 1
        else : cnt = 0

        for x in range(1,M):
            if arr[y][x] != arr[y][x-1] and arr[y][x] == '-':
                cnt += 1
        ans += cnt
    
    for x in range(M):
        if arr[0][x] == '|' : cnt = 1
        else : cnt = 0
        for y in range(1,N):
            if arr[y][x] != arr[y-1][x] and arr[y][x] == '|':
                cnt += 1
        ans += cnt
    print(ans)
    return 0


main()
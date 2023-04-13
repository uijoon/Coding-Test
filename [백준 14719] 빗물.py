import sys

def main():
    H,W = [*map(int,sys.stdin.readline().split())]
    blocks = [*map(int,sys.stdin.readline().split())]

    ans = 0

    for i in range(1,W-1):
        left = max(blocks[:i])
        right = max(blocks[i+1:])

        lower = min(left,right)

        if blocks[i] < lower:
            ans += lower - blocks[i]
    print(ans)
    return 0


main()
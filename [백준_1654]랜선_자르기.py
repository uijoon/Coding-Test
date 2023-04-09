import sys

def main():
    K,N = map(int,sys.stdin.readline().split())

    lan = []

    for _ in range(K):
        lan.append(int(sys.stdin.readline()))
    
    start = 1

    end = max(lan)

    ans = 0

    while start <= end:
        cnt = 0
        mid = (start + end)//2
        for l in lan:
            cnt += l//mid
        if cnt >= N:
            ans = mid
            start = mid + 1
        else :
            end = mid - 1

    print(ans)
main()
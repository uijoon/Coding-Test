import sys

INF = 1e10

def main():

    N = int(sys.stdin.readline())
    SB = []
    ans = INF
    for _ in range(N):
        S,B = map(int,sys.stdin.readline().split())
        SB.append([S,B])
    
    for i in range(1,1<<N):
        S = 1
        B = 0
        for j in range(N):
            if i&(1<<j):
                S *= SB[j][0]
                B += SB[j][1]
        ans = min(ans,abs(S-B))
    print(ans)
    
   
main()
import sys
from heapq import heappush, heappop

def main():
    V,E = map(int,sys.stdin.readline().split())
    S = int(sys.stdin.readline())
    INF = 1e7
    node = {}
    for _ in range(E):
        start, end, dis = map(int,sys.stdin.readline().split())
        try:
            node[start].append([end,dis])
        except:
            node[start] = [[end,dis]]
    
    q = []
    dis = [INF for _ in range(V+1)]
    dis[S] = 0
    heappush(q,(0,S))
    
    while q:
        cur_dis, cur = heappop(q)

        if cur not in node.keys():
            continue

        for nex, nex_dis in node[cur]:
            nex_dis += cur_dis
            if dis[nex] > nex_dis:
                dis[nex] = nex_dis
                heappush(q,(nex_dis,nex))

    for d in dis[1:]:
        if d==INF:
            print("INF")
        else:
            print(d)

main()
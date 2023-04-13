import sys
from heapq import heappush, heappop

def union(node1 : int, node2 : int) -> None:
    global parents

    P1 = Find(node1)
    P2 = Find(node2)
    
    parents[P2] = P1
    return

def Find(node : int) -> int:
    global parents

    if parents[node] == node:
        return node
    
    else :
        P = Find(parents[node])
        parents[node] = P
        return P

def main():

    N,E = map(int,sys.stdin.readline().split())

    global parents
    parents = [i for i in range(N)]
    
    edge = []

    for _ in range(E):
        From,to,weight = list(map(int,sys.stdin.readline().split()))
        heappush(edge,(weight,From,to))

    ans = 0

    connected_edge = 0

    while connected_edge != N - 1:
        edge_distance, node1, node2 = heappop(edge)
        if Find(node1) != Find(node2):
            union(node1,node2)
            ans += edge_distance
            connected_edge += 1
    print(ans)
main()
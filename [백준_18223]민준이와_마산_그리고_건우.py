import sys
input = sys.stdin.readline
from heapq import heappush, heappop   

inf = 1e12

def main()->str:
    V,E,P = map(int,input().split()) # 노드 수, 간선 수, 건우가 버려진 곳

    graph = [{} for _ in range(V+1)]
    # list[dict, dict, dict.....]
    # graph[a]={b:c, d:e} 이면 a -> b의 거리가 c , a->d의 거리가 e

    for _ in range(E): # graph 정보 저장
        a,b,c = map(int,input().split()) 
        graph[a][b] = c
        graph[b][a] = c

    distance = [inf for _ in range(V+1)] # 노드별 최단거리 초기화
    distance[1] = 0 # 시작노드 초기화

    pq = []

    heappush(pq,[0,1,[1]]) # 현재까지 거리, 현재 노드, 현재 지나온 노드 list

    while pq:
        cur_dis,cur,cur_list = heappop(pq)
        
        if (cur == V) and (P in cur_list): # 현재 마산이고, 오는 길에 건우를 구한 상황
            return "SAVE HIM"
        
        for next_node in graph[cur].keys(): # 현재 노드와 연결되어 있는 노드들 탐색
            next_dis = cur_dis + graph[cur][next_node] # 현재까지 거리 + 다음 노드와의 거리

            if next_dis <= distance[next_node]: # 여러 최단 경로를 고려해야 하기 때문에 같거나 작을 때로 합니다.
                distance[next_node] = next_dis # 1->next_node의 거리를 갱신해줍니다.
                heappush(pq,[next_dis, next_node, cur_list+[next_node]])

    return "GOOD BYE" # 잘가 건우야..

print(main())
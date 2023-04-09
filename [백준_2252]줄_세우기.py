import sys
from collections import deque
    
def main():
    N,M = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)] # u->v일 경우 graph[u]에 v가 속함
    degree = [0 for _ in range(N+1)] # 노드별 degree
    degree[0] = 50000 # 노드는 1번부터 이므로
    answer = [] # 정답 list

    for _ in range(M):
        From, to = map(int,sys.stdin.readline().split())
        graph[From].append(to) # From->to
        degree[to] += 1 # to의 degree를 1 더해줌
    dq = deque()

    for i,d in enumerate(degree):
        if d==0:
            dq.append(i) # 진입차수가 0이면 노드를 dq에 넣어줌
            
    for _ in range(N):
        cur = dq.popleft() # 왼쪽부터 차례로 pop
        # print("cur : ",cur)
        answer.append(cur) # answer에 현재 노드를 추가

        for g in graph[cur]:
            degree[g] -= 1 # 현재 노드와 연결되어 있다면 진입차수 -1
            if degree[g] == 0: # 진입차수가 0이 됐다면
                dq.append(g) # dq에 삽입
           
                
    # print(answer)
    for i in range(N):
        print(answer[i],end = ' ') # answer 출력

main()
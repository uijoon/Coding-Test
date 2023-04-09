import sys
from queue import Queue

def main():
    N = int(sys.stdin.readline())
    Time = [0 for i in range(N+1)]
    indegree = [[] for _ in range(N+1)]
    degree = [[0,0] for _ in range(N + 1)] # [indegree,outdegree]
    ans = [0 for i in range(N+1)]
    for i in range(N):
        idx = i + 1
        node = list(map(int,sys.stdin.readline().split()))
        Time[idx] = node[0]
        if len(node) > 2:
            for indeg in node[1:-1]:
                degree[idx][0] += 1
                degree[indeg][1] += 1
                indegree[idx].append(indeg)
    
    q = Queue()
    for i in range(1,N+1):
        if degree[i][0] == 0:
            q.put(i)
            degree[i][0] = -1

    while not q.empty():
        cur = q.get()
        ans[cur] += Time[cur]

        for i in range(1,N+1):
            if cur in indegree[i]:
                degree[i][0] -=1
                ans[i] = max(ans[i],ans[cur])
                

        if q.empty():
            for i in range(1,N+1):
                if degree[i][0] == 0:
                    q.put(i)
                    degree[i][0] = -1
    for i in range(1,N+1):
        print(ans[i])
   
main()
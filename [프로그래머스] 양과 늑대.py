from collections import deque

def solution(info, edges):
    graph = {i:[] for i in range(len(info))}
    
    for p,c in edges:
        graph[p].append(c)
        
    dq = deque()
    dq.append( (0,1,0,[]) ) # 현재노드, 양 마리수, 늑대 마리수, 갈 수 있는 곳
    
    answer = 0
    
    while dq:
        node,sheep,wolf,left = dq.popleft()
        
        if wolf >= sheep:
            continue
        
        answer = max(answer,sheep)
            
        left = left + graph[node] #갈 수 있는 곳에 현재 노드의 자식 노드를 추가

        # print(f"cur : {node}, sheep:{sheep}, wolf : {wolf},left : {left}")
        
        for next_node in left:
            temp = left.copy()
            temp.remove(next_node) # 갈 수 있는 곳에서 다음 갈 노드를 제거
            
            dq.append((next_node,sheep+(info[next_node]+1)%2,wolf+info[next_node]%2,temp))
            
    return answer
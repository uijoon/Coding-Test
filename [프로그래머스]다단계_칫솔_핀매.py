import sys
sys.setrecursionlimit(100000)

graph = {} # parent : [child1,child2...]
result = {"-":0} # name:result
sell = {} # 이름:판매가격

def dfs(name):
    from_child = [] # 본인 판매 금액 + 자식 노드로부터 얻은 금액
    to_parent = [] # 부모 노드에 전달할 금액
    
    if name in sell.keys(): # 판매 실적이 있는 경우
        for price in sell[name]:
            to_parent.append(price//10)
            from_child.append(price-price//10)
    
    if name in graph.keys(): # 자식 노드가 있는 경우
        for child in graph[name]:
            result_child = dfs(child)
            for rc in result_child:
                if rc>=10:
                    to_parent.append(rc//10)
                from_child.append(rc-rc//10)
    
    result[name] = sum(from_child)
    
    return to_parent

def solution(enroll, referral, seller, amount):
    for name in enroll:
        result[name] = 0
        
    for name, price in zip(seller,amount):
        try:
            sell[name].append(price*100)
        except:
            sell[name] = []
            sell[name].append(price*100)
    
    for child,parent in zip(enroll,referral):
        try :
            graph[parent].append(child)
        except :
            graph[parent] = []
            graph[parent].append(child)
    temp = dfs("-")
    answer = [result[name] for name in enroll]
    return answer
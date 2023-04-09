class Node():
    def __init__(self):
        self.len = 0 # 현재 단어 길이
        self.data = False # 단어가 끝날 경우 True
        self.children = {} # 자식 노드
        self.num = 0 # 현재 노드를 지난 단어가 몇개인지

class Trie():
    def __init__(self):
        self.head = Node() # Root Node
    
    def insert(self,string):
        cur_node = self.head
        cur_len = 0

        for s in string: # Node마다 한글자씩 저장
            cur_node.num += 1 # 현재 노드를 지나는 단어 개수 추가
            cur_len += 1 # 현재까지의 길이 갱신
            if s not in cur_node.children: # 자식 노드에 처음들어오는 글자일 경우 Node를 만들어야함
                cur_node.children[s] = Node()   
            cur_node = cur_node.children[s] # 현재 노드를 자식 노드로 갱신
            cur_node.len = cur_len # 노드에 현재 길이 저장
        cur_node.num += 1
        cur_node.data = True  # 단어가 끝났으니 data를 True로 바꿈
        
    def search(self): # dfs 탐색
        cnt = 0
        stack = []
        stack.append(self.head)
        
        while stack:
            cur_node = stack.pop()
            
            if cur_node.num == 1: # 계속 탐색해도 나올 단어가 1개이므로 자동완성 가능
                cnt += cur_node.len
                continue
                
            if cur_node.data: # 현재 노드에서 끝나는 단어가 있는 경우
                cnt += cur_node.len
            
            for key in cur_node.children.keys():
                stack.append(cur_node.children[key])

        return cnt
        
def solution(words):
    trie = Trie()
    for w in words:
        trie.insert(w)
    answer = trie.search()
    return answer
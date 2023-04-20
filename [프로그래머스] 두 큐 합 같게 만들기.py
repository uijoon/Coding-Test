from collections import deque

def solution(queue1, queue2):
    answer = -2
    length = len(queue2) + len(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    S1 = sum(queue1)
    S2 = sum(queue2)
    S = S1 + S2
    
    for cnt in range(2*length):
        if S1 == S2:
            return cnt
        
        elif (S1 > S2) | (S2==0):
            element = queue1.popleft()
            S1 -= element
            queue2.append(element)
            S2 += element
            
        elif (S1 < S2) | (S1==0):
            element = queue2.popleft()
            S2 -= element
            queue1.append(element)
            S1 += element
    
    return -1
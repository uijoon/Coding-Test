def solution(s):
    answer = True
    
    s = list(s)
    s.reverse()
    stack = []
    while s:
        cur = s.pop()
        if len(stack)==0:
            stack.append(cur)
        elif (stack[-1]=='(') & (cur==')'):
            stack.pop()
        else :
            stack.append(cur)
        
    return True if len(stack)==0 else False
def solution(n, t, m, p):
    char = ['A','B','C','D','E','F']
    itos = {i:str(i) for i in range(10)}
    
    for i,c in zip(range(6),char):
        itos[10+i] = c # 10이 넘을 경우 A~F로 변환할 dict
        
    def change(n,num):
        result = ''
        while num != 0:
            result = itos[num%n] + result
            num //= n
        if result == '': # num=0 일 때, 빈문자열이 출력됨
            result = '0'
        return result
    
    answer = ''
    idx = 0 # 현재 인덱스
    num = 0 # str으로 변환할 숫자
    while len(answer) < t:
        cur = change(n,num) # 현재 숫자를 문자열로 변환
        for i,char in enumerate(cur):
            if (idx+i)%m == p-1: # 내 차례가 된다면 그 때 문자를 answer에 삽입
                answer += char
        idx += len(cur) # 현재 인덱스 갱신
        num += 1        # 다음 숫자로
    
    return answer[:t] # 문자열의 길이가 t를 넘어갈 수도 있음
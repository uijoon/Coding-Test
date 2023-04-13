import sys

def odd(n : str)->int: # 홀수 개수 계산
    func = lambda x : (int(x))%2 
    return sum(map(func,n)) # n을 str으로 받기 때문에 map 적용 가능

def dfs(n : str, cnt : int)->None: # n은 현재 숫자, cnt는 현재까지 홀수 개수
    global ans
    if len(n) == 1: # 자리수가 1이 된다면 최소, 최대값 갱신
        if cnt < ans[0]:
            ans[0] = cnt
        if cnt > ans[1]:
            ans[1] = cnt
    
    elif len(n) == 2: # 두 자리수는 각각 더해주면 된다
        next_n = str(int(n[0]) + int(n[1]))
        dfs(next_n,cnt+odd(next_n))
    
    else : # 세자리 수 이상일 경우 idx1, idx2로 구간을 나눠줌
        for idx1 in range(1,len(n)-1):
            for idx2 in range(idx1+1,len(n)):
                n1 = n[:idx1]
                n2 = n[idx1:idx2]
                n3 = n[idx2:]
                next_n = str(sum(map(int,(n1,n2,n3))))
                dfs(next_n,cnt+odd(next_n))
    return 

def main():
    global ans
    ans = [1e8,0] # min, max

    N = sys.stdin.readline().rstrip() # \n 제외하고 입력 받기

    dfs(N,odd(N)) # dfs함수를 통해 모든 구간을 탐색
    print(ans[0],ans[1])
main()
import sys
input = sys.stdin.readline
from collections import deque

def main() -> int:
    N = int(input())
    if N==1:
        return 1
    elif N==2:
        return 2 # 길이가 3 미만일 경우 N을 그대로 출력하면 됩니다.
    num = list(map(int,input().split()))

    num.sort() # 오름차순으로 정렬해줍니다.

    result = 2 # 길이가 3 미만인 수열은 항상 삼각 수열이므로 정답의 최소값은 2입니다.

    for first in range(N-2): # 입력받은 수열을 오름차순으로 탐색합니다.
        for third in range(N-1,first,-1): # 세번째 숫자를 내림차순으로 탐색합니다.
            if third-first < result: # 탐색 지점이 현재까지 찾은 최대 길이보다 짧아진다면 반복문을 빠져나옵니다.
                break
            if num[first] + num[first+1] > num[third]: 
                # 내림차순으로 탐색하며 조건을 만족하는 third를 찾았을 경우
                # 길이를 result에 저장해주고 반복문을 뺘져나옵니다.
                result = third - first + 1
                break
    return result

print(main())
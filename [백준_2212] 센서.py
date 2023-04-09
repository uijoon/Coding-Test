import sys
    
def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    arr.sort() # 센서의 좌표를 정렬해줍니다.

    dis = []
    for i in range(len(arr)-1):
        dis.append(arr[i+1]-arr[i]) # 인접한 센서의 거리를 list로 나타냅니다.
    if len(dis)==0:
        print(0)
        return 
    for k in range(K-1):
        '''
        거리를 빼는 것과 집중국을 하나 더 놓는 것과 동치입니다.
        거리가 큰 순으로 하나씩 빼면 수신 가능 영역의 길이를 최소화 할 수 있습니다.
        집중국 개수가 될 때까지 최대 거리를 빼줍니다.
        '''
        dis.pop(dis.index(max(dis)))
    
    else :
        print(sum(dis))
    
main()
def solution(n, m, x, y, r, c, k):
    answer = ''
    #x,y -> r,c 
    #좌상단이 1,1/ 우하단이 n,m
    #세로,가로  -> 2.3이 S
    diff = abs(x-r)+abs(y-c) # 목적지까지 최단거리
    print(diff)
    if diff%2!=k%2 or diff>k: # 최단거리보다 k가 짧거나, 홀짝 여부가 다를 때
        return 'impossible'
    #dlru 순서 

    rest = k-diff # 최단거리로 갔을 때 남는 거리
    lcount = 0
    rcount = 0
    dcount = 0
    ucount = 0

    if x<r : #내려가야함
        dcount = r-x
    else:
        ucount = x-r
    if y<c :
        rcount = c-y
    else:
        lcount = y-c

    # k-diff를 했으므로 rest는 항상 짝수
    dplus = min( n-max(x,r), rest//2)# 아래로 갈 수 있는 만큼 가기
    rest -= dplus*2 # 다시 위로 올라와야 하므로 x2 해줌

    lplus = min( min(y,c)-1, rest//2)# 왼쪽으로 갈 수 있는 만큼 가기
    rest -= lplus*2 # 다시 오른쪽으로 가야하므로 x2

    # rest가 남았다면 rl 반복해줌
    answer = 'd'*(dcount+dplus)+'l'*(lcount+lplus)+'rl'*(rest//2)+'r'*(rcount+lplus)+'u'*(dplus+ucount)



    return answer
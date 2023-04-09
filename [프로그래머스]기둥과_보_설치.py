# building 규칙
# 1 : 기둥, 2 : 보, 3: 겹치는 곳

# build_frame 규칙
# a : 0-기둥 1-보
# b : 0-삭제 1-설치

class Building():
    def __init__(self,n):
        self.n = n
        
        # 인덱스 에러 방지를 위해 한 칸씩 증가하여 만듬 (1,1) 부터 시작
        self.building = [[0 for _ in range(n+2)] for _ in range(n+2)]
        
    def input_(self,x,y,a,b):
        # 기둥 설치
        if (a==0) & (b==1):
            if self.insert_pillar(x+1,y+1):
                self.building[y+1][x+1] += 1
        # 보 설치
        elif (a==1) & (b==1):
            if self.insert_paper(x+1,y+1):
                self.building[y+1][x+1] += 2
        # 삭제
        elif b==0:
            self.delete(x+1,y+1,a)
    
    # 기둥을 설치할 수 있는지 확인하는 함수
    def insert_pillar(self,x,y):
        # 바닥에 있을 때, 보의 한쪽 끝 부분 위에 있을 때
        if (y==1)|(self.building[y][x-1] > 1) | (self.building[y][x] > 1):
            return True
        
        # 다른 기둥 위에 있을 때
        if self.building[y-1][x]%2 == 1:
            return True
        return False

    # 보를 설치할 수 있는지 확인하는 함수
    def insert_paper(self,x,y):
        # 보의 한쪽 끝이 기둥 위에 있을 경우
        if (self.building[y-1][x]%2 == 1) | (self.building[y-1][x+1]%2 == 1):
            return True
        
        # 보의 양쪽 끝이 다른 보와 열결될 때
        if (self.building[y][x-1]>1) & (self.building[y][x+1]>1):
            return True
        
        return False
    
    # 삭제 함수
    def delete(self,x,y,a):
        self.building[y][x] -= a+1 
        # 해당 위치의 기둥,보를 제거한 후 주변에 기둥과 보가 존재할 수 있는지 확인
        # building에서 기둥 1,보 2 이고 입력에는 기둥 0, 보 1이기 때문에 a+1을 빼줌
        
        dx = [-1,0,1,-1,0,1,-1,0,1]
        dy = [1,1,1,0,0,0,-1,-1,-1]
        # 상하좌우, 대각선, 현재 위치 확인
        
        for ddx,ddy in zip(dx,dy):
            ny = y+ddy
            nx = x+ddx
            
            # building의 값이 1 or 3 일 때 기둥이 있을 수 있는 지
            if self.building[ny][nx]%2 == 1:
                if not self.insert_pillar(nx,ny):
                    self.building[y][x] += a+1
                    # 안된다면 현재 자리에 뺐던 값을 다시 더해줘서 삭제 취소
                    return
            
            # building의 값이 2 or 3 일 때 보가 있을 수 있는지 
            if self.building[ny][nx]>1:
                if not self.insert_paper(nx,ny):
                    self.building[y][x] += a+1
                    # 안된다면 현재 자리에 뺐던 값을 다시 더해줘서 삭제 취소
                    return
    
    def output(self):
        answer = []
        # 출력 조건은 x가 작은 값부터, 기둥과 보가 둘 다 있을 경우 기둥 먼저
        for x in range(1,self.n+2):
            for y in  range(1,self.n+2):
                if self.building[y][x] == 3:   # 둘 다 존재
                    answer.append([x-1,y-1,0]) 
                    answer.append([x-1,y-1,1])
                    # 한 칸씩 밀어서 building에 저장했으므로 x-1, y-1 해줌
                    
                elif self.building[y][x] != 0:
                    answer.append([x-1,y-1,self.building[y][x]-1])
        return answer
        
def solution(n, build_frame):
    building = Building(n)
    for x,y,a,b in build_frame:
        building.input_(x,y,a,b)
    answer = building.output()
    return answer
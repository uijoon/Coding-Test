def solution(gems):
    category = len(set(gems)) # 보석의 총 종류
    gem_len = len(gems) # gems의 길이
    idx1,idx2 = 0, 0 # 초기 포인터 위치
    answer = [1,gem_len] # answer의 초기값은 전체 범위
    gem_dict = {gems[0] : 1} 
    
    while idx2<gem_len:
        if len(gem_dict) == category: # 보석 종류를 모두 포함하고 있을 때
            if answer[1] - answer[0] > idx2-idx1: # 현재 길이가 저장된 길이보다 작은지 확인
                answer = [idx1+1,idx2+1] # 정답 갱신
                
            gem_dict[gems[idx1]] -= 1 # 왼쪽 포인터의 보석을 1개 뺌
            if gem_dict[gems[idx1]] == 0: # 0이 된다면 key값에서 제외
                del(gem_dict[gems[idx1]])    
            idx1 += 1 # 왼쪽 포인터 오른쪽으로 한 칸 이동
            
        elif len(gem_dict) < category: # 보석 종류가 모자랄 때
            idx2 += 1 # 오른쪽 포인터를 오른쪽으로 한 칸 이동
            if idx2 >= gem_len: # 범위를 벗어났으면 break
                break
            try : # 옮긴 포인터에 속한 보석 개수 추가
                gem_dict[gems[idx2]] += 1
            except :
                gem_dict[gems[idx2]] = 1
    return answer
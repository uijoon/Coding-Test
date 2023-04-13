import sys

def phone_number(n : int)->str:
    """일관성 확인 함수

    Args:
        n (int): 전화번호의 수

    Returns:
        str: YES or NO
    """
    num_list = []
    for _ in range(n):
        num_list.append(sys.stdin.readline().rstrip())
    
    num_list.sort(reverse = True) # 뒤쪽부터 빼올 예정이므로 reverse=True
    while len(num_list)>1: # 하나만 남을 때까지 반복
        cur = num_list.pop() # 제일 뒤에서 번호를 pop
        if len(num_list[-1]) < len(cur): # 현재 번호가 다음 번호보다 길면 continue
            continue
        else :
            if num_list[-1][:len(cur)] == cur:
                # 다음 번호에서 현재 번호 길이만큼 떼서 비교
                # 같다면 일관성이 있으므로 NO 출력
                return "NO"
    return "YES"
    
def main():
    T = int(sys.stdin.readline()) # 테스트 케이스 입력
    for _ in range(T):
        n = int(sys.stdin.readline()) # 전화번호 개수 입력
        print(phone_number(n))
    
main()
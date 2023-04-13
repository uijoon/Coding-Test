def solution(record):
    answer = []
    id2nickname = {}
    
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter" or rec[0] == "Change":
            id2nickname[rec[1]] = rec[2]
    
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            answer.append(f"{id2nickname[rec[1]]}님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(f"{id2nickname[rec[1]]}님이 나갔습니다.")
        
            
    return answer
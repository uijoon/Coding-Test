
def solution(genres, plays):
    answer = []
    playlist = {}
    playcount = {}
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g not in playlist:
            playlist[g] = [(0,10001),(0,10001)]
            playcount[g] = 0
            
        if p>playlist[g][0][0]:
            playlist[g][1] = playlist[g][0]
            playlist[g][0] = (p,i)
            
        elif p>playlist[g][1][0]:
            playlist[g][1] = (p,i)
            
        playcount[g] += p 
    playcount = dict(sorted(playcount.items(), key = lambda x : -x[1])).keys()
    
    for key in playcount:
        for i in range(2):
            if playlist[key][i][1] != 10001:
                answer.append(playlist[key][i][1])
    
    return answer
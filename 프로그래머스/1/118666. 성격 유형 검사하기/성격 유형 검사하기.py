# (R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 1)
# 지표 4개, 각 2개 중 1
# n개의 질문 / 선택지 321 4_0 123 # 7-cho
# 지표별로 높은 점수 & 같으면 사전 순
# 비동의 동의

#2) 각 알파벳 딕셔너리화 ->"AN" 에서 앞/뒤에 문자 각각 가져와서 관련점수주기 

# 2) 점수 전부 for계산 후()-> 높은 점수 or 같으면
def solution(survey, choices):
    answer = ''
    score2=dict()
    score2=score2.fromkeys(["R","T","C","F","J","M","A","N"],0)
    # score=[[0]*2 for _ in range(4)]
    # up=set(("RT","CF","JM","AN"))
    mapp=[3,2,1, 0, 1,2,3]
    for q, cho in zip(survey, choices):
        if cho < 4:
            score2[q[0]]+=mapp[cho-1] # 비동의쪽 점수
#         if q in up :# 정방향 점수
#             mapp[cho-1]
#         else :# 역방향
        else : # 동의 쪽 점수
            score2[q[1]]+=mapp[cho-1] 
    
        #"RT","CF","JM","AN"
    answer+= "R" if score2["R"] >= score2["T"] else "T"
    answer+= "C" if score2["C"] >= score2["F"] else "F"
    answer+= "J" if score2["J"] >= score2["M"] else "M"
    answer+= "A" if score2["A"] >= score2["N"] else "N"
    return answer
# : 30m / 성능 +2 / 최대 0.20ms
# :: 이게 그래도 30m이나 걸리네. 담번에는 핵심 간단 알고리즘으로 한 방에 빨리 돌파하여 떠올릴 수 있도록 해보장.

# - 다른 사람 풀이 : 얼핏 봤는데 굳이

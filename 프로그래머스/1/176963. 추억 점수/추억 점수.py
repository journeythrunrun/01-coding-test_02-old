# 추억 점수_https://school.programmers.co.kr/learn/courses/30/lessons/176963
# name = 안빔 자연수, 중복 없
# yearning = 안빔 자연수
# photo = 안빔. 자연수 중복없

# - 실수 방지 : 주석으로 현재값 & 상태 # ["may",
# 통과 (1.40ms, 10.7MB)
def solution(name, yearning, photo):
    # 구현 속도 피지컬용 풀이
    target=dict(zip(name, yearning))
    answer_all=[]
    
    # !@ 없는 놈 나올 수 있구나 ㄷㄷ 
    for i in photo: #["may", "kein", "kain", "radi"]
        answer=0
        for j in i: # "may"
            answer+=target[j] if j in target else 0 
        answer_all.append(answer)
    return answer_all
# 해설[비슷]
# :나_딕셔너리 굿<-> 코드 압축용으로 index 쓰심
# 문자열 내림차순으로 배치하기_https://school.programmers.co.kr/learn/courses/30/lessons/12917

# 문자를 내림차순 정렬
# 대문자 < 소문자
# : 소문자 -> 대문자 
# ( 안 빔 )

# - sort // sorted 입출력형
# : 입력=리스트/츌력=없음 / reverse'd' //  입력= 반복형 / 출력=리스트/ revers'e'
# : 문자_오름차순 = 대문자부터
def solution(s):

    # 문자열로 합체
    # s.sort()
    return "".join(sorted(s, reverse=True))
    
# 해설 : 똑같
    
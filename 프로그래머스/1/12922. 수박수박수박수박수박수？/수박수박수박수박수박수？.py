# 수박수박수박수박수박수?_https://school.programmers.co.kr/learn/courses/30/lessons/12922

# - 문자열 concatenate 스킬
# 1*( ) # 괄호는 튜플화 아니고 연산용이라 제거처리됨.
# +1*( else "") 
def solution(n):
    # m : join / concate # 이전(어제)_<->관계들 머 있었징
    
    # m2) concate : *=+반복 /  +=[= <=> return] / 
    # if문 대체 및 concatenate 막기_ 1*("str" if ~ else "" ) # 공백 사용
    return "수박"*(n//2)+1*("수" if n%2!=0 else "")
    #"".join
    
# 해설[효율X? / 코드 스피드&간단화용]
# : 충분히 저장 후 slicing
# str = "수박"*n # n보다 적게 해도 될듯. 내 코드 만큼 아니더라도, //2 +1개 까지라도 충분히. (((물론 시복 동일_코드 스피드&간략화 위해 걍 저거도 ㄱㅊ)))
#     return str[:n]
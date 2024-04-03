# 문자열 내 p와 y의 개수_https://school.programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    # i) p, y 다 하나도 없 -> True
    # : count=0에 포함 ㄱㄴ

    # ii) p류 == y류 -> True / != False
    
    # other) 아스키 코드는 c언어만인듯 
    count=0
    for a in s :
        if a=='p' or a=='P':
            count+=1
        if a=='y' or a=='Y':
            count-=1
    if count==0:
        return True
    else :
        return False
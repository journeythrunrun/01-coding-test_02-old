# 이상한 문자 만들기_https://school.programmers.co.kr/learn/courses/30/lessons/12930
# '단어'의 짝수번째_대문자, 홀수_소문자
# ( s = 한 개 이상의 단어, 사이에 공백 무조건

#	23m_통과 (0.10ms, 10.3MB)
# - 대소문자 .lower()&.uppper() <-> 나_ord, chr 
def solution(s):
    # print(ord('a') - ord('A') ) # 32
    # s.split() # "    "도 다 먹음
    # m_other) ord로 zip으로 한번에 연산하면 더 효율화 될 수도
    
    # 굳이 이중? 했는데, 어차피 연산시복 똑같고 / 단어당 index 짧은 코드로 보려면 이중이 낫겠다. 
    # for a in range(len(s)):#'try'
    #     for j in range(len(a)):
    #         answer+=

    # str_ 요소 변경 안됨 -> concatenate 및
    answer=''
    count=0
    for i in range(len(s)):
        if s[i] !=' ': # 문자
            # 파이썬 이중 부등식(양꺽쇠) 안됨
            if count%2==0 and ord('a')<=ord(s[i]) and ord(s[i]) <=ord('z') : # 짝수_대문자 (대문자->대문자(미변경)/소문자[]>대문)
                answer+=chr( ord(s[i]) -32)
            elif count%2==1 and ord('A')<=ord(s[i]) and ord(s[i]) <=ord('Z') :
                answer+=chr( ord(s[i]) +32)
                
            else :
                answer+=s[i]
            count+=1
        else : 
            count=0
            answer+=s[i] # 공백도 그대로 붙여줘야
                
    return answer
# print(solution("a        a    abab  abab  "))
# 해설_ 시복 비슷해 보이는데 걍 코드압축. 굳이 초압축복잡코드 이해 패스
 # return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
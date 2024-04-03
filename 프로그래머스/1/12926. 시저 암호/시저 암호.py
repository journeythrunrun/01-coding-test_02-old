# z->a = %32 
# ' '->' '
# ( 입력= 비었을 수도 /요소_영어,공백 n=자연수) 


# print(ord('a')- ord('A')) # a~A가 32, ~a-~z=25!!!! ㅇㅅㅇ 

# 30m_	통과 (2.75ms, 10.2MB)
def solution(s, n):
    if len(s)==0:
        return ""
    # m_other) ord _ zip 으로 한번에 +32연산 등
    answer=''
    for a in s:
        if a==' ':
            answer+=' '
            continue
        # 놓쳤던 케이스_여러번 미는 중에 zZ초과한 경우 
        # : m1_%32? &  n?이용   => 소문자_ord('a')+( ord(a)+n -ord('a')  )%26 #0이 아니라 
        # : ~~ 첫+(direction+n칸-첫0)%4 # 첫+left #4==반복 주기
        # : m2_조건문 -한값 ## m1보다 구현 빠를 줄 알았는데, 실수하다가인가 오히려 더 꽤 걸림
        # _ 대문자 케이스
        
        # A Z a z
        if ord(a)+n > ord('z') and  ord('a')<=ord(a)  : # z넘김 & 소문자
            left=n - ( ord('z')-ord(a) ) # 3-1=2
            answer+= chr ( ord('a')-1+ left )
            continue
        elif ord(a)+n > ord('Z')  and ord(a)<=ord('Z') : # Z넘김 & 대문자
            left=n - ( ord('Z')-ord(a) ) # 3-1=2
            answer+= chr ( ord('A')-1+ left )
            continue
        #    
        answer+=chr( ord(a)-31 if a=='z' or a=='Z' else ord(a)+n  ) # z->a
    return answer

# 해설_ 내가 생각했던 m1_오히려 이 방법_수식 1개_speed > m2_조건문 복잡
# - ord('a')+( ord(a)+n -ord('a')  )%26 # 첫값+ 남은 이동 수 #남은 이동수= (초과해서 밀고 - 첫요소)% 주기=남은 


# > 대소문자 구분 = .isupper()
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower():
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)
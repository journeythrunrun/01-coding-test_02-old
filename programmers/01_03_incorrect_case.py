# z->a = %32
# ' '->' '
# ( 입력= 비었을 수도 /요소_영어,공백 n=자연수)


# print(ord('a')- ord('A')) # a~A가 32, ~a-~z=25!!!! ㅇㅅㅇ

# 30m_	통과 (2.75ms, 10.2MB)
def solution(s, n):
    if len(s) == 0:
        return ""
    # m_other) ord _ zip 으로 한번에 +32연산 등
    answer = ''
    for a in s:
        if a == ' ':
            answer += ' '
            continue
        # 놓쳤던 케이스_여러번 미는 중에 zZ초과한 경우
        # : m1_%32? &  n?이용   => 소문자_ord('a')+( ord(a)+n -ord('a')  )%26 #0이 아니라
        # : ~~ 첫+(direction+n칸-첫0)%4 # 첫+left #4==반복 주기
        # : m2_조건문 -한값 ## m1보다 구현 빠를 줄 알았는데, 실수하다가인가 오히려 더 꽤 걸림
        # _ 대문자 케이스

        # A Z a z
        if ord(a) + n > ord('z') and ord('a') <= ord(a):  # z넘김 & 소문자
            left = n - (ord('z') - ord(a))  # 3-1=2
            answer += chr(ord('a') - 1 + left)
            continue
        elif ord(a) + n > ord('Z') and ord(a) <= ord('Z'):  # Z넘김 & 대문자
            left = n - (ord('Z') - ord(a))  # 3-1=2
            answer += chr(ord('A') - 1 + left)
            continue
        #
        answer += chr(ord(a) - 31 if a == 'z' or a == 'Z' else ord(a) + n)  # z->a
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

# 문자열 내 마음대로 정렬하기_https://school.programmers.co.kr/learn/courses/30/lessons/12915
# # =>for a in zip? lambda? 의 a[n]
# # ( strings=안빔, 원소_소문자,안빈문자열 )
# # * 똑같을 경우 # 사전순

# # sort_디폴트_요소의 성분 전부에 대해서 정렬하는듯
# a=["111","101","110","100","011","010", "001", "000"]

# # a.sort(key=lambda x: x[0] )

# #1h _ 조건문 개더럽넹 i i+1 i+2 같다가 다를 떄 같다가 같을 때 등등_ 내가지금 sort알고리즘을
# def solution(strings, n):
#     strings.sort(key=lambda x: x[n] ) # 들어오는 각 비교대상 x에 대하여
#     old=''
#     target=[] # 중복 여러 개 ㄱㄴ>따로 저장&sort
#     i=0
#     old="1"
#     target2=[]
#     while (i<=len(strings)-1 -1 ):
#         if strings[i][n] == strings[i+1][n]: # 'e'"e"='e'
#             if strings[i+1][n]!=old : # 중복 중첩  # 처음엔 old_무조건 겹칠일없는거.
#                 target.append(strings[i]) #"abce"
#             target.append(strings[i+1])# "abcd"
#             if i==len(strings)-2: # 마지막 경우면.
#                 target2.extend(target.sort())
#             old=strings[i][n] # 이전중복 떴던 놈

#         elif old !=strings[i][n] :# and old !="1": #e/a "e"='j' # 다른 경우. 이전 중복 누적 값 확장 더해/없으면 알아서 아무것도안되겄지(빈배열 에러 안나)
#             if len(target)>=1: # 이전까지 중복되던 놈들 있었
#                 target2.extend(target.sort()) # 같은 놈들끼리 같은 행에.
#                 target=''

#             if i==len(strings)-3:
#                 target2.append(strings[i])
#                 target2.append(strings[i+1])

#             target2.append(strings[i])
#             #else : #strings[i][n]!=strings[i+1][n] : # (이전에 중복없)&이번 새롭

#         # 하나씩 훑지 말고 중복인 놈들만 따로 빼는 게 나았겠..
#         i+=1

#     return strings
# # print(solution(["zaca", "aacz", "cdx"]	,2))

# 해설
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))  # 정렬할 순위 순차적 가능_(x[n],x)
### 근데 조건문 저거 구현해보는 것도......다른 방법으로 풀 수 있는 거니까,일단 나중에 시간 나면 오답노트_구현력을 위해?

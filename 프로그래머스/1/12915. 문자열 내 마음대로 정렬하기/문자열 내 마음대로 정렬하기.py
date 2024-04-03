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
    return sorted(strings, key=lambda x:(x[n],x)) # 정렬할 순위 순차적 가능_(x[n],x)
### 근데 조건문 저거 구현해보는 것도......다른 방법으로 풀 수 있는 거니까,일단 나중에 시간 나면 오답노트_구현력을 위해?

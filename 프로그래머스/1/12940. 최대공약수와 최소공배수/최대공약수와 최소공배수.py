# 최대공약수와 최소공배수_https://school.programmers.co.kr/learn/courses/30/lessons/12940
# ->[최대공약수, 최소 공배수]
# (두 수_자연수) 

# 나_통과 (0.14ms, 10.2MB)_ 42m.. 구현 피지컬 딸림
# 코딜리티 함수_
def max_common(a,b):
    if a==b:
        return a
    if a>b:
        max_common(a-b,b)
    else:
        max_common(a,b-a)
# print(max_common(3, 12)) # 출력_ "마지막 탈출 함수의 리턴 값 = 미지정_None
        
def solution(n, m):
    answer=[1,1] 
    # 2] 3, 12-> 최대공약수=3 / 최소공배수=12
    # > 최대공약수 
    # : m1) 작은 수?의 최대 약수로부터 나머지 체크[경험적 서치가 빠를 수도]  
    # : m2 최대공약수 구하는 연산방식으로 부터[정석_수학배운방법이니 빠르려나 흠] 
    # > 최소 공배수: m2 or 시복허락하련지_최소부터 공배수 완전탐색
    
    #  
    minv, maxv=min(n,m), max(n,m) # 3, 12
    # down= (minv, maxv)  #~튜플
    
    while(1):##  각 니은자, 다음 / 니은자 종료==2)최대공약수 없을 때까지        
        exist=False
        ## 2) (한 니은 안에서)_최대공약수 한 개 구하기
        
        for aa in range(minv, 2  -1,-1 ): # 경계포함 3,2

            if minv%aa==0 and maxv%aa==0 : # (최대)공약수 존재# 3
                minv,maxv=minv//aa, maxv//aa # 1,4 # /하면 float형으로 반환해버림
                answer[0] *=aa # 1*3
                exist=True
                break  
        if exist==False:#  좌측 공약수 없다->최소공배수 # aa_1제외 됐나
            break
            
            
    return [answer[0],answer[0]*minv*maxv]
    # # m1_반
    # minv, maxv=min(n,m), max(n,m)
    # # 최대순 부터 약수 쳌
    # for aa in range(minv, int(minv**0.5)-1,-1 ): # 경계포함_25면 5 & 26이면 5
    #     if minv%a==0 and maxv%a==0 : # 공약수
    #         answer[0]=aa
    #         break
    
    
# - 해설_(0.01ms, 10MB)
# > Euclidean algorithm글, ..
# def solution(a, b):
#     c,d = max(a, b), min(a, b) # 3, 12
#     t = 1
#     while t>0:
#         t = c%d # 3%12=3  / 12%3=4
#         c, d = d, t # <- 12, 3 /
#     answer = [ c, int (a*b/c)]
#     return answer
        
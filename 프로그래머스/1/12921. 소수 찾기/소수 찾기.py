# 소수 찾기_https://school.programmers.co.kr/learn/courses/30/lessons/12921
# 소수 개수 반환
# n=자연수
# ~ 입출력 예에는 n포함햇네 흐음
    
    
# # 	1) 통과 (3056.98ms, 10.3MB) 2효율성테스트) 통과 (3107.16ms, 10.3MB)
# def solution(n):
#     count=0
#     while(n>1):# n=2, 3 # for이면 한줄이라도 아끼는데 그냥 구현속도. 끝값 생각하려면 while 생각이 더 빠를 때도. 이미 뇌 명확&생각난것대로함.
#         for a in range(2, int(n**0.5)+1): # 소수니#int # 경계값= n**0.5
#             if n%a==0 :
#                 break
#         else :
#             count+=1
            
#         n-=1
#     return count

# 해설 - 약 10배 빨라!_빠른 소수 검사
# : 	통과 (481.22ms, 113MB) /	통과 (580.43ms, 116MB) 
# : / 다시하면 	통과 (324.69ms, 115MB)나오기도. 편차가 1.5배정도 되기도 하네
def solution(n):
    num=set(range(2,n+1)) # 소수인지 검사 대상

    for i in range(2,n+1): # 소수인지 검사 대상
        # 한 줄에서 소수 아닌 놈들 여러 개씩 지우기 위함.
        if i in num: # 뒷줄에서 집합 원소 빼주는 지라, 이미 뺀 거 제외하려고.
            num-=set(range(2*i,n+1,i)) # 집합 빼기 # 약수의 배수들(비소수) 뺴기 # range_범위 초과하는 인덱스 알아서 pass해줌
    return len(num)

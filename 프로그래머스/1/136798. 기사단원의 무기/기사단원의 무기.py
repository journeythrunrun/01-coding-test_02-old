# 기사단원의 무기_https://school.programmers.co.kr/learn/courses/30/lessons/136798
# [1, number]
# 자신 번호의 약수 개수_의 무기 > 제한 수치보다 크면_기관이 정한 공격력power 무기 구매해야
# 공격력당의 철 -> 총 철

# 자연수. 
def solution(number, limit, power): # 5
    # 약수 개수 [1,2,2,3,2] > 
    
    # m1) 자신 번호의 약수 구하기 <- 값 범위에서, 자신 범호 범위까지 곱하면서 약수의 개수 얻기
    #    layer변경 조건충족case _ 모든조건충족, 문제의 end단계까지 따져.

    # : 생각 구현 더 오래걸려서 m2 
    # 1부터 101(limit+1) 까지 약수개수 세고, 101되면 limit화 
    # 1* number , 2의 배수 몇개[n//2]

    # !아 limit_ limit 까지만 이렇게 계산?
    # answer=0 #약수 1가지는 놈들 # 0으로 
    # for i in range(1,102): # [1,101] # 101
    #     answer+=number//i
    
    
    # m2)	통과 (4339.90ms, 10.3MB)
    answer=0
    for i in range(1, number+1): # 약수 개수 찾을 대상 5
        j=1 #! 약수소수/ 초기값 0아니고 1 / 경계값 think해라 
        count=0
        while(j<i**0.5): #이때까지 약수 소수,
            if i%j==0:
                count+=2
            j+=1
        if j==i**0.5:
            count+=1
        if limit < count : # 1)2)3) 특히 문제 길면, 단계 및 조건 다 체크 해라 
            answer+=power
        else :
            answer+=count
    return answer

# # 기사단원의 무기_https://school.programmers.co.kr/learn/courses/30/lessons/136798
# # 해설_ 2배면 시복 비슷 아닌가_통과 (2196.23ms, 11.1MB)
# # - 약수 _ 나중에 시간초과 문제 생기면 보기? 
# def cf(n): # 공약수 출력 
#     a = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i == 0:
#             a.append(n//i)
#             a.append(i)
#     return len(set(a))
# def solution(number, limit, power):
#     return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])
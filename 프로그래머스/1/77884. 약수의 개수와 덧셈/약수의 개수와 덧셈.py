# 약수의 개수와 덧셈_https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 요소_약수의 개수 짝수-> 더함  => len %2==0 
#  _ 홀수 -> 안 더해 

# - 문제 읽기 & 필기
# : 1) 문제 읽기 : '문장 단위로 이해'하면서( 눈으로 '예시와 같이' 보면서), '필기'
# : 1.i) 이해 100퍼 확실하지 않은 부분 있으면, 예시 설명 읽

# - 3]code 경계값 조건 생각하며. (<-> 후 엄밀체크 : 풀이 조금이라도 길어지면 or 다른 부분에서 실수한 거 있으면, 나중에 복잡해서 더 찾기 어려워져.)

# 2]_m) 약수의 개수_ 순차적 의미 계승 있? => 걍 효율 무시 일반 방법
def solution(left, right):
    answer=0
    for a in range(left, right+1): # 13, 17
        numb=0
        # 2] 경계값 포함해야 ( int(15**0.5) = 3 까지 봐야지[ (,+1까지) ] ) & 경계값_-=1
        for b in range(1, int(a**0.5) +1) : # 약수 ... 의 개수(_더 간단 알고리즘적혔을 수도_지금 굳이?) # m_제곱근 포함 & 후 -1 
            if a%b==0: # 약수인 경우
                numb+=2
        # 경계값 
        # if a**0.5 == int (a**0.5): # <  ==> while( k<n**0.5): 경계값 비포함 & 경계값_+=1
        if a**0.5 == b : # 경계값((제곱근_중복 피하기)) 
            numb-=1
    
        if numb %2 ==0 : # 짝수개
            answer+=a
        else : # (그 당시 이상한데 결과가 같아도) 옳은 코드로 원상복귀 해두기.
            answer-=a
        # 4] i) 오류시 : 문제_입출력 예 설명에 나오는 변수들 출력
        # print(a, numb) # 15가 4가아니라 2개가 떠버림 / 24가 8가 아니라 6떠버림
    return answer
            
# - 해설 : 나/root(n) 
# : 수학m_ 제곱근이 있는 숫자 = 약수가 홀수개다. (맞넹 내코드에서도 제곱근 조건이면 +2더하던 거에 -1해줬잖)
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer

    
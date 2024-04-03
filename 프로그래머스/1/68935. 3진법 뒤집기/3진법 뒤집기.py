# (풀기 오래걸림ㅜ_(0.04ms, 10.3MB)_가능 다양 방법 시도 하다가 시간 더걸린다. )
# 3진법 뒤집기_https://school.programmers.co.kr/learn/courses/30/lessons/68935

# 3진법 -> 앞뒤 뒤집 > 10진법

def solution(n):                
    # 
    # (100 40 이 아니라 1 4 를 구하려는 거)
    # 2] m_수식 양변 조작해서 계수 찾기_'수식'에서 '양변에 연산 취해서' ' 계수 구하기'  # 연산 == % //로 떨구는 방법도 있음
    # :10진법 45 =10^2 *0 10(^ (1)) *4 + (10^0)*5
    # : (( 100으로 나누면 뒤에 45가 나오는 식 > 몇자리인지 찾기 귀찮으니 뒷부분부터하자
    
    # 2] m_X너무 45 같은 case로만 fit하다가는 앞뒤 상황 반영 안되기도.
    # 10으로 나눈 나머지 =5 #! 원랜 이전 것들 다인데, 이전 것들이 한개라. 
    # 10으로 나눈 몫 = 4
    # 100으로 나눈 몫 = 45 == n
    # if 100으로 나눈 나머지==n : break
    
    # 3진법 45= (3^3)*1+3^2 *2 +3^1 *"0" + 3^0 *0 # 10(^ (1)) *4 + (10^0)*5
    last=[str(n%3)] 
    i=1
    #left=n
    while(1):
        # 조건문을 앞에 했어야 아까도
        if n%(3**i)==n: 
            break
        #left-=last[-1]*(3** (i-1) ) # 140
        
        #last.append( left  //(3**i)) # \
        #b%(2**(i+1) ) //(2**(i)) 
        last.append( str (  n%(3**(i+1)) //(3**(i))  )) # %[ 인덱스부터 위쪽 날려 (145면 45)] //[인덱스부터 아래쪽 날려 (145면 14)] 
        
        i+=1
    
    #['0',0,2,1] 
    return int(''.join(last),3) # 시간초과_다른 거 봄
    
    # i=1
    # # 
    # while(1):
    #     #-last[0] 
    #     last.append(n%(3** (i) ) ) # 45//(10^1) =4
    #     #last=[ n//3**i for i in ]
    #     total+=last[-1]*3**i # 4* 10^1
    #     if total==n:
    #         break
    #     i+=1
    # print(last)
    # return 1
     
        
    
#    
#     i=1
#     last=[n%10] 
#     n-=last[0]
#     while(1):
#         n%(3**(i+1) )
#         i+=1
#         if a==0:
#             break
#     # -> 3진법 45= 3(^3)*1+
#     last=[n%3]  # 0
#     # 45//9=
#     while(1):
#         #-last[0] 
#         last.append(n//(3** (i) ) ) # //100 - 5 = 45 - 5 =40
#     print
        
#     for j in range(len(last), ):
#         answer=last[j]

# # 해설
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer
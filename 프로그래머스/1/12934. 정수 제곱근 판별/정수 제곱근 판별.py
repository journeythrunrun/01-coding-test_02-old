#정수 제곱근 판별_https://school.programmers.co.kr/learn/courses/30/lessons/12934
# x의 제곱 -> (x+1)**2
# != -> -1
def solution(n):    
    #m1_ 제곱 쪽일 n에 root를 씌운 후 정수인지 보기.
    # 정수판별= 1로 나눈 나머지가 0인지
    if n**0.5%1 == 0 : # 정수란 것
        return (n**0.5+1)**2
    else :
        return -1

#     # m2    
#     x=1
#     while(x<= n**0.5):
#         if x==n**0.5:
#             return (x+1)**2
#         x+=1
        
#     return -1
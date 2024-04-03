# 부족한 금액 계산하기_https://school.programmers.co.kr/learn/courses/30/lessons/82612
# N 번째 이용 : price*N
# 모자람 -> count 번에서 얼마가 모자라는지
# 안모자람 -> 0

# (가격 자연수, 자금 자연수, 횟수 자연수 )
def solution(price, money, count):
    # money - ( 4*price + 3*price + 2*price + price )
    a=money- ( count *(price + count*price )/2 ) #  1,2..든 / *price까지든 등차수열. ((price 뽑아주면 아주 조금 더 효율인데 굳이))

    # 했던 실수_연산 때 * 붙이기! (특히 *(       
    return abs(a) if a <0 else 0  
    
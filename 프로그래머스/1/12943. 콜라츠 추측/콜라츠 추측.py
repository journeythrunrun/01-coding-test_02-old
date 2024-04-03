# 콜라츠 추측_https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 500번 반복 후 아직 1 아니면 -> -1
# 몇 번 반복해야?
def solution(num):

    if num==1 : 
        return 0
    for i in range(500):
        if num%2==0:
            num/=2
        else :
            num=num*3+1
        if num==1:
            return i+1
    
    return -1
# 해설_별 차이 없음
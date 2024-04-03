# 크기가 작은 부분문자열_https://school.programmers.co.kr/learn/courses/30/lessons/147355
# count_수<=수

#_	통과 (6.00ms, 10.3MB)
def solution(t, p):

    pp=int(p)
    count=0
    for i in range( len(t) - ( len(p) -1)  ): # 7 3 -> 5
        count+=1 if int(t[i:i+len(p)])<=pp else 0# len 개
    
    return count
# 해설[같]
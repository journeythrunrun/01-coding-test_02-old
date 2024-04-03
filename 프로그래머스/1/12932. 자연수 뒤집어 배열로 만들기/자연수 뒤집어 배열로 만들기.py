# 자연수 뒤집어 배열로 만들기_https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    nn=str(n)
    answer=[]
    # answer.extend(int(nn[k] ) for k in range(len(nn)-1,-1,-1))
    
    for i in nn[::-1]:
        answer.append(int(i))

    
    return answer
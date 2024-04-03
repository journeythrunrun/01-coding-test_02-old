# 모의고사_https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 12345
# 21 22pass 23 24 25 / 21
# 33 11 22 44 55/
# 앗 수포자 3명만 있다. 일반화 패턴 내가 찾아내는 거 아님
# _*최고득점 여럿일 경우,

# _*빈배열 : 자동처리, print로 체크
def solution(answers):
    # answer-aa -># m1) not 연산자로 정답일 0케이스를 1로 하고 나머지 다 0으로 한다음에 sum하는 방법

    # m2) 단순 for_구현속도 빠르려나	통과 (4.47ms, 10.3MB)
    a=[1,2,3,4,5]
    b=[2,1 , 2,3, 2,4, 2,5]
    c=[3,3, 1,1, 2,2, 4,4, 5,5]
    
    answer1=[[0,1],[0,2],[0,3]]# 힙큐 
    for i in range(len(answers)):# 에라이 s한글자 오타
        answer1[0][0]+=1if a[i%5]==answers[i] else 0# [0]없을 때TypeError: 'int' object is not iterable
        answer1[1][0]+=1 if b[i%8]== answers[i] else 0
        answer1[2][0]+=1 if c[i%10]== answers[i] else 0 
    
    #answer1.sort() ##변수이름 안 겹치게
    answer1=sorted(answer1,key=lambda x:x[0]) #x_각 행 한개씩 받네 # x[0]이든 x든 됨.2열 이미 정렬돼있어서.
    
    #역순
    if answer1[-1][0]==answer1[-2][0]: ## 변수명 겹친다. result같은 일반폼 말고 의미 무조건 담자. 
        result=[ answer1[-2][1],answer1[-1][1] ]
        if  answer1[-2][0]==answer1[-3][0]:
            result=[answer1[-3][1], answer1[-2][1],answer1[-1][1] ]
    else :
        result=[answer1[-1][1]] # 고득점자

    # !조건 틀림 # if 속 if 여야
    # for j in range(2): 
        # if answer1[-(j+1)][0]==answer1[-(j+2)][0] :
        #     result.append(answer1[-(j+2)][1])
        
    return result
# - 해설_GOod_내 정렬보다 낫다(3개밖에 없긴 해도)
# - 딴 점수를 max값과 각각 다 비교 
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

    
# 서울에서 김서방 찾기_https://school.programmers.co.kr/learn/courses/30/lessons/12919
# kim 위치 찾기 

def solution(seoul):
    # join _입력=반복 객체(5) 1개 & 모든 요소가 str형 => 출력=str ( 반복객체형의 '요소'가 str형이면, 반복객체형 껍질 벗고 str가져와서 str반환 )
    for i, a in enumerate(seoul):
        if  a=="Kim":
            return str(i).join(["김서방은 ","에 있다" ] ) 
    
# - 해설 : index 사용_ 코드 짧은 대신 더 느려
    # return "김서방은 {}에 있다".format(seoul.index('Kim'))
# 빵1 – 야채2 – 고기3 - 빵1
# -> 햄버거 수

# 2) 길이 김 -> 1,000,000 시복
# m1 for n 하며, 새 세트 시작마다 old에 append
# i)1_len(old[-1])!=3 : 1 append / else : answer+=1;  
# ii) 2 and 

# 2핵심) len(old(-1)) check & 조건에 맞을 때 append
def solution(ingredient):
    answer = 0
    old=[] # m2 list index 방지용 [1,0,0,0]
    for numb in ingredient : 
        if numb == 1:
            if len(old)==0 or len(old[-1])!=3 : # 길이 3 있는 거 아니면 무조건 새 old화
                old.append([1])
            else : # 길이 3 
                answer+=1
                old.pop()
        elif numb==2: #
            if len(old)!=0 and len(old[-1])==1:
                old[-1].append(2) ## 나중에 출력 확인용으로 굳이 123 맞게 넣음
            else :
                old=[]# 전부 제거 
        else : # 3
            if len(old)!=0 and len(old[-1])==2:
                old[-1].append(3)
            else :
                old=[]            
    return answer
# : 22m / 성능 +8 / 최대 174.30ms

# - 문법 : 리스트 old=[] 재정의 됨
# - 리스트 인덱스 초과 케이스 방지법 : 조건문 추가
# : if ""len(old)!=0 and""  len(old[-1])==2: # ((파이썬에서는 앞에서 위배면 넘기기 때문임))

# - 다른 사람 풀이
# > 시복은 내가 더 나을 수도 있음(시복은 똑같고 미세하게 나을 수도 있겠다.) (저장/형식/함수에 따른 차이는 모름 ) / but 이 사람풀이가 더 멋진 것 같기도 함. 무엇보다 풀이 빠르겠다. 
# > 무조건 append & 매번 최근 4개 한꺼번에 다 비교 
# :  if s[-4:] == [1, 2, 3, 1]: 

    # for i in ingredient:
    #     s.append(i)
    #     if s[-4:] == [1, 2, 3, 1]:
    #         cnt += 1
    #         for i in range(4):
    #             s.pop()
# [1] eddieK , 최종오 , 김태일 , Jin-s-work 외 257 명
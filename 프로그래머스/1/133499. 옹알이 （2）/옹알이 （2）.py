# 네 가지 발음, 조합, 연속 x
# "aya", "ye", "woo", "ma" 
# 술먹고 코딩 하는 거라 좀 더 걸리는 거일 수도 있음
me=-1
# passs=0
# 재귀함수 : 함수 종료시, 함수 내 그 다음 라인진행 주의. <->(나는 while 탈출처럼 생각해버림) 
# (적은 수정을 위해)-> 새 함수 내 'while'화 & 'return' 한 방 탈출 >= '재귀' & 'passs변수 및 무조건 탈출 조건' 추가 

def ha(left):
    while (1):    
        global me, passs
        # print(left, passs)
        
        # if passs==1:
        #     return 1
        # 추후 조건문 위해 2개 짜리 단어 먼저체크
        
        # 탈출 : 남은 문자열에서 가능한 단어 나올 수 없는 조건 
        if len(left) <= 1 :
            return 0    
        
        # me : 단어 연속 등장인지 체크 / 바로 이전 각 단어 케이스 0,1,2,3 으로 구별
        if left[0]=='y' and left[1]=='e' and me !=0 :
            
            if len(left)==2: # 바로 위 조건 통과했어서 이미 길이 2 이상 & ye만족인데 남은 길이가 2면 딱 마지막인거.
                # passs=1
                return 1 # <-> 1의미 없 재귀에서는
            me=0
            left=left[2:]
            continue

        if left[0]=='m' and left[1]=='a' and me!=1 :
            if len(left)==2: 
                # passs=1          
                return 1
            me=1
            left=left[2:]
            continue

        if len(left) <=2 :
            return 0

        if left[0]=='w' and left[1]=='o' and left[2]=='o'and me!=2:
            if len(left)==3: 
                # passs=1
                return 1
            me=2
            left=left[3:]
            continue


        if left[0]=='a' and left[1]=='y' and left[2]=='a' and me!=3:
            if len(left)==3: 
                # passs=1
                return 1
            me=3
            left=left[3:] 
            continue
        return 0

def solution(babbling):
    global me, passs
    answer = 0
    for a in babbling : ##룰루난나 코딩 ㅎㅋㅋㅋ
        ## 집쭈웅
        ## 6) a _ ayaye
        ## 함수 재귀 # 최종 미선택 m
        
        if ha(a)==1:
            answer+=1
        me =-1
        # passs=0
        
    return answer


# - 다른 풀이( 문제들 다른 사람들 코딩보니까 난 완전 lowlowlow(계층적)코딩이넼)
# > 3) in ['aya'  # 문자열 뭉텅이 단위도 가능.
# > 3) i =i.replace_반환형
# > 2) 굿 : 우왕 발음 가능한 단어 지우고 -> 남은 문자 길이 체크 알고리즘 굿[1]
# > 10) 실행 속도 빠름
# def solution(babbling):
#     answer = 0
#     for i in babbling:
#         for j in ['aya','ye','woo','ma']: # 3)
#             if j*2 not in i: # 중복 조건 체크 : 문자열concat
#                 i=i.replace(j,' ') # ''말고 띄어 쓰기로는 하네
#         if len(i.strip())==0: # [1]
#             answer +=1
#     return answer
# [1] ( 전지훈 , 단재 , eunseo.thatsme@gmail.com , 권영수 외 53 명)

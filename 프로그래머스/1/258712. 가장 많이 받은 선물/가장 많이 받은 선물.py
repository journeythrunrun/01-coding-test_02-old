# 0)
# friends_중복없음	gifts_주고받은놈이 서로 같은 경우 없음	result
# ["muzi", "ryan", "frodo", "neo"]	["muzi_준놈 frodo_받은놈", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]	2


# 12) 규칙대로 다음 달에 선물을 주고 받음
# if) 두 사람 선물 교환 기록 있음 : 이번달까지 더 많이 준 사람 : 다음달에 선물 1개 받음
#   ) 교환 경험 없음 or 서로 주고받은 수 같음 :
# XX 이건 앞 단 if문 가정 얘기 좀 했던거였음_ i서로 교환 경험없음?? 같은 수로 선물 주고받았음? : B가 1개 받음 # 말이 상충되는 거 같은데 조건 누적 덮어쓰기인가 중의적 표현인가

# _ii선물지수 큰 사람 : 더 작은 사람에게 받음 
# _iii선물지수 같으면 : 다음달에 선물주고받지 않음
# : 선물 지수 : 이번달까지 준 선물의 수 - 받은 선물의 수
# XX_ A,B선물지수_초기값==(주고받은 적이 아예 없음)

# -> 다음달에 가장 많은 선물 받는 친구_

# 3) friends_딕셔너리화 -> 선물 받을때 count+=1 -> 딕셔너리 max

from itertools import combinations 
def solution(friends, gifts):
    answer=[[0,0] for _ in range( len(friends)) ] #[0,0]*len(friends)_이건concate 주의!해라잉_*는 리스트 껍질 한 개 벗기고 연장 # 준 수, 받은수 # 막판 sort를 위해 리스트 # 예전 fromkeys에서처럼 주소 복사 아니겄지_0을 복사하는 원래 기본꼴 형태 비슷이라 ㄱㅊ할듯
    answer2=[[0,0] for _ in range( len(friends)) ] # 줄 수, 받을 수 # 코드편집 스피드를 위해 복사 사용한 형식
    dict1=dict()
    dict1=dict(zip( friends,range(len(friends)) ) ) # 리스트의 idx를 딕셔너리에서
    dict2=dict()# 두 사람 간 주고 받은 수 ~> 준 숫자
    # m_두 사람 간의 교환 기록 : 알파벳순의 딕셔너리 -> 그 순서의 값 
    # : 그냥 따로 저장할 걸 그랬나 암튼
    for trade in gifts :
        tralist = trade.split()# 이미 리스트
        answer[ dict1[ tralist[0] ] ][0]+=1  # 준 수
        answer[dict1[ tralist[1] ]][1]+=1 # 받은 수 

        # target=tralist[0]+tralist[1]
        tralist.sort() #리스트 문자열 정렬 # 여기까진 ab순
        ## 아래 왠지 뒤집히네
        reverse= False if tralist[0]==trade.split()[0] else True # 나중 활용
        target=tralist[0]+tralist[1] #if reverse==False else tralist[1]+tralist[0] # 이미 sort했는데 trade에서로 안하고 이미 sort한 tralist에서 가져다 붙여써버림. 방버 여러 개 생각하다가 둘다써버렸네
        
        if dict2.get(target,'a')=='a' : # 교환 기록 없음 -> 첫 1
            dict2[target]= [1,0] if reverse==False else [0,1] 
        else : # 교환 기록 있음
            dict2[target][0 if reverse==False else 1]+=1 # 준 기록 저장
    # list(combinations(friends,2))시복 병렬아닌가
    present=[] #[0] * len(friends) # for _ in range( len(friends)) ] #~
    for person in friends :
        # 선물지수 굳이 계산 미리 _ 콤비 최악케이스보단 낫다
        present.append(answer[dict1[ person ]][0] - answer[dict1[ person ]][1]) # 실화냐 [0] [0] ->[1] ##### 둘다 초기화돼있어서 없을리는 없음
    # print('present',present) # 마지막 예시에서만 맞던거임. 보통 일반적인 케이스/몇 케이스에서의 출력 일치 확인

    
    for istra in combinations(friends,2): 
#     for person in friends : # 사람들 대상 추가로 받는 수만 조사
        istra=list(istra) 
        istra.sort()
        passs=False
        if dict2.get(istra[0]+istra[1],'a')!='a': # if) 두 사람 선물 교환 기록 있음 : 이번달까지 더 많이 준 사람 : 다음달에 선물 1개 받음
            A, B =dict2[ istra[0]+istra[1] ] # 준 수 비교
            if A>B :
                answer2[dict1[ istra[0] ]][1]+=1 
                ## answer[dict1[ istra[0] if A>B else istra[1] ]][1]+=1 # 받은 수 up ## elif
                passs=True
            elif A<B:
                answer2[dict1[ istra[1] ]][1]+=1 
                passs=True
            # else : # 같음
            #     answer[]
        # muzi neo한테 못받았지왜
        if passs==False : # 초기화 흐름에 의해 교환기록 없는것도 포함됨. # else : #   ) 교환 경험 없음 or 서로 주고받은 수 같음 :
            # print(1)
            if present[dict1[ istra[0] ]] > present[dict1[ istra[1] ]]:#    answer[dict1[ istra[0] ]][1]+=1 
                # answer2[dict1[ istra[0] ]][1]+=1
                answer2[dict1[ istra[0] ]][1]+= 1
                
                # print('선물_앞큼') # neo ryan때 왜 r값 안오르징 # 여기로는 건 다른 1출력 착각오는뎅
            elif present[dict1[ istra[0] ]] < present[dict1[ istra[1] ]]:
                answer2[dict1[ istra[1] ]][1]+=1 
                # print('선물_다름')
            else : # 같으면
                # print('선물_same')
                pass
        # print(istra, answer2)

    # _ii선물지수 큰 사람 : 더 작은 사람에게 받음 
    # _iii선물지수 같으면 : 다음달에 선물주고받지 않음
    # : 선물 지수 : 이번달까지 준 선물의 수 - 받은 선물의 수
    # XX__elif) A,B선물지수_초기값(주고받은 적이 아예 없음)
    answer2.sort(reverse=True, key=lambda x : x[1])  # max O(n)이 낫지만 어차피 시복 범위가 더 커서 걍 빠른 코드사용.
    # print(answer2)
    
    return answer2[0][1]
   
    
# - 오래 걸린 이유1h 43m + 디버깅 35분?(반영_문제/데이터 형식/내코드변수 다시 이해 반영)  / 근데 +1점이었나?  /(22.50ms, 11MB)
# 1) 데이터 형식 확실히 몰라서(가끔은 비익숙한 부분) ( 형식 관련 출력 및 디버깅 )
# 2) 문제 정리 : 15m ㄷㄷ
# 3) 너어무 길게 정리하다가, 핵심 논리 설계를 위한 핵심 조건만의 틀이 머리에 잘 안들어옴

# - 디버깅: 내일 이어서 ( 논리 구현에 필요한 저장 및 연산은 성공해놨으니, 배치 수정 정도하면 되겄징)
# : 대충 결과 값봐서는 문제를 다르게 이해한듯 연산 배치 이동 <- 중간출력비교 
# > '이미' 받은 수, '다음달' 받은 수=받을 수 : answer2 추가
# ; 수행한 핵심알고리즘 하나하나 체크해보기?

# > [0] - [1] 인데 -[0]했었.
# * 복붙할 때 '2)바꿔야 하는 거' 수정
# > ab ba가 알파벳순으로해서 한 순서로가 안됐네 

# : 이미 sort했는데 다른 방법으로도 이중 뒤집어버림
# -> *핵심 알고리즘 하나하나 출력 확인
# -> *예시에서 준 정보 출력 비교 빠름
#  * 마지막 예시에서만 맞던거임. 보통 일반적인 케이스/몇 케이스에서의 출력 일치 확인

# - 다른 사람 코드 : 내가 1.5배 정도 빠르기도 한듯 (max_37.80ms)
# > 이 부분은 내가 시복은 나을듯
#   나_키_교환자 같을 시 두 사람이름 오름차순 합쳐서 값_[알파벳 앞놈이 준?수, 알파벳 뒷놈이 준?수 ]저장 <-> 상대_ trade시 사람이름 계속 append 저장 -> for2개 안에서 사람이름 카운트

# > 딕셔너리도 컴프리헨션?되나봄
# : {어엄:[엄준식-엄준식] for 어엄 in 엄} 
# > 나_present_새로 for 및 저장 <-> 마지막 for문 안에서 계산 (가장 복잡 최악 케이스 방지 위해 내 방법 썼었음)

# def solution(엄, 준식):
#     엄준식=int(not []) # 왜 일케 한거즤 걍 1뜸
#     어떻게사람이름이={어엄:[엄준식-엄준식] for 어엄 in 엄} # 딕셔너리에 0을 for로 저장 
#     식 = len(엄)
#     엄준식화이팅 = [엄준식-엄준식]*식
#     for 어엄준식 in 준식:

#         어엄준식 = 어엄준식.split()
#         어떻게사람이름이[어엄준식[엄준식-엄준식]].append(어엄준식[엄준식]) # A.1) 딕셔너리_준사람키_ 받은 사람 이름 append.
#         어떻게사람이름이[어엄준식[엄준식-엄준식]][엄준식-엄준식]+=엄준식 # 준놈 수+1
#         어떻게사람이름이[어엄준식[엄준식]][엄준식-엄준식]-=엄준식 # 받은놈 -=1

#     for 준 in range(식): # 사람 총 명수
#         for 주운 in range(준+엄준식,식): # combination구현. 
#             if 어떻게사람이름이[엄[준]].count(엄[주운])==어떻게사람이름이[엄[주운]].count(엄[준]): # 상대 명수 서로 찾기 # A.2) 문자열을 찾아서 count하네
#                 if 어떻게사람이름이[엄[준]][엄준식-엄준식]>어떻게사람이름이[엄[주운]][엄준식-엄준식]:
#                     엄준식화이팅[준]+=엄준식
#                 elif 어떻게사람이름이[엄[준]][엄준식-엄준식]<어떻게사람이름이[엄[주운]][엄준식-엄준식]:
#                     엄준식화이팅[주운]+=엄준식
#             elif 어떻게사람이름이[엄[준]].count(엄[주운])>어떻게사람이름이[엄[주운]].count(엄[준]):
#                 엄준식화이팅[준]+=엄준식
#             else:
#                 엄준식화이팅[주운]+=엄준식
#     return max(엄준식화이팅)
# # [1] 코딩하는엄준식
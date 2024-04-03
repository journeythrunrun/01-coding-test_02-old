# 1)
# -> 미완수자 이름 return
# : 미완수자 딱 1명  
# 4) 동명이인 -> 딕셔너리에 값 저장
# 4) 100,000명 이하 -> 딕셔너리
# 4) 한 쪽 비어있기 -> check

# Again 2)
# for in completion_딕셔너리에 명수1과함께 집어넣기_이미 있으면+=1 -> for in participant_-1 및 더이상없으면return

# 2)
# : 딕셔너리
def solution(participant, completion):
    answer = ''
    dict1={}
    dict1=dict1.fromkeys(completion, 0) # 중복 명수 때문에 어차피 for 돌아야해서 걍 이거 없이 추가해도 되긴함.
    
    for a in completion :
        dict1[a]+=1
        # try :
        #     dict1[a]
        # except :
        #     dict1[a]=1
        # # if dict1[a]>=1: # 할당 전에 값 비교 시 인덱스 사용이라 keyError(이건 =할당 아니고 비교잖슴.) -> setdefault(key,없으면-1) OR get(key, 없으면-1)
        #     # print(dict1)
        # else :
        #     dict1[a]+=1 
            
    for a in participant :
        # 없을 때 -1 일때
        if (a not in dict1) or dict1[a]==0: # or  ( 이미 1 빼서 count값이 다시 0돼있을 때. )
            answer=a
            break
        dict1[a]-=1
        
    return answer


# : 18m / 성능 +2 & 최대 60ms

# Again)
# - 딕셔너리 정리 및 복습
# >> 1긴 딕셔너리 생성
# : 1) target=dict(zip( key_list, value_list)) # dict( 키벨류 연속 )
# : 2) 동일값 저장 x=dict1.fromkeys( list_keys,3_으로저장) # 반환형들! # value는 한 덩어리만 동일하게 들어감 _디폴트 None
# >> 2수정&없으면 추가 
# : 1) dict1["new"]=1 # 큰 따옴표 안 하면 변수명으로 인식
# : 2.1) x.update( {1: 'sa' , 3:'a'}) # (딕셔너리)
# : 2.2) x.update([  [2,'aa'], [3, 'bb'] ])  #  입력 : 2차원 행열 /  각 행 =[키, 벨류]  
# : > x.update( zip ([2,3], ['aa','bb']) ) # zip활용 zip( [키,키], [벨류,벨류] )_ zip_튜플 

# 셋겟 _3개 getㅎ
# >> 3에러 없는 조회 & 없으면 원하는 값 "저장"&반환 ㄱㄴ
# : 1) dict1.setdefault(key, 11) # 가진 value 출력, 없는 키면 11 저장 & 출력
# >> 4조회만
# : i) x.get('a',0) # value 출력, 없는 키면 에러 없이 0 출력

# - 다른 자 풀이 
# : collections.Counter(~~) 사용법
# >
    # return list(answer.keys())[0] 
    # 카운터형 속 딕셔너리에서 ".keys를 가져온 후" "list 씌우고" -> 하나 있는 원소 "[0]"호출
    # answer : 카운터형 ( 딕셔너리 : 0카운팅수)
    # answer.keys() :	dict_keys(['mislav'])
    # list(answer.keys()) : 	['mislav']    

# import collections
# def solution(participant, completion): #"leo", "kiki", "eden"]	["eden", "kiki"]
#     answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer.keys())[0]
# [1] 김형준 , ii , 홍승현 , YoungHo Choi 외 1424 명

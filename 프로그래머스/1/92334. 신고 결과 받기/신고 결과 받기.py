# 0)
# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi_이용자 frodo_신고","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# 1)
# 유저-> 한 번에 한 명의 유저만 신고 가능
# 한 유저를 여러 번 신고 가능 but 한유저가 한 건 무조건 1회처리
# k번 이상 신고된 유저 : 게시판 이용 정지 -> 신고한 유저에게 메일로 해당 사실 알려줌
# => 받은 아이디 순서대로의 유저가 받은 메일 횟수

# : 중복 없음 

# report : 2십만
# : 없는 사용자
# 4) 자기 자신 신고 X

# 2) 
# dict1= : [신고받은 횟수, 한 사람들] 저장
# for a in report : aa, bb = a.split(' ') 횟수 
# if not in 이면 count
# -> 막판 for id in id_list : 돌며 k 횟수 넘은거 result.append(dict1[id][1:])

def solution(id_list, report, k):
    answer=[0]*len(id_list)
    
    dict1=dict( zip(id_list, [[0] for _ in range(len(id_list))]  ) )   # : [신고받은 횟수, 한 사람들] 저장
    dict2=dict()
    dict2=dict( zip(id_list,range(0,len(id_list))) ) # ~ dict(zip(list1, list2)) 
    # 이것도됨 dict2=dict( [ [person, index] for index, person in enumerate(id_list)]  ) # 사람 : 인덱스 # 2차원 update
    for a in report : 
        person, target = a.split(' ') # 횟수 
        if target not in dict1 or person not in dict1 or person==target :# 같은 사람
            continue
            
        if dict1[target][0]==0 or person not in dict1[target][1:]: # 비어서 무조건 신고되는 거 or 한 유저가 또 신고 하는 거 아니면
            dict1[target].append(person)
            dict1[target][0]+=1 # count
            
            
    # 메일 받은 횟수 : list에 메일 받은 횟수 idx로 넘기기?
    for id in id_list : # 내가 메일 받은 횟수_for in 찝찝 OR 나로 인해 메일 받은 사람들 위치에 +
        if dict1[id][0] >= k : # k 횟수 넘은 target : 그 타겟을 신고한 사람들 : 딕셔너리에 담겨있음(인덱스도?) -> 그사람들의 숫자+=1
            for i in range(1, len(dict1[id])): #-1) : # 획수땜시 1빼줬던거 ㄴㄴ : 횟수는 맨앞 0인덱스에서 이미 뺴줌
                answer[ dict2 [  dict1[id][i] ] ]+=1 # 메일갈 사람_dict1[id][i]의 인덱스 찾기
    return answer

# : 43m?(print때문에 오류난 시간 뺀?) : 성능 +3 / 최대 828ms

# - 시간 걸린 이유 : 논리에 조금, 딕셔너리에 조금 
# - 디버깅: 중간 결과 출력
# XX_m2_X 그냥 reoprt 돌 때 answer[자신]+=1하고, 마지막 루프에서 k이하인거 0화?:X 메일 안감

# - dict 생성_주소생성 공유 주의
# : fromkeys 자체의 문제가 아니라_value로 리스트형을 저장할 때 공유되기도 하는거네.
# -> 그냥 후에 변경 활용을 편하게 하려면, 모든 변경활용에 통용되는 생성법 1.1) 방법 OR 2)_value 값은 리스트로 저장하진 마.
# ::: 아래 예는 안이상함.[0]리스트의 첫 인덱스에 해당하는 게 0이니까. 위 코드는 그냥 이전엔append가 뒤에 있었어서 그랬던 건가.
    # dict1=dict1.fromkeys([1,2,3],[3])
    # dict1[1][0]=20 #{1: [20], 2: [20], 3: [20]} ## 이거 인덱스를 잘못사용했었는데 음
    # dict1[1]=[20] # {1: [20], 2: [3], 3: [3]}
# 1.1) dict1=dict( zip(id_list, [[0] for _ in range(len(id_list))]  ) ) 
# 1.2) 리스트 *concat로하면 값공유(주소 공유같음) 
# 2) fromkeys value 한 값 초기화도, 모든 key에서 값 공유 된다.
# dict1=dict1.fromkeys(id_list,[0]) 

# - 다른 사람 풀이 :Good! 
# > 나_딕셔너리에 신고당한 횟수 뒤에 신고한 사람들이름 붙임. ((G?정확전체코드는기억안남)<->  report 한 번 더 돌면서 k이상이면 answer+=1  
# -> 코드 단순화, 풀기속도 : 저사람 / 큰 단위 시복은 내가 더 좋을듯 (report가 길기에)
# : m2 시도 중_id_list말고 report돌 때 +1했었는데_아직 신고전체 값이 미반영되는 논리라서 하다맘
# : -> 그럼 report를 한 번 더 도는 방법. (시복 단위에선 병렬이라 같음)

# > 나_dict2 (시복효율은 좋을듯) <-> 있는 id_list.index()
# > set으로 중복 자동제거 : for r in set(report) :: set화가 시복n 이긴 할테지만 for in에서라 병렬시복연결일듯
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1
        
        
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1 

#     return answer
# : 최대 1392ms
# [1] 최하람 , 이유현 , 이중목 , jamin-rachel-kim 외 233 명 
# 명수보니 어디 책에 나와있는 건가 암튼

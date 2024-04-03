# 0)
# players	callings	result
# ["mumu", "soe", "poe", "kai", "mine"]	["kai", "kai", "mine", "mine"]	["mumu", "kai", "mine", "soe", "poe"]

# 1)
# 바로 앞의 선수를 추월[<->]한 사람 : 이름 불림
# -> 최종 등수

# 2)
# -> for man in callings -> 인덱스 찾아서( players.index(man)) idx-1인놈이랑 바꿔주기 , =,
# --> players반환


# m2_ii)딕셔너리 -> 리스트에 저장 -> sort
def solution(players, callings):
    dict1 = { a : i for i, a in enumerate(players)} # 0위~k위
    # dict2 = { i : a for i, a in enumerate(players) } -> 이거대신 리스트 사용함
    # m3 불린횟수 .count
    # m2_iii_수정) 
    for man in callings : # 1> 내 idx 사용 및 변화, 2> 추월당한애도 동일
        idx=dict1[man] # 1>사용 : callings 변수에 의해 이름으로 찾아서 시작
        dict1[man]-=1 # 1> 내 등수idx 올라감 
        target=players[idx-1]
        dict1[target]+=1 # 2> 추월당한놈 등수idx 올라감
        
        # m2_iii) 인덱스 대체_딕셔너리는 2> 앞등수 애 찾기가 어렵네 -> 딕셔너리 두 개 OR "리스트도 병렬 사용"
        players[idx], players[idx-1] = players[idx-1] , players[idx]      
    return players
    
    # - m2_iiii)딕셔너리 sort보다 리스트도 같이 쓰는 게 나을듯
    # answer= [ [v,key] for key, v in dict1.items()]# 딕셔너리 아이템
    # answer.sort()
    # # print(answer)
    # # print([a[1] for a in answer])
    # return [a[1] for a in answer]
# : 35m / 최대1135.02ms 

# - 디버깅
# : 70점_시간초과 
# > ; callings의 길이 ≤ "1,000,000 ": O(n^2) 안됨
# -> m2_i) index 대체 : 딕셔너리에 인덱스 저장. for로 돌며 다시 리스트화


# - 꽤 많이 예전에 맞추었던 거네 
# : 기억은 안 났었는데, 결론적으론 방법이 똑같네

# def solution(players, callings):
#     # 변수명으로 찾을 수 있게(for j in players:# if j==i:대신)-> 딕셔너리
#     temp={player:order for order, player in enumerate(players) }
#     for i in callings: 
#         rank=temp[i]
#         players[rank-1],players[rank] =players[rank],players[rank-1] # 결과p위치 뒤집
#         # 추후 순위획득 위해 접근할 딕셔너리 temp값 변경
#         temp[i]-=1# 순위 좋아짐
#         temp[players[rank]]+=1# 순위 나빠짐_앞에있다가 이제 뒤에있던놈
#     answer=players    

            
#     # m1_ index먼저로 정렬, 꼭 추월당한 놈의 점수 안좋게화도
# #     target=[] # player,score 
# #     for a, b in enumerate(players):
# #         target.append([a,b])
        
# #     callings.sort() # nlogn?
# #     #target.sort()
# #     index, i=0,0
    
# #     ### 등장 안 하는애 있을 수도 있네
# #     for a in callings:
        
# #         if target[index][0] == a :
# #             target[index][1]-=1
            
# #         else:
# #             while(1 ):
# #                 if target[index+1][0] == a: # 다음거랑 같늬
# #                     target[index+1][1]-=1
# #                     index+=1 
# #                     break 
# #                 index+=1
# #         print(a)
# #         print (target)
                    
# #     target.sort(key=lambda x : x[1])#
    
# #     for a in target:
# #         answer.append(a[0])

        
#     # m2_아래와 같은 점수방식은 안됨.그 앞놈 점수를 깎던지.
#     # 현재등수_점수 0,1 
#     # count_점수 -1씩__n^2보다, callings 따로 돌면서 점수바로 +-[=+할위치까지n^2] or새로우면 append하든
#     # > sort후 횟수 세면, n^2아녀도
#     #, sort _오름차순
# #     target=[] # player,score 
# #     for a, b in enumerate(players):
# #         target.append([b,a])
        
# #     callings.sort() # nlogn?
# #     #target.sort()
# #     index, i=0,0
    
# #     ### 등장 안 하는애 있을 수도 있네
# #     for a in callings:
        
# #         if target[index][0] == a :
# #             target[index][1]-=1.001
# #         else:
# #             while(1 ):
# #                 if target[index+1][0] == a: # 다음거랑 같늬
# #                     target[index+1][1]-=1.001
# #                     index+=1 
# #                     break 
# #                 index+=1
# #         print(a)
# #         print (target)
                    
# #     target.sort(key=lambda x : x[1])#
    
# #     for a in target:
# #         answer.append(a[0])
#         # '중복'=새놈이 우세
#         # 기존있던놈 우세 X _ +-:n(->.9)과 0.999(0.999,0.9999되게?)씩-(-> -1) /  2씩/1씩_X
        
#     #m1
# #     for i in callings: 
# #         k=0
# #         for j in players:#list get
# #             if j==i:
# #                 players[k-1],players[k] =players[k],players[k-1]  # value를 바꿔 넘겨버려 엥 그럼 temp필요없었네
# #                 break
# #             k+=1
            
# #     answer=players
#     return answer
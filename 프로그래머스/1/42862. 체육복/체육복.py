
# 0) 
# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5

# 1) 바로 앞/뒤 번호에만 빌려줄 수 있음
# -> 최대 수업 참여 학생수

# Again 2) : 자신의 체육복이 lost, reserve에 다 있는 경우 남 못빌려줌 
# n-len() -> for in lost _ a in reserve 체크(미리 set/딕셔화)_ 추후 pass할 번호로 새로저장&answer+1 -> for in lost : 앞번호나 뒷번호가 reserve에 있는지
# ;정렬 돼있는줄. 왜 그렇게 확신해버렸늬!! 
# -> 논리 흐름 세부값 출력해봤으면 바로 알았을듯


# 2) lost 학생이 reserve에서 앞 번호 부터 가져가기? in
### 뒤 꺼 가져 가는 게 나은 반례 : 앞에가 몰림 -> 둘 다 가져갈 수 있으면 앞에께 이득같은데 어차피 cout라 말얌. 123 123  ==> 5가
### 재귀? dfs bfs? 
# 3)
# answer=n-len(lost)
# for a in lost :
#   if a-1 in reserve :
#       answer+=1
#       reserve.pop(a-1)
#   elif a+1 in reserve :
#       answer+=1
#       reserve.pop(a+1)

# 4) lost & reserve 학생 : 못 빌려줌 (건너연달아 못빌려주나봄) ->
# ; 0번 학생 없겠지? -1되면 귀찮으니 걍 있다 가정

def solution(n, lost, reserve):
    lost.sort()
    answer = 0
    answer=n-len(lost) 
    # - 문자형 특징 덜 암기/체화돼있음
    # > list1_remove 잘 몰라서 <-> str1_replace로 대체 하던 중 ㅋㅋ (agan remove 대신 pass할 것 append법)
    # reserve2=str(reserve) #	[:]든 '[1, 3, 5]'로 저장인거임. (( 요소를 string화하려면 map을 쓰든 해라잉. ))
    # print(reserve2) 
    # print(reserve2[0],reserve2[1])
    
    # > method : 완전 str화 방법 은 안 되긴함 : '11'도 '1'replace때 지워져버림
    ## a=['11','1']
    ## print(str(a).replace('1','')) # ['','']
    
    # X_코드효율화 : 이미 오름 차순이니(아녔음ㅜ) in 확인 때도 특정 index증가해가며 체크 OR 낮은값 pop
    # <-> m_우선순위 큐 : 0) heapq.heappush/heappop
    
    for i, a in enumerate(lost) :
        if a in reserve : # <-> str1.find('a')
            answer+=1
            # remove 까먹어서, 상대 reserve/lost에 있을 수 없는 숫자로 변경해서 저장함
            lost[i]=-4 # lost에서 돌고 있는 거라 얘는 인덱스 이미 있음
            inde=reserve.index(a) 
            reserve[inde]=-2  # reserve2=reserve2.replace(str(a),'') # 인덱스 함수로 인덱스 찾은거면 pop쓸 수있긴함. Again) remove <->~ .index & pop 병렬
    
    for i, a in enumerate(lost) :
        # if str(a) in reserve2 :
        #     answer+=1
        #     reserve2=reserve2.replace(str(a),'')
        if a-1 in reserve : #
            answer+=1
            inde=reserve.index(a-1)
            reserve[inde]=-2            
            
            # pop은 인덱스를 받는 거라 안됨.->.index병렬로 쓰면 되긴함(중복없기 때문임) #reserve2=reserve2.replace(str(a-1),'')# reserve.pop(a-1)
        elif a+1 in reserve :
            answer+=1
            inde=reserve.index(a+1)
            reserve[inde]=-2 
            # reserve2=reserve2.replace(str(a+1),'')# reserve.pop(a+1)
            # print(reserve2)
    return answer
# : 1h_93.3% -> 질문하기 문서 봐버림 (sort 돼있는줄 ㅜ) 
# ->* 중간 변수 다 출력해봤으면 충분히 찾을 수 있었음
# -> 성능 : +8 & 최대0.02ms



# - 다른 사람풀이
# : list1.remove사용


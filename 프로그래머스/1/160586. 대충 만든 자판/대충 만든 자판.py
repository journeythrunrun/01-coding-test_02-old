# 0)
# 키의 개수 (1~100)
# :없으면 -1

# 4) 같은 문자가 다른/같은 자판에 여러번 할당 가능 / 미할당 가능
# -> 키를 최소 몇 번 눌러야 하는지 & 불가능 = -1

# 2)
# m1) 첫 입력 대상 단어_각 자판들 병렬로 체크?(최대3for)&min값? 
# m2) [빠를듯]OR 알파벳에 따른 최소 횟수 미리 저장

# Again) 키패드 클릭 최소 수 
# cnt[A~Z] :for for문자 in keymap_min(_,j+1) -> for for문자 in targets : cnt[A~Z]
def solution(keymap, targets):    
    numb=ord('Z')-ord('A')+1
    cnt = [200]*numb # X_[200*numb] 
    
    for a in keymap :
        for i,b in enumerate(a) : 
            # 더 적은 횟수를 min으로 저장. # 굳이 조건문 체크&저장보다, 그냥 min으로 퉁침
            cnt[ord(b)-ord('A')]=min(cnt[ord(b)-ord('A')] ,i+1)
            
    answer=[]
    for i,word in enumerate(targets): 
        count=0
        for one in word :
            if cnt[ord(one)-ord('A')] != 200:
                
                count+=cnt[ord(one)-ord('A')]
            else :
                count=-1
                break # 웬 순간 continue냐
        answer.append(count)
    return answer
# : 26m / 성능: +8 & 최대시간3.93ms
# - 오류 케이스 해결 : 코드 알고리즘 논리 엄밀 분석

# - 다른 사람 # Again) 
# > 알파벳을 '리스트 인덱스에 1대1 맵핑' 시키기보다 ->  '딕셔너리는 바로 간단 사용'&상황따른효율도 가능 ( 다른 문자열로 호출 때도 good)
# : [ord(b)-ord('A')]
# > 미등장 체크 : 키 in 딕셔너리 <->나_200초기값 체크

# def solution(keymap, targets):
#     answer = []
#     hs = {}
#     for k in keymap:
#         for i, ch in enumerate(k):
#             hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

#     for i, t in enumerate(targets):
#         ret = 0
#         for ch in t:
#             if ch not in hs:
#                 ret = - 1
#                 break
#             ret += hs[ch]
#         answer.append(ret)

#     return answer
#[1] YeoEunSeong , sangyun

# 가장 가까운 같은 글자_https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 앞쪽 중 가장 가까운 동일문자와의 간격/없=-1

#	통과 (8.26ms, 11MB)
def solution(s):
    # a~z 인덱스 위치에 저장 및 업데이트
    temp=[-1]*26
    ans=[]
    for i in range(len(s)):# b
        # '간격'!=인덱스
        # 조건문 temp[i] 아님 index_alpa=temp[ord(s[i])-ord('a')]
        ans.append(i- temp[ord(s[i])-ord('a')] if not temp[ord(s[i])-ord('a')]  ==-1 else -1 )# i-{'a'-'a'=0}  # 10-8 # 없으면 -1 떠야 
        #저장
        temp[ord(s[i])-ord('a')]=i # [-1,0,]
    return ans

# 해설 
# - 나_인덱스 (속 인덱스) 할당 = 해설_ dict #어차피 for에서 찾는 거 아니라서, list도 인덱스값 구해서 접근이라 큰 차이 없을듯. 
# : dict장점 = 1) 미리 알파벳26개 짜리 변수 만들 필요도, 2) index계산 식도 필요없음(ord라서개조금 더 더럽?)  
# - 찾기 = 'in'
#	: t 두배면 시복같은수준 아닌가_통과 (3.82ms, 10.9MB)
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
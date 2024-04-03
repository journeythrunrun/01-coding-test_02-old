# 덧칠하기_https://school.programmers.co.kr/learn/courses/30/lessons/161989


# n미터 # 롤러 길이 m 
# 롤러 시작 아무곳이나됨 / -> 최소 칠 수
# 여러번 칠해도됨 / 안칠해도되는 곳 칠해도됨 

# m,n,원소 자연수
# 배열 = 1) 안빔  / 2) 중복 없음 / 오름차순 정렬

# 1h
# *조건을 디버깅이나 후단계가 아니라, 처음부터 엄밀히 잡아야 시간이 줄여질 것 같은데 말이다.
#통과 (10.67ms, 12.9MB)
def solution(n, m, section): # 8 / 4/ [ 2,3,6
#     # m2) 단순 완전탐색, dfs_재귀
        # 나중에 필요하면..    
#     # ms) 양 끝 먼저 사용 2+3(_m-1)=5 까지 칠함 
    #m other) 사용을 수식에 맵핑 how= 해당 인덱스부터 사용? (10만 인덱스 배열생성이 더 오래걸리나.. O(n)? )or 나누기 or set& in 
#     # -> 10만대신 sort돼있는거에서 한 두개 검사하고 break 등오로 나오거나 하면 되니.

#     # left pop대신, 왼쪽은 index로 다루기
    # 1) val+=m_까지칠함 / index+=m /if section[index]
    #* 초기값 실수가 잦다.~ 식 세우고 초기값은 후에 한 개를 정확히 대입 및 맵핑?**
    val=section[0] +m # 이미 1개 쓰고 다음 타겟부터 검사# 2 # val=target
    count=1
    if len(section)==1:
        return 1
    index=1
    # m other) 다음 대상위해 +m으로. 첫번째꺼에서  ㅡ
    # 다음 타겟부터 시작. (페인트 칠한 인덱스 후에있는 값중에서 처음 등장하는 타겟)
    
    bre=False
        #  2,3, 200
        # for 대신해당 section[index] 로부터 곱나누기로 효율화가능할듯. 리스트에서 도는 건 동일하고 그 케이스 내에서도 +m씩 할때? 해설코드 보니까 걍 O(n)바로 되네 
        ## value 에서 m을 더한 거와 < => 배열에서 빼서 검사하든 _이게 시복 더 낫다.
        
        
    # 다음 타겟 갱신_=count+1 # val  200으로 갱신해야   
    while(1):

        if index > len(section) -1: # section끝까지 검사.
            bre=True
            break
                
        if val <= section[index]:# 2->6 <=200,6 # 검사 대상 갱신
            val=section[index]+m # 써서 이미 '그' '다음께' 검사대상여야 # val=200
            count+=1
            index+=1 # 썼고 다음거.
            continue #break
        else: # val> section[j] : # 2->6 >= 5,6
            index+=1 # 이미 검사된 section속 번호라서.

    return count 
    
# - 해설[내꺼보다 2배빠름. 비슷]
def solution(n, m, section):
    answer = 1
    prev = section[0] 
    for sec in section:# <-> 인덱스. 대신 솔루션은 한 요소당 검사할 수 있게 구현해놓음
        if sec - prev >= m: # 수식 관점차이. 내코드랑 비슷한 조건. 기점을 prev에서 더하면서 시작하지 않고, 처음부터 배열의 요소에서 시작했네. '이전 것val'과의 차이로 했고.나는 m을val에서 그전에 더해줬었고. 즉, 수식 및 조건 통합.
            
            # 색칠한 위치인 prev갱신. 검사 대상아니고 색칠한 놈.
            prev = sec
            answer += 1

    return answer
    
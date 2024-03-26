# 달리기 경주_https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    # 변수명으로 찾을 수 있게(for j in players:# if j==i:대신)-> 딕셔너리
    temp = {player: order for order, player in enumerate(players)}
    for i in callings:
        rank = temp[i]
        players[rank - 1], players[rank] = players[rank], players[rank - 1]  # 결과p위치 뒤집
        # 추후 순위획득 위해 접근할 딕셔너리 temp값 변경
        temp[i] -= 1  # 순위 좋아짐
        temp[players[rank]] += 1  # 순위 나빠짐_앞에있다가 이제 뒤에있던놈
    answer = players

    # m1_ index먼저로 정렬, 꼭 추월당한 놈의 점수 안좋게화도
    #     target=[] # player,score
    #     for a, b in enumerate(players):
    #         target.append([a,b])

    #     callings.sort() # nlogn?
    #     #target.sort()
    #     index, i=0,0

    #     ### 등장 안 하는애 있을 수도 있네
    #     for a in callings:

    #         if target[index][0] == a :
    #             target[index][1]-=1

    #         else:
    #             while(1 ):
    #                 if target[index+1][0] == a: # 다음거랑 같늬
    #                     target[index+1][1]-=1
    #                     index+=1
    #                     break
    #                 index+=1
    #         print(a)
    #         print (target)

    #     target.sort(key=lambda x : x[1])#

    #     for a in target:
    #         answer.append(a[0])

    # m2_아래와 같은 점수방식은 안됨.그 앞놈 점수를 깎던지.
    # 현재등수_점수 0,1
    # count_점수 -1씩__n^2보다, callings 따로 돌면서 점수바로 +-[=+할위치까지n^2] or새로우면 append하든
    # > sort후 횟수 세면, n^2아녀도
    # , sort _오름차순
    #     target=[] # player,score
    #     for a, b in enumerate(players):
    #         target.append([b,a])

    #     callings.sort() # nlogn?
    #     #target.sort()
    #     index, i=0,0

    #     ### 등장 안 하는애 있을 수도 있네
    #     for a in callings:

    #         if target[index][0] == a :
    #             target[index][1]-=1.001
    #         else:
    #             while(1 ):
    #                 if target[index+1][0] == a: # 다음거랑 같늬
    #                     target[index+1][1]-=1.001
    #                     index+=1
    #                     break
    #                 index+=1
    #         print(a)
    #         print (target)

    #     target.sort(key=lambda x : x[1])#

    #     for a in target:
    #         answer.append(a[0])
    # '중복'=새놈이 우세
    # 기존있던놈 우세 X _ +-:n(->.9)과 0.999(0.999,0.9999되게?)씩-(-> -1) /  2씩/1씩_X

    # m1
    #     for i in callings:
    #         k=0
    #         for j in players:#list get
    #             if j==i:
    #                 players[k-1],players[k] =players[k],players[k-1]  # value를 바꿔 넘겨버려 엥 그럼 temp필요없었네
    #                 break
    #             k+=1

    #     answer=players
    return answer


# 최대공약수와 최소공배수_https://school.programmers.co.kr/learn/courses/30/lessons/12940
# ->[최대공약수, 최소 공배수]
# (두 수_자연수)

# 나_통과 (0.14ms, 10.2MB)_ 42m.. 구현 피지컬 딸림
# 코딜리티 함수_
def max_common(a, b):
    if a == b:
        return a
    if a > b:
        max_common(a - b, b)
    else:
        max_common(a, b - a)


# print(max_common(3, 12)) # 출력_ "마지막 탈출 함수의 리턴 값 = 미지정_None

def solution(n, m):
    answer = [1, 1]
    # 2] 3, 12-> 최대공약수=3 / 최소공배수=12
    # > 최대공약수
    # : m1) 작은 수?의 최대 약수로부터 나머지 체크[경험적 서치가 빠를 수도]
    # : m2 최대공약수 구하는 연산방식으로 부터[정석_수학배운방법이니 빠르려나 흠]
    # > 최소 공배수: m2 or 시복허락하련지_최소부터 공배수 완전탐색

    #
    minv, maxv = min(n, m), max(n, m)  # 3, 12
    # down= (minv, maxv)  #~튜플

    while (1):  ##  각 니은자, 다음 / 니은자 종료==2)최대공약수 없을 때까지
        exist = False
        ## 2) (한 니은 안에서)_최대공약수 한 개 구하기

        for aa in range(minv, 2 - 1, -1):  # 경계포함 3,2

            if minv % aa == 0 and maxv % aa == 0:  # (최대)공약수 존재# 3
                minv, maxv = minv // aa, maxv // aa  # 1,4 # /하면 float형으로 반환해버림
                answer[0] *= aa  # 1*3
                exist = True
                break
        if exist == False:  # 좌측 공약수 없다->최소공배수 # aa_1제외 됐나
            break

    return [answer[0], answer[0] * minv * maxv]
    # # m1_반
    # minv, maxv=min(n,m), max(n,m)
    # # 최대순 부터 약수 쳌
    # for aa in range(minv, int(minv**0.5)-1,-1 ): # 경계포함_25면 5 & 26이면 5
    #     if minv%a==0 and maxv%a==0 : # 공약수
    #         answer[0]=aa
    #         break


# - 해설_(0.01ms, 10MB)
# > Euclidean algorithm글, ..
# def solution(a, b):
#     c,d = max(a, b), min(a, b) # 3, 12
#     t = 1
#     while t>0:
#         t = c%d # 3%12=3  / 12%3=4
#         c, d = d, t # <- 12, 3 /
#     answer = [ c, int (a*b/c)]
#     return answer




# (풀기 오래걸림ㅜ_(0.04ms, 10.3MB)_가능 다양 방법 시도 하다가 시간 더걸려 )
# 3진법 뒤집기_https://school.programmers.co.kr/learn/courses/30/lessons/68935

# 3진법 -> 앞뒤 뒤집 > 10진법

def solution(n):
    #
    # (100 40 이 아니라 1 4 를 구하려는 거)
    # 2] m_수식 양변 조작해서 계수 찾기_'수식'에서 '양변에 연산 취해서' ' 계수 구하기'  # 연산 == % //로 떨구는 방법도 있음
    # :10진법 45 =10^2 *0 10(^ (1)) *4 + (10^0)*5
    # : (( 100으로 나누면 뒤에 45가 나오는 식 > 몇자리인지 찾기 귀찮으니 뒷부분부터하자

    # 2] m_X너무 45 같은 case로만 fit하다가는 앞뒤 상황 반영 안되기도.
    # 10으로 나눈 나머지 =5 #! 원랜 이전 것들 다인데, 이전 것들이 한개라.
    # 10으로 나눈 몫 = 4
    # 100으로 나눈 몫 = 45 == n
    # if 100으로 나눈 나머지==n : break

    # 3진법 45= (3^3)*1+3^2 *2 +3^1 *"0" + 3^0 *0 # 10(^ (1)) *4 + (10^0)*5
    last = [str(n % 3)]
    i = 1
    # left=n
    while (1):
        # 조건문을 앞에 했어야 아까도
        if n % (3 ** i) == n:
            break
        # left-=last[-1]*(3** (i-1) ) # 140

        # last.append( left  //(3**i)) # \
        last.append(str((n % (3 ** (i + 1))) // (3 ** (i))))  # %[ 인덱스부터 위쪽 날려 (145면 45)] //[인덱스부터 아래쪽 날려 (145면 14)]
        i += 1

    # ['0',0,2,1]
    return int(''.join(last), 3)  # 시간초과_다른 거 봄

    # i=1
    # #
    # while(1):
    #     #-last[0]
    #     last.append(n%(3** (i) ) ) # 45//(10^1) =4
    #     #last=[ n//3**i for i in ]
    #     total+=last[-1]*3**i # 4* 10^1
    #     if total==n:
    #         break
    #     i+=1
    # print(last)
    # return 1

#
#     i=1
#     last=[n%10]
#     n-=last[0]
#     while(1):
#         n%(3**(i+1) )
#         i+=1
#         if a==0:
#             break
#     # -> 3진법 45= 3(^3)*1+
#     last=[n%3]  # 0
#     # 45//9=
#     while(1):
#         #-last[0]
#         last.append(n//(3** (i) ) ) # //100 - 5 = 45 - 5 =40
#     print

#     for j in range(len(last), ):
#         answer=last[j]
#----------------------------


# [1차] 비밀지도_https://school.programmers.co.kr/learn/courses/30/lessons/17681
# 한 변 n / 1=벽_ or, 0=공백_and
# 원소 0인 case

# 통과 (0.38ms, 10.2MB)
# met_함수 따로 빼기 : 시복 줄이려할 때는 한 번에 보기/수정 불편한듯. 그래도 재귀함수 등은 가능
def to_two(a, b, n):  # 1 line
    ans = ''
    # reverse.
    for i in range(n - 1, -1, -1):  # n ##
        # old값 저장하기보다 간단 연산이니 한번에.
        # 앞큰값 버린 값에서, 몫구하기
        aa = a % (2 ** (i + 1)) // (2 ** (i))  # c & 없으면 0  # 'a'+""""""3
        bb = b % (2 ** (i + 1)) // (2 ** (i))

        ans += '#' if aa or bb else " "
    return ans


def solution(n, arr1, arr2):
    # 2진수로.
    # 2] x=a*2^0 + b*2^1 + c*2^2 #3
    lines = []
    for i in range(len(arr1)):
        lines.append(to_two(arr1[i], arr2[i], n))  # '11111' #시복단축
    # m_s) 자릿수에 대한의미로 9,20 등에서 연산계산을 통해 바로 출력해보려하다가 생각하는데 시간 걸릴 것 같아서 패쓰
    return lines

# 해설_훨빠름 _ 진수변환함수사용_나머진 시복 비슷.< - > 나_k진수변환 직접 구현
# - 2진수로는 bin, 10진수로는 int
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str( bin(i|j)[2:]  )
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer


# 모의고사_https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 12345
# 21 22pass 23 24 25 / 21
# 33 11 22 44 55/
# 앗 수포자 3명만 있다. 일반화 패턴 내가 찾아내는 거 아님
# _*최고득점 여럿일 경우,

# _*빈배열 : 자동처리, print로 체크
def solution(answers):
    # answer-aa -># m1) not 연산자로 정답일 0케이스를 1로 하고 나머지 다 0으로 한다음에 sum하는 방법

    # m2) 단순 for_구현속도 빠르려나	통과 (4.47ms, 10.3MB)
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer1 = [[0, 1], [0, 2], [0, 3]]  # 힙큐
    for i in range(len(answers)):  # 에라이 s한글자 오타
        answer1[0][0] += 1 if a[i % 5] == answers[i] else 0  # [0]없을 때TypeError: 'int' object is not iterable
        answer1[1][0] += 1 if b[i % 8] == answers[i] else 0
        answer1[2][0] += 1 if c[i % 10] == answers[i] else 0

        # answer1.sort() ##변수이름 안 겹치게
    answer1 = sorted(answer1, key=lambda x: x[0])  # x_각 행 한개씩 받네 # x[0]이든 x든 됨.2열 이미 정렬돼있어서.

    # 역순
    if answer1[-1][0] == answer1[-2][0]:  ## 변수명 겹친다. result같은 일반폼 말고 의미 무조건 담자.
        result = [answer1[-2][1], answer1[-1][1]]
        if answer1[-2][0] == answer1[-3][0]:
            result = [answer1[-3][1], answer1[-2][1], answer1[-1][1]]
    else:
        result = [answer1[-1][1]]  # 고득점자

    # !조건 틀림 # if 속 if 여야
    # for j in range(2):
    # if answer1[-(j+1)][0]==answer1[-(j+2)][0] :
    #     result.append(answer1[-(j+2)][1])

    return result

    # - 해설_GOod_내 정렬보다 낫다(3개밖에 없긴 해도)
    # - 획득 점수를 max값과 각각 다 비교
for idx, s in enumerate(score):
    if s == max(score):
        result.append(idx + 1)

return result


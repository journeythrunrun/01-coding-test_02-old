# #짝수와 홀수_https://school.programmers.co.kr/learn/courses/30/lessons/12937
# def solution(num):
#     answer = ''
#
#     if num % 2 == 0:
#         # answer="Even"
#         answer = answer.join('Even')
#     else:
#         # answer="Odd"
#         answer = answer.join('Odd')
#
#     return answer

# # 평균 구하기_https://school.programmers.co.kr/learn/courses/30/lessons/12944
# def solution(arr):
#     answer = 0
#     for a in arr:
#         answer+=a
#     answer/=len(arr)
#     return answer


# #나머지가 1이 되는 수 찾기_https://school.programmers.co.kr/learn/courses/30/lessons/87389
# def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         if n % i == 1:
#             answer = i
#             break
#
#     return answer

# # 약수의 합_https://school.programmers.co.kr/learn/courses/30/lessons/12928
# # [약수] 1) 나눌 초기값1 2) 제곱근 케이스, 따로 1개만 더해
# def solution(n):
#     answer = 0
#     k=1 # 약수를 위해 나눠볼 변수_초기값 1
#     if n==0:
#         return 0

#     while( k<n**0.5):
#         if n%k==0:
#             answer+= k+n//k
#         k+=1
#     if k==n**0.5:
#         answer+=k
#     return answer

# # x만큼 간격이 있는 n개의 숫자_https://school.programmers.co.kr/learn/courses/30/lessons/12954
# def solution(x, n):
#     answer = [ x+x*i for i in range(n)]
#     print(answer)
#     return answer

# 자릿수 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/12931
# def solution(n):
#     answer = 0

#     nn=str(n)# "123"
#     for i in nn:
#         answer+=int(i)
#     return answer

# # 자연수 뒤집어 배열로 만들기_https://school.programmers.co.kr/learn/courses/30/lessons/12932
# def solution(n):
#     nn = str(n)
#     answer = []
#     # answer.extend(int(nn[k] ) for k in range(len(nn)-1,-1,-1))
#
#     for i in nn[::-1]:
#         answer.append(int(i))
#
#     return answer

# # 문자열 내 p와 y의 개수_https://school.programmers.co.kr/learn/courses/30/lessons/12916
# def solution(s):
#     # i) p, y 다 하나도 없 -> True
#     # : count=0에 포함 ㄱㄴ
#
#     # ii) p류 == y류 -> True / != False
#
#     # other) 아스키 코드는 c언어만인듯
#     count = 0
#     for a in s:
#         if a == 'p' or a == 'P':
#             count += 1
#         if a == 'y' or a == 'Y':
#             count -= 1
#     if count == 0:
#         return True
#     else:
#         return False


# # 문자열을 정수로 바꾸기_https://school.programmers.co.kr/learn/courses/30/lessons/12925
# def solution(s):
#     # 부호_int()가 부호도 해결 ((X_앞에 한 개만 그걸로 받고 ))
#     # s='-123'
#     answer = int(s)

#     return answer


# 정수 제곱근 판별_https://school.programmers.co.kr/learn/courses/30/lessons/12934
# # x의 제곱 -> (x+1)**2
# # != -> -1
# def solution(n):
#     #m1_ 제곱 쪽일 n에 root를 씌운 후 정수인지 보기.
#     # 정수판별= 1로 나눈 나머지가 0인지
#     if n**0.5%1 == 0 : # 정수란 것
#         return (n**0.5+1)**2
#     else :
#         return -1

# #     # m2
# #     x=1
# #     while(x<= n**0.5):
# #         if x==n**0.5:
# #             return (x+1)**2
# #         x+=1

# #     return -1


# # 정수 내림차순으로 배치하기_https://school.programmers.co.kr/learn/courses/30/lessons/12933
# # : 118372 -> 873211_'자리수'_'큰 순서'로
#
# # > 연속 <-> 자릿수
#
# # A) '123'->[1,2,3]
# # list(str) : str에 씌우면_'ab'붙어있어보여도 순서있는놈 list순서로 옮기는 것 뿐( 출력 꼴은 분해같아 보여지긴함)
# # >> 반복형 객체 --map ->반복형 객체
# # list(  map(int,'123'))  # 변경 대상) map_'요소의' 형식, only'list( 를 map에 _ 합체
#
# # <-> str(list1) : 설령(자료형 바꿀필요 없는데도) map까지 씌우고해도 분해 반대인 강제 합체 안됨(비가역적). 분해했다가 작업해야
# # B) [8,7..]-> '87..' (( -> 87..)) 변경_요소형식 & 합체
# # m1) concatenate
# # answer=''
# # for k in [8, 7, 5]:
# #     answer+=str(k)
# # answer=int(answer)
# # m2)
# # 1) [8,7.. -> ['8','7',..] 요소 형식
# # 1.m1) [    str(k) for k in [8,7,5]]  # (list?) comprehension
# # 1.m2) list   (map(str,[8,7,5] ))
# # 2) ['8','7',..] -> '87..' 합체
# # answer=''.join(answer)
#
# def solution(n):  # 118372
#     # - list(str1) # '리스트'를 씌울 때만 입력 분해 # '12'-> ['1','2']
#
#     # 1) [자리수] 정보 =str사용
#     a = str(n)  # '118372'
#
#     # 2) 큰 순서 = sort 필요 = list화
#     a = list(map(int, a))  # list화 [8,7..
#     a.sort(reverse=True)  # [8,7..
#
#     # 3) [한놈으로 각 자리들을 합치기]=in str _ join ((or 값을 x10^n 씩_시복 자릿수일듯.))
#     #  -> str -> _join
#     answer = [str(k) for k in a]  # ['8', ..
#     answer = ''.join(answer)  # 리스트(iterate)의 요소가 str이어야 # '87..'
#
#     answer = int(answer)
#     return answer
# # 추후_문자열값도 sort 가능

# #하샤드 수_https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=c
# #x: 양의정수
# # 각 자릿수 합  으로 x를 나눴을 떄 나머지 0

# def solution(x):
#     #answer = True
#     a=0
#     for i in str(x) :  #"10"
#         a+=int(i)
#     if x%a ==0:
#         answer=True
#     else:
#         answer=False
#     # 해설m) sum(int(x) for x in str(n))  # generator의 sum ㄱㄴ

#     return answer

# #두 정수 사이의 합_https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=python3
# def solution(a, b):
#     # -7  4
#     # 지금은 더 효율적인 수식 풀이보다, 조건 하에 빨리 풀고 피지컬 올리기.-> 걍 코드 스피드 좀 더 보고 더럽게 구현
#     if a==b:
#         return a
#     answer=0
#     # 부호가 다를 경우
#     if a*b<0:#
#         maxv,minv=max(abs(a),abs(b)),min(abs(a),abs(b))
#         answer=sum(range(minv+1,maxv+1) ) #ran #반대부호값 상쇄됨
#         maxv,minv=max(a,b),min(a,b)
#         if abs(minv)-abs(maxv) >0: #  7 - 4 = 3 # i) 양수_음수의 절댓값이 더 큼
#             answer*=-1

#     # 부호가 같을 경우
#     else :
#         maxv,minv=max(a,b),min(a,b)
#         answer=sum(range(minv,maxv+1))
#         #부호 함수

#     return answer
#     # # m_해설)
#     # if a > b:
#     #     a, b = b, a
#     # return sum(range(a, b + 1)) # 이정도 시간복잡도도 괜찮았나보네

# 콜라츠 추측_https://school.programmers.co.kr/learn/courses/30/lessons/12943
# # 500번 반복 후 아직 1 아니면 -> -1
# # 몇 번 반복해야?
# def solution(num):

#     if num==1 :
#         return 0
#     for i in range(500):
#         if num%2==0:
#             num/=2
#         else :
#             num=num*3+1
#         if num==1:
#             return i+1

#     return -1
# # 해설_별 차이 없음

# 서울에서 김서방 찾기_https://school.programmers.co.kr/learn/courses/30/lessons/12919
# # kim 위치 찾기

# def solution(seoul):
#     # join _입력=반복 객체(5) 1개 & 모든 요소가 str형 => 출력=str ( 반복객체형의 '요소'가 str형이면, 반복객체형 껍질 벗고 str가져와서 str반환 )
#     for i, a in enumerate(seoul):
#         if  a=="Kim":
#             return str(i).join(["김서방은 ","에 있다" ] )

# # - 해설 : index 사용_ 코드 짧은 대신 더 느려
#     # return "김서방은 {}에 있다".format(seoul.index('Kim'))


# 음양 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/76501

# # - get
# # np.sum / sum 시복_1차원에서 비슷. np가 worst가 심하고 평소엔 좀 더 좋음
# # np.int는 reutrn 불가

# # import numpy as np
# def solution(absolutes, signs):
#     #m1) element wise_numpy만 암
#     # : 곱하는 놈들 같은데 연산도 더 효율인가. np부르는데 더 걸리나. <-> m2 for
#     # [압축]_t 약 3배(시복은 비슷해서 그럴수도)_통과 (2.33ms, 28.4MB)
#     # return int( sum(np.array(absolutes)*(2*(np.array(signs) )-1) ) )


# #     # [기본]_통과 (6.72ms, 28.3MB)
# #     a=np.array(absolutes) # 복잡도_O(n)이라는데_시간은 더 걸릴 듯
# #     b=2*(np.array(signs) )-1 # 0->-1 처리 (1->1)
# #     # ax+b=y / b=-1 / a+b=1 -> a=2 / 2x-1=y
# #     return int( np.sum(a*b) ) # np.sum?
# #     # int 안 씌우면 np.int64?32?형이라 return불가 _TypeError: Object of type int64 is 'not JSON serializable'


#     #m2) for각각곱_차라리 빠름(m1_압축_np.sumd_worst 뺀 것보다 조금 더)_통과 (0.14ms, 28.3MB)
#     answer=0
#     for i in range(len(signs)):
#         answer+=absolutes[i]*( True if signs[i]>0 else -1 ) # 0ㄱㅊ
#     return answer
# # 해설
# # : return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
# # : > element-wise < ===> zip
# # : > 부호값으로 -를 곱하지 말고, 조건 만 따진 후 크기에다 '-'로 뒤집어

# # 나누어 떨어지는 숫자 배열_https://school.programmers.co.kr/learn/courses/30/lessons/12910
# # 나누어떨어지는지 > 오름차순sort
# def solution(arr, divisor):
#     # 공통 없음
#     answer=[]
#     for i in arr:
#         if i%divisor==0:
#             answer.append(i)
#     if not len(answer) : #len 시복 1?>
#         return [-1]
#     answer.sort()
#     return answer
# # 해설 : 압축만 다름_comprehension & if, (sorted바로 반환)
# # def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


# # 핸드폰 번호 가리기_https://school.programmers.co.kr/learn/courses/30/lessons/12948
# def solution(phone_number):
#     leng=len(phone_number)
#     num=leng-4
#     # m1) join [t_똑같]
#     return ''.join( ['*'*num,phone_number[leng-1-3:] ]) #concatenate

#     #m2) print [통과 (0.01ms, 10.2MB)]
#     # return'{}{}'.format('*'*num,phone_number[leng-1-3:]) # 뒤에 네개 그냥 [-4:]

# # 해설 : 유사

# # 없는 숫자 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/86051
# def solution(numbers):
#     answer=0
#     for i in range(10):
#         if i not in numbers:
#             answer+=i
#     return answer
# # 해설 : 효율화_수학적 m ((구현 속도용으로 풀어서 방법 생각 시도 아예 안함))
# # : return 45 - sum(numbers)

# # 제일 작은 수 제거하기_https://school.programmers.co.kr/learn/courses/30/lessons/12935
# # 1) min 값 제거
# # 2) if 빈 -> [-1]
# # ( 중복 값 없
# def solution(arr):
#     minv=sorted(arr)[0]
#     # m1) [	통과 (6.37ms, 15.4MB) / 최빈 0.0n]
#     # for이 시복 좋을 듯
#     i=arr.index(minv) # O(n)
#     arr.pop(i) # O(n)
#     return arr if len(arr) else [-1]

# # - 해설[큰 차이 없] : min() ((min_뇌를 스쳤는데 빨리 안 잡으면 사라지는 듯. 걍 이미 생각했던 for 방법 쪽이라 pass한 걸 수도 ))
# # : 코드 압축하시느라 n^2된거고 / min 값 '병렬로 저장'하면 2ㅋ*O(n)
# # return [i for i in mylist if i > min(mylist)] # O(n^2)


# # 가운데 글자 가져오기_https://school.programmers.co.kr/learn/courses/30/lessons/12903

# # 길이_짝수 = 두글자 => 2) [4=>[1]&[2]] 3) leng//2-1 leng//2
# # _홀수 = 한글자   => 2) [5=>[3-1]] 3) leng//2
# def solution(s): # len_O(1)
#     return s[len(s)//2] if len(s)%2!=0 else s[len(s)//2-1:len(s)//2+1]

# # 해설[비슷]
# # : 시복 동일_수학m->if문 제거_ 시복 동일*도아니고 -라 굳이 습득?
# # return str[(len(str)-1)//2 : len(str)//2 + 1]


# 수박수박수박수박수박수?_https://school.programmers.co.kr/learn/courses/30/lessons/12922

# - 문자열 concatenate 스킬
# 1*( ) # 괄호는 튜플화 아니고 연산용이라 제거처리됨.
# +1*( else "")
def solution(n):
    # m : join / concate # 이전(어제)_<->관계들 머 있었징

    # m2) concate : *=+반복 /  +=[= <=> return] /
    # if문 대체 및 concatenate 막기_ 1*("str" if ~ else "" ) # 공백 사용
    return "수박" * (n // 2) + 1 * ("수" if n % 2 != 0 else "")
    # "".join

# 해설[효율X? / 코드 스피드&간단화용]
# : 충분히 저장 후 slicing
# str = "수박"*n # n보다 적게 해도 될듯. 내 코드 만큼 아니더라도, //2 +1개 까지라도 충분히. (((물론 시복 동일_코드 스피드&간략화 위해 걍 저거도 ㄱㅊ)))
#     return str[:n]


# 내적_https://school.programmers.co.kr/learn/courses/30/lessons/70128

# 내적
# 음수,0 있음
# ( 길이 같, 안 빔 )
def solution(a, b):
    return sum( [i*j for i,j in zip(a,b)] )
# 해설_같

# 약수의 개수와 덧셈_https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 요소_약수의 개수 짝수-> 더함  => len %2==0
#  _ 홀수 -> 안 더해

# - 문제 읽기 & 필기
# : 1) 문제 읽기 : '문장 단위로 이해'하면서( 눈으로 '예시와 같이' 보면서), '필기'
# : 1.i) 이해 100퍼 확실하지 않은 부분 있으면, 예시 설명 읽

# - 3]code 경계값 조건 생각하며. (<-> 후 엄밀체크 : 풀이 조금이라도 길어지면 or 다른 부분에서 실수한 거 있으면, 나중에 복잡해서 더 찾기 어려워져.)

# 2]_m) 약수의 개수_ 순차적 의미 계승 있? => 걍 효율 무시 일반 방법
def solution(left, right):
    answer = 0
    for a in range(left, right + 1):  # 13, 17
        numb = 0
        # 2] 경계값 포함해야 ( int(15**0.5) = 3 까지 봐야지[ (,+1까지) ] ) & 경계값_-=1
        for b in range(1, int(a ** 0.5) + 1):  # 약수 ... 의 개수(_더 간단 알고리즘적혔을 수도_지금 굳이?) # m_제곱근 포함 & 후 -1
            if a % b == 0:  # 약수인 경우
                numb += 2
        # 경계값
        # if a**0.5 == int (a**0.5): # <  ==> while( k<n**0.5): 경계값 비포함 & 경계값_+=1
        if a ** 0.5 == b:  # 경계값((제곱근_중복 피하기))
            numb -= 1

        if numb % 2 == 0:  # 짝수개
            answer += a
        else:  # (그 당시 이상한데 결과가 같아도) 옳은 코드로 원상복귀 해두기.
            answer -= a
        # 4] i) 오류시 : 문제_입출력 예 설명에 나오는 변수들 출력
        # print(a, numb) # 15가 4가아니라 2개가 떠버림 / 24가 8가 아니라 6떠버림
    return answer


# - 해설 : 나/root(n)
# : 수학m_ 제곱근이 있는 숫자 = 약수가 홀수개다. (맞넹 내코드에서도 제곱근 조건이면 +2더하던 거에 -1해줬잖)
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer

# 문자열 내림차순으로 배치하기_https://school.programmers.co.kr/learn/courses/30/lessons/12917

# 문자를 내림차순 정렬
# 대문자 < 소문자
# : 소문자 -> 대문자
# ( 안 빔 )

# - sort // sorted 입출력형
# : 입력=리스트/츌력=없음 / reverse'd' //  입력= 반복형 / 출력=리스트/ revers'e'
# : 문자_오름차순 = 대문자부터
def solution(s):
    # 문자열로 합체
    s.sort()
    return "".join(sorted(s, reverse=True))

# 해설 : 똑같


# 부족한 금액 계산하기_https://school.programmers.co.kr/learn/courses/30/lessons/82612
# N 번째 이용 : price*N
# 모자람 -> count 번에서 얼마가 모자라는지
# 안모자람 -> 0

# (가격 자연수, 자금 자연수, 횟수 자연수 )
def solution(price, money, count):
    # 2] money - ( 4*price + 3*price + 2*price + price )
    a = money - (count * (price + count * price) / 2)  # 1,2..든 / *price까지든 등차수열. ((price 뽑아주면 아주 조금 더 효율인데 굳이))

    # 했던 실수_연산 때 * 붙이기! (특히 *(
    return abs(a) if a < 0 else 0  # 해설후 : -min(a,0) # '음수[양수]인 경우'라서 min[max].


# 해설 후
# - 0과의 비교 조건문 <=> max 함수
# : '음수[양수]인 경우'라서 min[max]

# 해설 : 값 식 동일
#     return max(0,price*(count+1)*count//2-money)

# 문자열 다루기 기본_https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 길이 4혹은 6인지 and 숫자로만 구성인지

# (안빔)
def solution(s):
    # 숫자로만 구성 : int() 쳌 => try
    a=True
    try :
        int(s)
    except:
        a=False
    return True if (len(s)==4 or len(s)==6) and a  else False

# 해설[시복 유사]
# (암기 노필요) 문자열 정수인지 = a.isdigit()
    # return s.isdigit() and len(s) in [4,6]

# 행렬의 덧셈_https://school.programmers.co.kr/learn/courses/30/lessons/12950
# -wise

def solution(arr1, arr2):
    # [1,2] [3,4]
    # [ 제거] [ [ 0]*n for _ in range(n)]
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]

# 해설[같음]
# return [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]

# 직사각형 별찍기_https://school.programmers.co.kr/learn/courses/30/lessons/12969
# mxn의 별
# (자연수)
n, m = map(int, input().strip().split())

for _ in range(m):
    print('*' * n)

# 해설 : 엔터포함된 str
# > string_'\n' = 엔터역할 ㄱㄴ
# answer = ('*'*a +'\n')*b
# print(answer)

# 같은 숫자는 싫어_https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 나_(127.31ms, 27.9MB)
def solution(arr):
    # O(n) 너무 클듯_ 되네
    # m_ot)특수 정보 : 0~9숫자인 거 이용.

    answer = [arr[0]]
    for a in range(len(arr) - 1):
        if arr[a] != arr[a + 1]:
            answer.append(arr[a + 1])
    return answer
# 해설_같 (136.67ms, 27.9MB)
# def solution(s):
#     # 함수를 완성하세요
#     a = []
#     for i in s:
#         print(a[-1:])
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a

# 예산_https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 최대 몇 개의 부서에 ㄱㄴ
# ( d = 안빔 , 요소_자연수 / budget = 자연수 )

# (0.04ms, 10.1MB)
def solution(d, budget):
    d.sort(reverse=True)
    count = 0
    while (len(d)):
        budget -= d.pop()  # pop=길이 체크하기_미리 몰랐다.
        if budget >= 0:
            count += 1
        else:
            break
    return count


# 해설 [ 효율성 안좋아보임 ]
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

# 이상한 문자 만들기_https://school.programmers.co.kr/learn/courses/30/lessons/12930
# '단어'의 짝수번째_대문자, 홀수_소문자
# ( s = 한 개 이상의 단어, 사이에 공백 무조건

#	23m_통과 (0.10ms, 10.3MB)
# - 대소문자 .lower()&.uppper() <-> 나_ord, chr
def solution(s):
    # print(ord('a') - ord('A') ) # 32
    # s.split() # "    "도 다 먹음
    # m_other) ord로 zip으로 한번에 연산하면 더 효율화 될 수도

    # 굳이 이중? 했는데, 어차피 연산시복 똑같고 / 단어당 index 짧은 코드로 보려면 이중이 낫겠다.
    # for a in range(len(s)):#'try'
    #     for j in range(len(a)):
    #         answer+=

    # str_ 요소 변경 안됨 -> concatenate 및
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] != ' ':  # 문자
            # 파이썬 이중 부등식(양꺽쇠) 안됨
            if count % 2 == 0 and ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):  # 짝수_대문자 (대문자->대문자(미변경)/소문자[]>대문)
                answer += chr(ord(s[i]) - 32)
            elif count % 2 == 1 and ord('A') <= ord(s[i]) and ord(s[i]) <= ord('Z'):
                answer += chr(ord(s[i]) + 32)

            else:
                answer += s[i]
            count += 1
        else:
            count = 0
            answer += s[i]  # 공백도 그대로 붙여줘야

    return answer


# print(solution("a        a    abab  abab  "))
# 해설_ 시복 비슷해 보이는데 걍 코드압축. 굳이 초압축복잡코드 이해 패스
# return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 크기가 작은 부분문자열_https://school.programmers.co.kr/learn/courses/30/lessons/147355
# count_수<=수

# _	통과 (6.00ms, 10.3MB)
def solution(t, p):
    pp = int(p)
    count = 0
    for i in range(len(t) - (len(p) - 1)):  # 7 3 -> 5
        count += 1 if int(t[i:i + len(p)]) <= pp else 0  # len 개

    return count
# 해설[같]

# 삼총사_https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 합하면 0이되는 삼총사_경우의 수
# ( number = 안빔, 요소_'정수'&중복가능 )

#	통과 (0.13ms, 10.1MB)
def solution(number):
    # 3개고르는 경우의수_탐색 => sort하고 처리 효율적이겠다? 굳이 그렇게까지? 입력 길이도 짧다

    count = 0
    comb = []
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number)):  # 뒤에서 자동으로 처리됨
            for k in range(j + 1, len(number)):
                comb.append([number[i], number[j], number[k]])
    for i in range(len(comb)):
        count += 1 if sum(comb[i]) == 0 else 0
    return count

# # 해설[비슷] 통과 (0.10ms, 10.1MB)
# def solution (number) :
#     from itertools import combinations
#     cnt = 0
#     for i in combinations(number,3) :
#         if sum(i) == 0 :
#             cnt += 1
#     return cnt

# 최소직사각형_https://school.programmers.co.kr/learn/courses/30/lessons/86491
# => max를 가진 가로 혹은 세로의 나머지 까지 저장
# : m1) max값 두가지씩? 100 9, 90 1 /1 100 2 99
# : m2) sort?
# ( sizes= 안빔, 자연수 )

#_	통과 (6.11ms, 11.3MB)
def solution(sizes):
    # 정렬효율? # 정렬이 접근n보다 더 시간 걸림.


    # k개 까지의 최소 명함하며 완전 탐색이 가능할까?
    # <-> 반례: 60 50, 70 100  : 70 100이 낳을지 100 70이 나을지 나중에 나오는 거 알아야 최적화<->나왔을 때 갱신하면 되지.

    big, small=1,1 # max()로 순서부여(정렬)_뒤집가능 무시
    #    side=[[1,1],[1,1]]
    for a,b in sizes :
        # maxv,minv=max(a,b),min(a,b)# 가로세로 무시
        # # 둘다 클때 # 엄밀 최적해 방법 헷갈릴때 = (for안) 조건_경우의 수 쪼개서 생각
        # if maxv >= big and minv >=small :
        #     big, small =maxv,minv
        # # 한쪽이라도 클 떄 # 60 30<- 70 30
        big, small = max( max(a,b) , big), max( min(a,b), small) # 압축본
#         elif maxv >= big :
#         elif minv >=small :
    return big*small
# -해설[압축]

# 숫자 문자열과 영단어_https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 문자열 단어 -> 숫자
# ( s= 안 빔, 결과=자연수 )

# _	통과 (0.03ms, 10.4MB)
def solution(str1):
    # upper() lo
    answer = ''
    i = 0
    while (i <= len(str1) - 1):

        if str1[i].islower():  # 소문자
            if str1[i] == 'z':
                answer += '0'
                i += 1 + 3
                continue
            elif str1[i] == 'o':
                answer += '1'
                i += 1 + 2
                continue
            elif str1[i:i + 2] == 'tw':
                answer += '2'
                i += 1 + 2
                continue
            elif str1[i:i + 2] == 'th':
                answer += '3'
                i += 5
                continue
            elif str1[i:i + 2] == 'fo':
                answer += '4'
                i += 4
                continue
            elif str1[i:i + 2] == 'fi':
                answer += '5'
                i += 4
                continue
            elif str1[i:i + 2] == 'si':
                answer += '6'
                i += 3
                continue
            elif str1[i:i + 2] == 'se':
                answer += '7'
                i += 5
                continue
            elif str1[i] == 'e':
                answer += '8'
                i += 5
                continue
            elif str1[i] == 'n':
                answer += '9'
                i += 4
                continue
        else:
            answer += str1[i]
            i += 1

    return int(answer)
# 해설- str1.replace()
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)


# K번째수_https://school.programmers.co.kr/learn/courses/30/lessons/42748

####m효율 어차피 정렬할것(굳이 안함)
# 자르고, 정렬, k번째 수
# 두 입력 안 빔, 입력1_자연수

# '번째' < -> 'index' 주의.
# 저장도안된 리스트슬라이싱.sort()처럼 막 연속기도 안됨
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = sorted(array[commands[i][0] - 1:commands[i][1] + 1 - 1])
        answer.append(temp[commands[i][2] - 1])

    return answer
    # 비자연수~/ n번쨰 숫자가 인덱스 초과 / 너무 어거지? -> 이 정도는 처리 안 해도 맞음 항상.

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


# 두 개 뽑아서 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    # m1) 라이브러리_구현이랑 t비슷. 걍편리함.) 통과 (4.84ms, 10MB)
    from itertools import combinations
    answer = []
    for a, b in combinations(numbers, 2):
        if a + b not in answer:
            answer.append(a + b)
    # m2) 통과 (4.93ms, 10.1MB)
    #     answer=[]
    #     for i in range(len(numbers)):
    #         for j in range(i+1, len(numbers)):
    #             if numbers[i] + numbers[j] not in answer :
    #                 answer.append(numbers[i] + numbers[j])

    answer.sort()
    return answer


# 해설 [비슷]
# - 나_중복 제거용 조건문 => set 씌워
# - 조합 = 예전 내가 생각해낸거((당연한거긴한데 이렇게 흔하게 있는 거였다늬. 그래도 set도 있긴해도 추천 많이 받은 코드에 있는 거니 의민 있겄지))

# def solution(numbers): # 	통과 (0.53ms, 10.1MB)
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))


def solution(food):  # [1, 3, 4, 6]
    # 구현속도용 풀이
    # : //2 -> a1 + '0' + a1[::-1]
    a = ''
    for i in range(len(food)):
        a += str(i) * (food[i] // 2)  # 반절(7_2로 나눈거)에서 사용개수(15->14_나머지1버려짐)
    return a + '0' + a[::-1]

# 해설 [시복 같]
# - 문자열을 중간부터 만들어나가는 부분이 흥미롭
# : answer = str(i) + answer + str(i)

# def solution(food):
#     answer ="0"
#     for i in range(len(food)-1, 0,-1):
#         c = int(food[i]/2)
#         while c>0:
#             answer = str(i) + answer + str(i)
#             c -= 1
#     return answer


# 콜라 문제_https://school.programmers.co.kr/learn/courses/30/lessons/132267
# int(20/2) > # (넘 짧고 쉬워서 적으려다 그냥 바로 구현 들감)

# - 한글 주석으로 핵심 코드 의미 적어놔야, 더 엄밀 가능한듯. 놓치는 거 디버깅으로 발견하긴 하지만 ㅎㅋㅎ
# 통과 (0.48ms, 10.2MB) # 빈도는 0.01가
def solution(a, b, n):
    left = n
    answer = 0
    # m_s) 굳이 반복?   등차등비(//a)*b  등 방법 있을 것 같
    # m) 걍 구현속도용풀이로해보자
    # n= a* k + a보다 작은 수 # k
    while (left >= a):
        answer += (left // a) * b  # k*
        left = left % a + (left // a) * b  # 남은거=먹고남은 거 + 새로 받은 거

        # 음수시 몫 나머지는
    return answer

# 해설 [시복 비슷] # 굳이? 내 추가 시간소모 X
# solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# 추억 점수_https://school.programmers.co.kr/learn/courses/30/lessons/176963
# name = 안빔 자연수, 중복 없
# yearning = 안빔 자연수
# photo = 안빔. 자연수 중복없

# - 실수 방지 : 주석으로 현재값 & 상태 # ["may",
# 통과 (1.40ms, 10.7MB)
def solution(name, yearning, photo):
    # 구현 속도 피지컬용 풀이
    target = dict(zip(name, yearning))
    answer_all = []

    # !@ 없는 놈 나올 수 있구나 ㄷㄷ
    for i in photo:  # ["may", "kein", "kain", "radi"]
        answer = 0
        for j in i:  # "may"
            answer += target[j] if j in target else 0
        answer_all.append(answer)
    return answer_all
# 해설[비슷]
# :나_딕셔너리 굿<-> 코드 압축용으로 index 쓰심

# 명예의 전당 (1)_https://school.programmers.co.kr/learn/courses/30/lessons/138477

# 매일 점수 -> k 번쨰 이내 = 목록올림 (k 번쨰놈보다 크면) -> 최하위점수
# : 제한
# k=자연수
# score=안빔, 0이상, !중복 ㄱㅊ

# - 쉬운데 괜히 sort같은 거 안쓰려다 시간 더 걸림(오히려 예쌍과 다르게 쓰는것도 ㄱㅊ했기도) -> 시복 비슷하면 그냥 구현속도용 방법으로 ㄱㄱ
# - 생성한_배열 길이!!생각
def solution(k, score):  # 통과 (1.09ms, 10.3MB)

    # 상위3개중 min값
    result = []
    topv = []
    for i in score:  # 10, 100, 20
        if len(topv) <= k - 1:  # ~! 2-> 결과로 3됨 ### 아침 꽉 안찬상태일때! pop쓸때! 길이주의
            topv.append(i)
        elif i > topv[-1]:  # 랭킹화 # 'minv'와의 중복은 무시가능.
            topv.pop()  # 젤 작은놈제거 ## 중복가능하니 한개만 ## 인덱스주의
            topv.append(i)
        topv.sort(reverse=True)

        # 단순 minmin아냐. 300나오면 어쩌려구 # topv필요할듯. 값 업데이트 하다보면 나중에 비교할 일 생겨서결국.

        result.append(topv[-1])  #
    return result

# 해설
# - 근데 해설법 remove중첩min 이 시복 더 큰거같기도 nn
# - 해설_간단_"remove(min)" <-> 나 sort&pop&[-1]
# .remove(min(q))


# 카드 뭉치_https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 카드=길이1이상 / 영단어 적힘 / 서로 다른 단어 존재? 각각? 애매해서 굳이 신경 안 써도 되는 문제일듯

# 중복 불가. 카드 순서 사용.
def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0
    for a in goal:
        # '인덱스 체크' 'and' '인덱스 사용'# 파이썬 특이라 앞 False면 뒤 안함
        if index1 <= len(cards1) - 1 and a == cards1[index1]:  # index =index error 체크
            index1 += 1
        elif index2 <= len(cards2) - 1 and a == cards2[index2]:
            index2 += 1
        else:
            return "No"
    return "Yes"

# - 해설[유사]
# - pop보다 <-> 나_index+1 접근이 계산.은 효율일듯. 메모리 까지하면 놉

# 2016년_https://school.programmers.co.kr/learn/courses/30/lessons/12901
# 1.1 금요일
# 윤년 = 4년마다, 2월 29일
# 4,6,9,11 _30일


def solution(a, b):
    answer = ["SUN","MON","TUE","WED","THU",'FRI','SAT'] # 일요일,
    # a월1일 > a-1월 말일
    months=[31,29,31, 30,31,30,31,31,30, 31,30,31] # -1 >a월 이전월[a-2]
    # 총일    # +b일
    return answer[ (4+sum(months[:a-2+1])+b) %7 ] # 변수 계수 식 세우고& <= 초기값 대입 생각. # 1 # +4

# 해설[유사]
# - 그나마 초기값 반영을 아예 => [0]을 금요일로 한거?. 근데 음 굳이
# 나_연산 효율 > 타코드는 그나마 메모리효율? 코드간단화?
#  노가다 개웃기네


# 폰켓몬_https://school.programmers.co.kr/learn/courses/30/lessons/1845
# N/2 가져도 된대_ 최대한 많은 종류의 개수
# 안빔_ , 자연수

def solution(nums):
    a = set(nums)  # 몇 종류 있니 # 7개
    max_get = len(nums) / 2  # 6개 #N/2
    return min(len(a), max_get)
# 해설 똑같

# 과일 장수_https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 사과 [1,k]점_ m개
# 박스 가격 = 가장 낮은 점수 * m개
# 가능한 많은 사과를 팔 수 있을 때, ㄱㄴ 최대 이익
# *이익 미발생 =0, max(0, result)

# - !문제 암기, 필기 놓침_여러 상자 팔 수 있음
def solution(k, m, score):
    # 여러 상자=비싼놈들끼리 하는게낫다. 최저점이 어차피 하향평준화라.
    # 최고 점수부터 > 그중 가장 최저점수min
    score.sort()
    # -파라미터 안쓰이기도. k가 안 쓰이긴 하네

    # # m2) [시간비슷]통과 (92.71ms, 21.6MB)
    # i=m
    # result=0 # comprehension과 sum으로 압축할 수 있는데 그건 시복 좀 더 생기는 건 아닌데(O(1)연산등이라).연결연산이긴해서. 이건 메모리 추가 버리는 거 같긴 했는데 걍 다 비슷
    # while(i <= len(score) ): # 뒤에서 i번째라 그냥 인덱스 아님. # 뒤에서 n개수 번째까지 ㄱㅊ
    #     result+=score[-i]*m # ! 점수 "*개수"
    #     i+=m
    # return max(0,result)

    # m1) (100.05ms, 21.6MB)
    return max(0, sum([score[-i * m - m] * m for i in range(len(score) // m)]))  # m개 #

# - 해설_[유사]_내께 낫다 (110.04ms, 26.1MB)
# : 나_for 대신 해설_slicing  : 그걸 n~ 만큼 해서 시간 비슷
# return sum(sorted(score)[len(score)%m::m])*m
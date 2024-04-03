# 정수 내림차순으로 배치하기_https://school.programmers.co.kr/learn/courses/30/lessons/12933
# : 118372 -> 873211_'자리수'_'큰 순서'로

# > 연속 <-> 자릿수

# A) '123'->[1,2,3] 
# list(str) : str에 씌우면_'ab'붙어있어보여도 순서있는놈 list순서로 옮기는 것 뿐( 출력 꼴은 분해같아 보여지긴함) 
# >> 반복형 객체 --map ->반복형 객체
# list(  map(int,'123'))  # 변경 대상) map_'요소의' 형식, only'list( 를 map에 _ 합체

# <-> str(list1) : 설령(자료형 바꿀필요 없는데도) map까지 씌우고해도 분해 반대인 강제 합체 안됨(비가역적). 분해했다가 작업해야
# B) [8,7..]-> '87..' (( -> 87..)) 변경_요소형식 & 합체
# m1) concatenate
# answer=''
# for k in [8, 7, 5]:
#     answer+=str(k)
# answer=int(answer) 
# m2) 
# 1) [8,7.. -> ['8','7',..] 요소 형식
# 1.m1) [    str(k) for k in [8,7,5]]  # (list?) comprehension
# 1.m2) list   (map(str,[8,7,5] )) 
# 2) ['8','7',..] -> '87..' 합체
# answer=''.join(answer)

def solution(n): #118372
    # - list(str1) # '리스트'를 씌울 때만 입력 분해 # '12'-> ['1','2']
    
    # 1) [자리수] 정보 =str사용
    a=str(n) #'118372' 
    
    # 2) 큰 순서 = sort 필요 = list화
    a=list( map(int, a) ) # list화 [8,7..
    a.sort(reverse=True) #[8,7..
    
    # 3) [한놈으로 각 자리들을 합치기]=in str _ join ((or 값을 x10^n 씩_시복 자릿수일듯.))
    #  -> str -> _join
    answer=[str(k) for k in a] #['8', ..
    answer=''.join(answer) # 리스트(iterate)의 요소가 str이어야 # '87..'
    
    answer=int(answer)
    return answer
# 추후_문자열값도 sort 가능
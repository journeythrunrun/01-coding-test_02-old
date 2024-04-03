# 0) "banana"	3
# 두 횟수가 같아지면 분리 -> 몇 개로 나눌 수 있니

# 123) 
# 첫 문자=x 
# -> for_if x : cnt_x +=1 else : cnt_x_not+=1  (X_OR count x & -그값)
# -> if cnt_x ==cnt_x_not : answer+=1 ((문자열 분리)) & 다음 번 x리뉴얼(newx=True)  
## & 남은부분 없으면 종료

## 굳이 효율화를 위해 안할랭
## -> if cnt_x > ~ 
## 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.

# -> 분해한 문자열의 개수


def solution(s):
    answer = 0
    cnt_x, cnt_x_not = 0,0
    newx=True
    for a in s :
        if newx==True:
            x=a # ex) b
            cnt_x, cnt_x_not = 0,0
            newx=False
        if a==x:
            cnt_x +=1
        else :
            cnt_x_not+=1
            
        if cnt_x ==cnt_x_not :
            answer+=1 
            newx=True 
    if cnt_x !=cnt_x_not : # 마지막에 개수 안 맞는 나머지 문자열인 상태였는지
        answer+=1
        
    return answer
# ; '분해한' 문자열 개수라, 딱 안 맞는 나머지 문자열 있으면 +=1임
# : 14m / 성능 : +5 & 최대 1.83ms

# - 다른 사람 풀이 ( 성능 비슷 _ 코드 효율화 )
# : 2) " '분해한' 문자열 개수라, 나머지 딱 안 맞는 나머지 문자열 있으면 +=1"을 맨 처음에 더함 & 같을 때 그 다음번 회전에 +=1 [ 논리적흐름 일치 연산보다 논리적 1대1 맵핑 해결 느낌 ]  ---> 분리기(-) 때 count한다고 볼 수도 있음
# :: 막판 때, 나머지가 있으면 그 나머지는 맨 처음에 더했었고 나머지 때 이전일치+1, 나머지가 없었으면 맨 처음에 더해줬던 1이 마지막 일치 더해준 셈. 
# : 개수 비교 및 answer+=1을 조건의 맨 앞에 둠으로써(다음 번에 더함) -> 리뉴얼 시 연산도 그때 한번에 함.

# def solution(s):
#     answer = 0
#     sav1=0
#     sav2=0
#     for i in s:
#         if sav1==sav2:
#             answer+=1
#             a=i
#             print(i, answer)
#         if i==a:
#             sav1+=1
#         else:
#             sav2+=1
            
#     return answer
#[1] 임은성 , ddcd , 성혜경 , keepithunnyt 외 340 명
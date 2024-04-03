# 두 문자열인 숫자에서, 공통으로 나타나는 정수 짝꿍(0~9) 찾기 (공통 문자 개수 같아야함)
# -> 짝꿍을 한 덩어리로 여기고 배열하여 만들 수 있는 max 정수 & 전부 0들이면 0화 & 없으면 -1 

# 2) 0~9 count : X.count() , Y. 
# -> 9부터 count값만큼 concat (& natu_True) & 0만 있으면(&natu_False) 0화 & 0도 없으면 -1

# Again 2) for zip X,Y ->각 cntx,y[인덱스]+=1  -> for i in 9~0 answer+=i*(min(cntx[i],cnty)) //2??? &ii) sum(cnt)[시복줄이려면 루프 밖에서 계산저장해도 됨)==cnt[0] : 0화 &iii) (먼저) ==0 : -1
# 장점 : 이전2) 10*(2)n <-> 이번2) 따로 인덱스이용하여 저장법 n+10
# sum쓰면 시복 느는 단점있지만, 원래의 빠른 조건문 떠올랐어도 쓰기 귀찮아서 적은 방법 
def solution(X, Y):
    answer = ''
    natu=False
    # print('check:','1'*0,)
    for i in range(9,-1,-1): # 9~0
        cnt_x=X.count(str(i))
        cnt_y=Y.count(str(i)) # 문자열에서 정수문자 찾을 때, 'str' 씌워야함. !=chr ord
        cnt_xy=min(cnt_x, cnt_y)
        if cnt_xy>0 and i!=0: # 0만 있는 조건 체크용 변수 저장
            natu=True
        answer+=(str(i)*cnt_xy) 
        if i==0 and natu==False and cnt_xy>0 : # for 안이 더 틀 안 코드일줄. 걍 for 밖이 나았겠다. = natu랑 cnt_xy만 체크 해도 됨 [ 더 적게 체크해도됨 ]
            answer='0' #재정의 됨
        elif i==0 and natu==False and cnt_xy==0:
            answer='-1'
    return answer

# : 23m / 성능 : +8 & 최대 102.95ms

# - 다른 사람 풀이
# : 비슷 & 코드 압축 적기(이건 익숙해지면 자동으로 될 듯)

# > 좀 더 간단한 조건 체크
# : 0만 있는 조건 : len(answer) == answer.count('0') ## count 또 해야하긴 해도 시복은 동일.
# : 공통 없는 조건 : if answer == '' :

# def solution(X, Y):
#     answer = ''

#     for i in range(9,-1,-1) :
#         answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
#     if answer == '' :
#         return '-1'
#     elif len(answer) == answer.count('0'):
#         return '0'
#     else :
#         return answer
# [1] gusjo , 탈퇴한 사용자 , Hyunsung , hyeyoonc 외 247 명
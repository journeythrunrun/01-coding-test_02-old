# 1) 0~9, 상하좌우 움직임
# 2열 : 각 엄지손가락의 현재 위치 중_ (다르면)더 가까운 쪽 사용 & (같으면)어디손잡이

# 2) 몇번째 열 -> i) 왼손위치업데이트, answer+='L' iii) 오른손위치업데이트, +=
# ii) 거리값[,] : 왼_new=hand[0]+ (1 if hand[0] in first else 0 )-> dist[0]=abs(target-new)//3 +(1 if hand[0] in first else 0 ) )      ->() 
# : 

def solution(numbers, hand):
    answer = ''
    first=set([1,4,7,10])
    second=set([2,5,8,11])# 0-> 11화
    third=set([3,6,9,12])
    # print(first)
    posi=[10,12]
    for numb in numbers :
        numb= 11 if numb==0 else numb
        
        if numb in first : 
            posi[0]=numb
            answer+='L'
        elif numb in third:
            posi[1]=numb
            answer+='R'
        else :
            # m2 코드 효율화 _ 어차피 거리값 안쓰고 '비교'만 함_ 하다가 다른 오류 이유 떠올라서 수정 안했음
            # L 이 가까울 조건 , 왼오값 차이 +-1
            # distL = abs(posi[0]-numb)//3    + (1 if posi[0] in first else 0)
            # distR = abs(posi[1]-numb)//3 +  (1 if posi[1] in third else 0)
            # m1
            # # 그냥 // & 나머지 날아가는 것 이용해서 식 간략화 가능할 것 같지만, 연산 1대1체크가 시간소비.
            
            # ; new변수 식에 합쳐줄 때 괄호 
            distL=abs(numb-( posi[0]+ (1 if posi[0] in first else 0) ))//3 +(1 if posi[0] in first else 0 ) #~
            # (왼)new=posi[0]+ 가운데라인화_(1 if posi[0] in first else 0 ) --> dist[0]=abs(numb-new)//3 + 가운데라인으로들어간 거리비용_(1 if posi[0] in first else 0  )
            distR=abs(numb- (posi[1]+ (-1 if posi[1] in third else 0) ))//3 +(1 if posi[1] in third else 0 )
            
            force=0
            if distL == distR :
                force=1 if hand=='left' else 2 
            if distL < distR or force==1:
                posi[0]=numb
                answer+='L'
            elif distR <distL or force==2:
                posi[1]=numb
                answer+='R'
                
    return answer
# : 44m / 성능 +3, (0.63ms)

# ; 변수 이름 안 겹치게 미리 다 봐

# - 디버깅 
# > *,#에 해당하는 10,12를 초기 변수에 안 넣어놔서 극히 일부 케이스에서 오류 생김
# >; 한 변수 식을 다른 변수 식에 합쳐줄 때 '괄호' 걍 항상 미리 넣어.

# - 다른 사람 코드
# : (( 키에 따른 값을 딕셔너리 키의 벨류에 두개씩 넣어 놓으셨네._복잡 case 시 한계 <-> 나_조건문_+=1 ( if in first  ) ))

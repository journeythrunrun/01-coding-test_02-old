# 세 번의 합계 : 0~10 ^ &S1승 D2승 T3승 
# if * : (현재점수+바로 이전 점수(초기회0))*2 => 이전점수 곱해진 걸로 업로드 
# elif # : 현재 점수 *=(-1) => old 이 마이너스로 업로드


# CH: 예제 4번 4배 케이스

def solution(dartResult):
    answer = 0
    old=0
    aa=0
    # X_10 처리하기 귀찮으니까 금방 생각난 방법인, 타입별 병렬 저장법
    numb=[]
    sng=[]
    opti=[]
    re=False
    firs=True
    option=False # 1초기화 2사용 3재정의
    # 마지막 다트에 따른 계산은 for 나와서 하고 (X_len으로 포착) / (10귀찮X)_나머지 다트에 따른 계산은 다음 정수 등장 시 할까
    for a in dartResult :
        # 정수
        if ord(a) >=ord('0') and ord(a)<=ord('9') : # 조건 : 문자열 여러 가지 범위 (정수 등)->ord # 다른 사람 else법이 더 나음
            #[11)] old를 옵션의 종류에 따라 다르게 저장하고 있었음->무조건 최종 값에 더하기 전의 aa를(answer+=aa) 그대로 old에 저장하면 안됨.  # 세 번째 케이스 '옵션이 없었을 시', 다음 다트에서 aa를 그대로 old에 저장
            if option==False :
                old=aa 

            #~ 연산
            a=int(a) # 정수화
            if a==0 and re==True : # 10 # re : 10 체크용
                aa=10 # aa 이번 다트'로 인한' 점수 계산중 ( 옵션에 의해 이전 다트에 대한 것도 더해질 수 있음)
                # numb.pop()
                # numb.append(10)
                # 이 조건에선 최종결과에 더하는 계산 안했던 이유 : 10에서 1이 뜰 때 이미함.             
            elif a==1 : 
                if firs==False : # 첫번째 다트 아닐 때 ( 이전 다트 점수->최종결과반영을 다음 다트 숫자에서 함 )
                    #old=aa # 이번에 던진 다트로 인해 얻은 점수를 저장해둠.
                    answer+=aa # 최종 결과에 이번 직전에 던진 다트로 인한 점수 반영
                
                re=True
                aa=a
                # numb.append(a)
                continue # 10체크 위해 re=False화 안하기 위함임(그렇게 코드 위치 설계함).# 지양하는 게 나을 수도 있으려나
                
            else : # 다른 정수
                # numb.append(a)
                if firs==False :
                    # old=aa
                    answer+=aa
                aa=a
                
        elif a=='S' :
            option=False 
            ### 옵션이 존재할 시, 이번 이전 다트에 대한 old값도 연산에 쓰인다. 따라서 이번 다트에 대한 값을 old에 덮어버리면 안됨.(쓰일 수 있는 이전 old값 상실) # 옵션이 없을 시 old 저장은 옵션 단계 지난 후 가능.
        elif a=='D' :
            aa=aa**2
            option=False
        elif a=='T' :
            aa=aa**3
            option=False
            
        elif a=='*' :
            # m_for 진행하면서 연산 이유: m_병렬__옵션은 존재가 선택이라 단순 append하면 몇 번째 다트에 해당하는 연산인지 헷갈림. count하면 되긴함(코드수정 귀찮). 
            # old=aa*2
            aa,old=(aa*2+old),aa*2 # : old는 이미 이전 텀에 한번 더했어서 한번만 더해줌. X_(aa+old)*2,aa*2 
            option=True # 옵션이 없는 조건을 체크하여 추후 old를 저장하기 위함

        elif a=='#' :
            aa*= -1
            old=aa 
            option=True # 옵션이 없는 조건을 체크하여 추후 old를 저장하기 위함
        
        re=False
        firs=False
        
    # 마지막 다트에 의한 연산에서는 old를 저장해 놓을 필요 없음.    
    answer+=aa
    print(answer)        
    return answer
# - 디버깅_정답률 93
# > 오류 찾은 방법 : 정답률 93퍼 정도였어서 극히 예외라 그런지, 코드 논리 분석법을 통해 해결 = 옵션 단계에서 특정 변수에 연산한 것 & 변수값 저장 시 '옵션 미등장 케이스' 놓침 
# > 다른 케이스 시도
# solution("10S2D*3T") # 55 # 37-2+20 맞넹
# solution("1S2D*10T") # 1010 # 37 -27+1000 맞넹 

# - 알고리즘 후평가 
# > m :걍 각각 병렬 저장 & count가 나았을듯. / for 흐름 속 변수 정의 및 사용 복잡함

# - 결과 (최대 0.01ms)
# - 코테 주의점
# ; 변수의 사용 의미범위 주의

# - 좋은 풀이
# > 10을 replace로 찾아서 처리
# : = dartResult.replace('10','k')
# -> 입력 문자열을 각 문자의 '역할'에 따라 '배열의 각 요소로 저장'함
# : =  ['10' if i == 'k' else i for i in dartResult]
# -> SDT : in을 사용하여 한꺼번에 조건체크 (( & 연산시 sdt.index(j) 사용 ))
# -> old보다 [i - 1]사용이 좋음( 다트당 계산 값 또한 병렬저장) ( 말했던 병렬저장법과 유사 )
# -> [good]정수 범위 조건 : 그냥 else로 처리 
# ** 조건 설계법 : 더 간단한 조건 먼저 모두 처리 & else
# [1] - , - , - , osjf 외 18 명

# 0)
# today	terms	privacies	result
# "2022.05.19"	["A 6", "B 12", "C 3(1~100)"]	
# ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"][1, 3]

# : A~Z / term에 약관 중복X
# : -> index +1 번_ 오름차순

# 1)
# : 약관별 유효기간 (+ -> 해당 일부터 파기)
# -> 오늘 날짜에서 파기해야/돼있어야할, 개인정보 번호
# : 모든 달은 28일

# 2) private에 따른 or 미리 정렬
# term (정렬 안돼있을 수 있음) -> dict에 저장
# :: 날짜 비교 다 일화할까. or  [년,달,일] 
# today<=deadline : 파기 # 데드라인 : private[i][0]+dict1[]
# :: deadline[0]+= (-)//12 ,deadline[1]= 
# -> index +1 번_ 오름차순 / 

import string
def solution(today, terms, privacies):
    answer = []    
    dict1=dict()
    dict1=dict1.fromkeys(list(string.ascii_uppercase),0) 
    for word in terms :
        dict1[word[0]]=int(word[2:])
    today=[int(today[:4]),int(today[5:7]),int(today[8:10])]
    for i, person in enumerate(privacies) :
        # 식 귀찮
            # today>=deadline : 파기 # 데드라인 : private[i][0]+dict1[person[11]]
    # :: deadline[0]+= (-)//12 ,deadline[1]= 
    # # 식 귀찮
        # deadline[0] +=( deadline[1]-dict1[person[11]] )//12 # +유효기간_dict1[person[11]] # 초과분
        # deadline[1] += ( dict1[person[11]] ) %12
        deadline=[int(person[:4]),int(person[5:7]),int(person[8:10])]
        plus=dict1[person[11]]
        while(plus>0):
            if deadline[1]!=12:
                deadline[1]+=1
            else : # 12
                deadline[0]+=1
                deadline[1]=1
            plus-=1
        # if today>=deadline :# '>'= # 파기
        for j in range(3):
            if j==2 and today[j]==deadline[j]:
                answer.append(i+1)
            if today[j]>deadline[j]: # 파기
                answer.append(i+1)
                break
            elif today[j]<deadline[j]:
                break                
    answer.sort()
    return answer
# 53m / +6 / 최대_1.98ms
# - 디버깅
# >; 문자열형인 숫자 -> 숫자형 _ 자리수 주의 (1~100)

# - 다른문제_ 나 달에 따른 일 모름 
# 31일 = {111,3,5,777 ,8,10,12} # 행운의 숫자 7이라, 얘만 1 칸만 가도 됨 ㅋ ㅎ
# 30 = {444,666,   9,11} # 4에서 시작해서 육시럴...땐 3칸이나 가야해..ㅋ..
# 29 = { "윤년"(4년마다의) 2월 } # 원래 9는 할인"이벤트"임 ㅋ
# 28일 = { 평년 2월 }

# - 다른사람 코드
# > m2로만 적어놨던, 일화 계산이네. 이게 더 간단해보이기도함
# > str형숫자 -> 숫자형 _speed   : map(int, date.split _ )
# # : ear, month, day = map(int, date.split("."))
# def to_days(date):
#     year, month, day = map(int, date.split("."))
#     return year * 28 * 12 + month * 28 + day
#
# def solution(today, terms, privacies):
#     months = {v[0]: int(v[2:]) * 28 for v in terms}
#     today = to_days(today)
#     expire = [
#         i + 1 for i, privacy in enumerate(privacies)
#         if to_days(privacy[:-2]) + months[privacy[-1]] <= today
#     ]
#     return expire
# [1] imsiyun , 맹구 , tultle93@gmail.com , 이수달 외 3 명
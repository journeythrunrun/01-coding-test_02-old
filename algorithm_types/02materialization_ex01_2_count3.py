# 1. 문제 : 3 있는 시각
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩

# 코딩빠르기용 법
N=int(input()) #_10
time=[0,0]
count=0
for i in range(N+1):
    if i==3 or i==13 or i== 23 :
        count+=60*60
        continue

    else:
        # while&t카운트 연산 -> for두개 대신
        while (time[0] <= 59) : # m_) 0부터 59 #분에서 이미 3나왔으면 *60하고 continue 해도되긴함
            if '3' in str(time[0])   or '3' in str(time[1]): # m_) %3, %30==0  ##[string index out of range]if str(time[0])[0] == '3' or str(time[0])[1] == '3' or str(time[1])[0] == '3' or str(time[1])[1] == '3':
                count += 1
            time[1]+=1

            if time[1] == 60: # 실제 시각_실제값으로의 조정은 무조건 바로 해줘.
                time[0] += 1
                time[1] = 0

        time=[0,0] # 초기화! (( 초->분, ! 분->시간))
print (count)
#27m

# - 느낀점
# : 수학적 방법(공간 복잡도 good)보다 코딩속도를 위해 하나하나 반복문에서 따지기 법을 썼는데, 코드가 복잡하니 '구현'면에서 더 걸려버림






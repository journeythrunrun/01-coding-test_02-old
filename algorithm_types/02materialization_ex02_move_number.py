# 1. 문제 : 왕실의 나이트
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩

position=str(input()) #ex_c1 # list ['c','1']# str 'c1' 반복접근 가능
move=[ [2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]  ]
count=0
new=[0,0]
for i in range(8) :
    # 1) 계산_8가지
    new[1]=ord(position[1]) +move[i][1]
    new[0]=ord(position[0])+move[i][0]
    # 2) 조건
    if new[0] < ord('a') or new[0] > ord('h') or new[1] < ord('1') or new[1] > ord('8') : #    if position[1] < 'a' or position[1] > 'h' or position[0] < 1 or position[1] > 8 :
        continue
    count+=1

print(count)

# 35분: 파이썬 문법을 잘 모름
# > string_'abc'_[0]:a
# > 아스키코드 자동아님 _c언어와 다름
# >> 영어숫자화 : ord(aa[0]) - ord('a')
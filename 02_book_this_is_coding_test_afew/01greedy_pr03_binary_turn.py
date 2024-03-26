# 1. 문제 : 이진수 문자열 뒤집어서 다 똑같은 숫자로 만드는 최소 횟수
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
inpu=input()
first=True
old=inpu[0]
count=0
for i in inpu:
    if first==True : # (문자열의 각 요소를) 비교하기 위해 첫 번째는 패쓰
        first=False
        continue
    if old!=i : # 저번 값과 현재 값이 다르면
        count+=1 # count
        old=i
print( (count+1)//2 )
#19m
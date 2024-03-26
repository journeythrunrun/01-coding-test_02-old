# 1. 문제 : 곱하거나 더해서 만드는 최대 수
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
inpu=input()
old=0

for i in inpu : # i==new
    old=max(old+int(i), old*int(i))
print(old)

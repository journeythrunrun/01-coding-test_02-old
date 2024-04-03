# 직사각형 별찍기_https://school.programmers.co.kr/learn/courses/30/lessons/12969
# mxn의 별
# (자연수)
n, m = map(int, input().strip().split()) 

for _ in range(m):
    print('*'*n)
    
# 해설 : 엔터포함된 str
# > string_'\n' = 엔터역할 ㄱㄴ
# answer = ('*'*a +'\n')*b
# print(answer)
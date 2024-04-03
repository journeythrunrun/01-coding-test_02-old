# 핸드폰 번호 가리기_https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    leng=len(phone_number)
    num=leng-4
    # m1) join [t_똑같]
    return ''.join( ['*'*num,phone_number[leng-1-3:] ]) #concatenate
    
    #m2) print [통과 (0.01ms, 10.2MB)]                     
    # return'{}{}'.format('*'*num,phone_number[leng-1-3:]) # 뒤에 네개 그냥 [-4:]

# 해설 : 유사
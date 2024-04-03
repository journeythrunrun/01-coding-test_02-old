# 문자열 다루기 기본_https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 길이 4혹은 6인지 and 숫자로만 구성인지

# (안빔)
def solution(s):
    # 숫자로만 구성 : int() 쳌 => try
    a=True
    try :
        int(s)
    except:
        a=False
    return True if (len(s)==4 or len(s)==6) and a  else False

# 해설[시복 유사]
# (암기 노필요) 문자열 정수인지 = a.isdigit() 
    # return s.isdigit() and len(s) in [4,6]

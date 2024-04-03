# 1. 문제 :
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩

# - 해설

def split(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:  # 올바른 말고 그냥 균형은 )먼저 등장해도 되니까. <하면 안됨
            return i #! index쓸 꺼니까 index i~

def proper(u):

    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        elif u[i] == ')':
            if count == 0:
                return False
            count -= 1
    return True





def solution(p):
    answer = ''
    if p == '':
        return answer
    #index = balanced_index(p)
    index=split(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if proper(u) :
        answer =u+ solution(v)
        # ~ join
    else:
        c = '('
        c += solution(v)
        c += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':  # 4-4
                c += ')'
            else:
                c += '('
        answer = c
    return answer


# 이것이 코딩테스트다_난이도 1_풀이시간 20분

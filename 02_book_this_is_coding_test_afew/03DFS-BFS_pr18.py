# - 해설

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/60058



# 나 2차
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


# 완전 첫 시도
# - 다른 방법 < - > 내 아이디어 : count[0] >= count[1] & bool
# : bfs/dfs를 쓴다면 stack으로 ()pair때마다 상쇄?[dfs]

def who(p_list):
    count = [0, 0]

    right = True  # u 비진 않았
    for i in range(len(p_list)):
        if p_list[i] == '(':
            count[0] += 1
        elif p_list[i] == ')':
            count[1] += 1

        if count[0] < count[1]:
            right = right and False #+ 나_'and False'로 값 누적 <-> 해설_return해버림

        if count[0] == count[1]:
            key = i
            u = p_list[:key + 1]
            v = p_list[key + 1:]
            if right == True:  # 3.
                result.append(u)  # [ ['(',  ],
                who(v)

            # return u,v , right
    return u, v, right

def solution(p):
    result = []
    if len(p) == 0:
        return p
    p_list = list(p)  # [ '(', ')',

    # 2)
    u, v, right = who(p_list)

    # for
    # 3) i) 올바른 문자열

    left = []
    else:
    ['('] + left


return answer


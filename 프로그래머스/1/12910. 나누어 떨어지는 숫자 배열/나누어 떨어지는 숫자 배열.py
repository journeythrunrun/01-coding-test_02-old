# 나누어 떨어지는 숫자 배열_https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 나누어떨어지는지 > 오름차순sort
def solution(arr, divisor):
    # 공통 없음
    answer=[]
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if not len(answer) : #len 시복 1?>
        return [-1]
    answer.sort()
    return answer
# 해설 : 압축만 다름_comprehension & if, (sorted바로 반환)
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

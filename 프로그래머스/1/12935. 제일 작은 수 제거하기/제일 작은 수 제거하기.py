# 제일 작은 수 제거하기_https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 1) min 값 제거 
# 2) if 빈 -> [-1]
# ( 중복 값 없
def solution(arr):
    minv=sorted(arr)[0]
    # m1) [	통과 (6.37ms, 15.4MB) / 최빈 0.0n]
    # for이 시복 좋을 듯
    i=arr.index(minv) # O(n)
    arr.pop(i) # O(n)
    return arr if len(arr) else [-1]

# - 해설[큰 차이 없] : min() ((min_뇌를 스쳤는데 빨리 안 잡으면 사라지는 듯. 걍 이미 생각했던 for 방법 쪽이라 pass한 걸 수도 ))
# : 코드 압축하시느라 n^2된거고 / min 값 '병렬로 저장'하면 2ㅋ*O(n)
# return [i for i in mylist if i > min(mylist)] # O(n^2)
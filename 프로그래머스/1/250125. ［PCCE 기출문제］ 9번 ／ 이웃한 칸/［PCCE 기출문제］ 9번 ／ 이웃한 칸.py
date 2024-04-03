# dfs bfs 비슷하네. 걍 지도문제류라 그런가.
def solution(board, h, w):
    n=len(board)
    count=0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1] # 3.1)
    for i in range(4): # 3.2)
        h_check, w_check = h + dh[i], w + dw[i] # 3.3)
        if h_check >=0 and h_check <=n-1 and  w_check >=0 and w_check <=n-1 :
            if board[h][w]==board[h_check][w_check]    :
                count+=1
        
    return count
    
# : 6m / +2 / 최대 0.01ms


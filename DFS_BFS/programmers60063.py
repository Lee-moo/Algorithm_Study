# https://programmers.co.kr/learn/courses/30/lessons/60063

# n*n 크기의 지도에서 2*1 크기인 로봇을 움직여 (n*n) 위치까지 이동
# 로봇은 (1,1)에서 시작하며 지도 내에 표시된 숫자 '0'은 빈칸 '1'은 벽
# 두 칸 중 어느 한칸이다로 (n*n)위치에 도착하면 된다.

# dfs로 풀이 가능

def solution(board):
    answer = 0
    return answer


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

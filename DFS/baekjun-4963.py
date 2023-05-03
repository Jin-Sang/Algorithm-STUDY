# 테스트 케이스의 갯수가 정해지지 않은 특이한 문제
# 각 테스트 케이스에 대한 정답을 모아뒀다가 한번에 출력해도 되고, 바로바로 출력해도 됨
# 항상 dfs에서 setrecursionlimit 주의

import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(graph, start, visited):
    
    visited[start[0]][start[1]] = True
    
    w = len(graph[0])
    h = len(graph)
    
    dr = [-1,1,0,0,1,-1,1,-1]                         # 대각선도 포함
    dc = [0,0,-1,1,1,-1,-1,1]
    
    for i in range(8):
        move_r = start[0] + dr[i]
        move_c = start[1] + dc[i]
        
        if 0<=move_r< h and 0<=move_c<w:
            if not visited[move_r][move_c] and graph[move_r][move_c] == 1:    # 방문여부 뿐만 아니라 랜드(graph 값 = 1)에만 이동 가능
                dfs(graph, [move_r, move_c], visited)
        
answers = []        
        
while True:

    w, h = map(int, input().split())
    visited = [[False for _ in range(w)] for _ in range(h)]
    if w == 0 and h == 0:
        break
    
    m_map = []
    
    for _ in range(h):
        m_map.append(list(map(int, input().split())))
    
    count = 0
        
    for i in range(h):
        for j in range(w):
            if m_map[i][j] == 1 and not visited[i][j]:
                dfs(m_map, [i,j], visited)
                count += 1
    
    answers.append(count)            

for answer in answers:
    print(answer)

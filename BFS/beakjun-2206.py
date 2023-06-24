# 3차원 visited를 이용해 벽을 뚫은 경우와 안 뚫은 경우 2 판을 이용해서 한다.
# bfs는 최단 거리로 움직이니까 특정 지점이 같은 경로를 지나 가는 것을 고려하지 않고 먼저 가는 것이 최단 경로이다.
# 메모리 초과를 경험했는데 이유는 벽이 아닌 경우에 큐에 중복 지점을 계속 추가하도록 잘못 설계하였다. (주석 참고)

import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
my_d = deque([[0,0,0]])

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(graph):
    
    
    
    while my_d:
        
        now_r, now_c, wall = my_d.popleft()
        
        if now_r == n-1 and now_c == m-1:
            
            return visited[now_r][now_c][wall]
        
        
        
        
        
        
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

        
            
            
            if 0 <= next_r < n and 0 <= next_c < m:
                
                if graph[next_r][next_c] == 1 and wall == 0 :
                    visited[next_r][next_c][1] = visited[now_r][now_c][0] + 1
                    my_d.append([next_r, next_c, 1])
                
                elif graph[next_r][next_c] == 0 and visited[next_r][next_c][wall] == 0 :     # visited의 wall 부분에 벽이 아니라고 생각해 0으로 했었는데,
                                                                                            # 저것은 현재 벽을 뚫은 경우의 경로라면 계속 걸리기 때문에 
                                                                                            # 밑에 visited는 wall가 1인 경우만 계속 바꿔주므로 계속 큐에 추가되는 문제 발생(메모리초과)
                    visited[next_r][next_c][wall] = visited[now_r][now_c][wall] + 1
                    my_d.append([next_r, next_c, wall])
                    
                    
                           
    return -1
        
        
        
                    
                
print(bfs(graph))

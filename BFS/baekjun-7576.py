# 시간 초과 문제 발생, 테스트 케이스에 대해서는 정확함  ( 2023-05-02 )

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())   # m, n의 최대는 1,000  

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, start, visited):
    
    my_d = deque([start])
    visited[start[0]][start[1]] = True
    
    while my_d:
        
        now = my_d.popleft()
        
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nr = now[0] + dx[i]
            nc = now[1] + dy[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 0 and not visited[nr][nc]:
                    my_d.append([nr, nc])
                    visited[nr][nc] = True
                    graph[nr][nc] =  graph[now[0]][now[1]]+1
                elif graph[nr][nc] >= 2 and not visited[nr][nc]:
                    my_d.append([nr, nc])
                    visited[nr][nc] = True
                    graph[nr][nc] = min(graph[nr][nc], graph[now[0]][now[1]] + 1)
                    
                    
starts = []

for i in range(n):
    for j in range(m):
        
        if graph[i][j] == 1:
            starts.append([i, j])
            
for start in starts:
    visited = [[False for _ in range(m)] for _ in range(n)]
    bfs(graph, start, visited)

answer = 0
not_do = False
    
for i in range(n):
    for j in range(m):
        a = graph[i][j]
        if a == 0 :
            not_do = True
            
        answer = max(a, answer)


if not_do:
    print(-1)
else:
    print(answer-1)

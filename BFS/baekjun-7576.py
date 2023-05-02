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


# bfs 시간 복잡도 O(V+E)에 대해 그래프의 모든 점에 대해 시행해서 O(V(V+E)) 심지어 여기서 E의 갯수도 V에 비례해서 시간 초과가 났던것이다
# 익은 토마토에 대해 여러번 bfs를 하는 것이 아니라 처음부터 익은 토마토를 큐에 모두 넣는 방법으로 해결한다.

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())   

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph):
    
    n = len(graph)
    m = len(graph[0])
    
    my_d = deque()
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                my_d.append([i,j])
                
    while my_d:
        
        now = my_d.popleft()
        
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        
        for i in range(4):
            next_r = now[0] + dr[i]
            next_c = now[1] + dc[i]
            
            if 0 <= next_r < n and 0 <= next_c < m:
                if graph[next_r][next_c] == 0:
                    graph[next_r][next_c] = graph[now[0]][now[1]] + 1
                    my_d.append([next_r, next_c])
                elif graph[next_r][next_c] >= 1:
                    if graph[next_r][next_c] > graph[now[0]][now[1]] + 1:
                        graph[next_r][next_c] = graph[now[0]][now[1]] + 1
                        my_d.append([next_r, next_c])

bfs(graph)


answer = 0
done = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            done = False
        answer = max(answer, graph[i][j])
if done:            
    print(answer-1)
else:
    print(-1)

# 여러 포인트에서 동시에 bfs를 하는 방법은 처음에 큐에 넣어주는 것이다.

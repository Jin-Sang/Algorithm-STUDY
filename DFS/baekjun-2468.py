# dfs할 때 항상 setrecursionlimit 해주기
# 항상 경계값 테스트하기 
# 비가 안오는 경우 0을 생각안해서 틀림

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


n = int(input())


graph = [list(map(int, input().split())) for _ in range(n)]   
                
     
rain = [0]

for i in range(n):
    for j in range(n):
        if not graph[i][j] in rain:
            rain.append(graph[i][j])

rain = set(rain)
            
def dfs(graph, start, visited, ra):
    
    visited[start[0]][start[1]] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for i in range(4):
        nr = start[0] + dr[i]
        nc = start[1] + dc[i]
        
        if 0<=nr<n and 0<=nc<n:
            if not visited[nr][nc] and graph[nr][nc] > ra:
                dfs(graph, [nr,nc], visited, ra)

answers = []
                
for ra in rain:
    answer = 0
    visited = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > ra:
                dfs(graph, [i,j], visited, ra)
                answer += 1
    
    answers.append(answer)

print(max(answers))  

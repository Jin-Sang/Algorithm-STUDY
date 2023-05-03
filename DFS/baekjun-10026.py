import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())

graph = []
rg_graph = []
for _ in range(n):
    row = input().strip()
    graph.append(row)
    rg_graph.append(row.replace("G", "R"))
    
def dfs(graph, start, visited):
    
    n = len(graph)
    
    visited[start[0]][start[1]] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for i in range(4):
        next_r = start[0] + dr[i]
        next_c = start[1] + dc[i]
        
        if 0<=next_r<n and 0<=next_c<n :
           if (graph[start[0]][start[1]] == graph[next_r][next_c]) and (not visited[next_r][next_c]):    
                dfs(graph, [next_r,next_c], visited)

visited = [[False for _ in range(n)] for _ in range(n)]

count = 0

for i in range(n):
    for j in range(n):        
        if not visited[i][j]:
            dfs(graph, [i,j], visited)
            count += 1
        

print(count)             

visited = [[False for _ in range(n)] for _ in range(n)]

count = 0

for i in range(n):
    for j in range(n):        
        if not visited[i][j]:
            dfs(rg_graph, [i,j], visited)
            count += 1
print(count)

# 항상 [row축][column축] 순서 신경 쓰자
# visited 검사하는 에서 반대로 써서 무한 루프 돌았음. 

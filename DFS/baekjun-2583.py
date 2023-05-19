# 문제가 요구하는 출력 양식 지키기. 이 문제는 첫 줄에 몇 개 영역인지 출력하라 했음
# 꼭꼭 dfs 할 때 setrecursionlimit 0 5개 100000
# 항상 그래프 가로 세로 뭔지 파악!


import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

m,n,k = map(int, input().split())  # n 가로, m 세로

graph = [[1 for _ in range(n)]for _ in range(m)]

for _ in range(k):
    c1,r1,c2,r2 = map(int, input().split())    
    for i in range(m-r2, m-r1):
        for j in range(c1, c2):
            graph[i][j] = 0
           
def dfs(graph, start):

    graph[start[0]][start[1]] = 0
    global spac
    spac += 1
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
   
    for i in range(4):
        nr = start[0] + dr[i]
        nc = start[1] + dc[i]
       
        if 0<=nr<m and 0<=nc<n:
          if graph[nr][nc] == 1:
              
            dfs(graph, [nr, nc])
            
answer = []            

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            spac = 0
            dfs(graph, [i,j])
            answer.append(spac)

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=" ")

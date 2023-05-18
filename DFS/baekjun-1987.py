# 시간 초과 왜 나는지 아직 모르고 pypy로만 통과다..

# dfs bfs는 노드를 기본적으로 한번씩만 방문한다..
# in 보다 alphabet 26 길이 리스트를 만들어서 하는게 더 빠르다
# dfs마다 길이를 리스트에 append 해주고 마지막에 max하는 것보다 매번 길이를 비교해서 하나의 값을 갱신하는게 빠르다. 

# 즉, in은 느리다.
# dfs마다 append해주는 건 느리다.


import sys
import copy

sys.setrecursionlimit(10000)

input = sys.stdin.readline

r, c = map(int, input().split())

graph =[list(input().strip()) for _ in range(r)]

alph = [0] * 26                    # 시간 단축 point 이유 모름..

answer = 0

def dfs(start, cnt):
    
    global answer                          # 요렇게 해주는거 
    answer = max(answer, cnt)              # 시간 단축 point 왜 인줄은 모름..
    alph[ord(graph[start[0]][start[1]])-65] = 1
    
    
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    
    
    
    for i in range(4):
        nr = start[0] + dr[i]
        nc = start[1] + dc[i]
        
        if 0<=nr<r and 0<=nc<c:
            if alph[ord(graph[nr][nc])-65] == 0:
                
                dfs([nr, nc], cnt+1)
                
                alph[ord(graph[nr][nc])-65] = 0
            
            

dfs([0, 0],1)

print(answer)

# 입력 범위가 짧다면 모든 경우를 combinations로 해볼 생각하자. 항상 입력범위 먼저 체크 사용할 수 있는 알고리즘 체크

# 헷갈림...
# 전역 변수와 지역 변수 학습했다. 
# 전역 변수는 함수 안에서도 사용가능하다. global을 쓰면 함수 안의 변수를 전역 변수로 쓰는거라 함수 끝나도 안 사라짐.
# 리스트는 함수 안에서 바뀐 것이 밖에도 적용되고, int는 안된다.
# 함수의 인자는 인자를 바꿔서 사용 할거라면 필요하고, 만약 인자가 하나만 쓸거라면 필요없이 전역변수를 함수 내에서 사용하면된다.


import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]       

oriq = deque()
s = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            oriq.append([i,j])
        if lab[i][j] == 0:
            s.append([i,j])

answers = []
            
for t in combinations(s, 3):
    
    tmp = copy.deepcopy(lab)
    q = copy.deepcopy(oriq)
    for i in range(3):
        tmp[t[i][0]][t[i][1]] = 1
    
    while q:
        
        now = q.popleft()
        
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
    
            if 0<=nr< n and 0<=nc<m:
                if tmp[nr][nc] == 0:
                    q.append([nr, nc])
                    tmp[nr][nc] = 2 
    
    answer = 0
                    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                answer += 1
                
    answers.append(answer)


print(max(answers))  

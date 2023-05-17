# 인덱스 꼼꼼히 순서랑 범위 살피기
# bfs에서 popleft와 append로 입구와 출구 다르게 하는거 잊지말기
# 문제에서 출력하는 조건 신경 쓰기

# 갑자기 구글 코랩 왜 input = sys.stdin.readline 안된다..

import sys
from collections import deque

m, n, h = map(int, input().split())  # 가로, 세로, 높이

boxes = []

for _ in range(h):

  box = [list(map(int, input().split())) for _ in range(n)]

  boxes.append(box)

done = []

no_do = True

for i in range(h):
  for j in range(n):
    for k in range(m):

      if boxes[i][j][k] == 1:
        done.append([i,j,k, 0])
      elif boxes[i][j][k] == 0:
        no_do = False

def bfs(boxes, starts, visited):

  h = len(boxes)
  n = len(boxes[0])
  m = len(boxes[0][0])

  my_d = deque(starts)

  for start in starts:  
    visited[start[0]][start[1]][start[2]] = True

  answer = 0

  while my_d:

    now = my_d.popleft()

    dh = [0,0,0,0,-1,1]
    dn = [0,0,-1,1,0,0]
    dm = [-1,1,0,0,0,0]

    for i in range(6):

      nh = now[0] + dh[i]
      nn = now[1] + dn[i]
      nm = now[2] + dm[i]
      nd = now[3] + 1

      if 0<=nh<h and 0<=nn<n and 0<=nm<m:
        if not visited[nh][nn][nm] and boxes[nh][nn][nm] == 0:
          visited[nh][nn][nm] = True
          boxes[nh][nn][nm] = 1
          my_d.append([nh, nn, nm, nd])
          answer = max(answer, nd)
    
  return answer

visited = [[[False for _ in range(m)] for _ in range(n)]for _ in range(h)] 

answer = bfs(boxes, done, visited)

impo = False

for i in range(h):
  for j in range(n):
    for k in range(m):

      if boxes[i][j][k] == 0:
        impo = True
if no_do:
  print(0)
elif impo:
  print(-1)
else :
  print(answer)

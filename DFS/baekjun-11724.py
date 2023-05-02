import sys
sys.setrecursionlimit(15000)

input = sys.stdin.readline               # python3의 시간초과는 input에 의해 일어나는 경우가 많다.
                                        

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    dep, arr = map(int, input().split())
    graph[dep].append(arr)
    graph[arr].append(dep)

visited = [False for _ in range(n+1)]

def dfs(graph, start, visited):
    
    visited[start] = True

    for n in graph[start]:
        if not visited[n]:
            dfs(graph, n, visited)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)


# python3의 시간 초과는 입력값의 갯수가 많은 경우 input()에 의해 발생하는 경우가 많다
# 이 경우도 m에 의해 간선의 입력수가 결정되는데 m은 최대 10000*(10000-1)/2 이므로 매우 크다.
# input() 대신 sys.stdin.readline을 사용하던가 pypy3를 이용하여 인터프리트한다.

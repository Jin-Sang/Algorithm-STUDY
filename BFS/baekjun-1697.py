# BFS 문제인줄 알고 풀었는데, DP 문제 같아서 풀어봤는데 풀렸다.
# 여기서 DP를 오름차순으로 채워나갈 때 DP는 밑에서가 아니라 바로 윗칸에서 -1로 올수도 있다는 것을 주의해야한다.
# DP 문제를 풀 때 어디서 마지막으로 오는지 항상 경우 잘 확인하기
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if k > n:
    dp = [0] * (k+1)
    
    for i in range(n):
        dp[i] = n-i
    
    dp[n] = 0
        
    for j in range(n+1, k+1):
        if j % 2 == 0:
            dp[j] = min(dp[j-1], dp[int(j/2)]) + 1
        else:
             
            dp[j] = min(dp[j-1], dp[int((j+1)/2)]+1) + 1   # 홀수의 경우 j+1에서 -1해서 오는 경우가 있다 이때, j+1이 j에서 +1로 되는 경우는 최솟값이 될수 없기에 
                                                           # *2로 만들어졌다고 경우의 수만 고려한다.
            
    print(dp[k])            


elif k == n:
    print(0)
    
else:
    print(n-k)
    
    
# bfs로도 풀어보자 왜 bfs인가?

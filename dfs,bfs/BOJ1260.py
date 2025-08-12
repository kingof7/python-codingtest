# BOJ1260

import sys
sys.stdin = open("input.txt", "r")

def dfs(c):
    v[c] = 1 # 방문 처리
    ans_dfs.append(c) # 방문 노드 추가
    
    for n in adj[c]:
        if not v[n]:    # 방문하지 않은 노드인 경우
            dfs(n)

def bfs(s):
    q = []              # 필요한 q, v[], 변수 생성
    q.append(s)         # q에 초기데이터(들) 삽입
    ans_bfs.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:    # 방문하지 않은 노드 => 큐에 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


# N = 정점의 갯수, M = 간선의 갯수, V = 정점의 번호
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# [1] 오름차순 정렬하기
for i in range(1, N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
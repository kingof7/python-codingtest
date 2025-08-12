import sys
sys.stdin = open("input.txt", "r")

def dfs(c):
    v[c] = 1
    ans_dfs.append(c)

    for n in adj[c]:
        if v[n] == 0:
            dfs(n)

def bfs(s):
    q = []
    q.append(s)
    v[s] = 1
    ans_bfs.append(s)
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = 1
                ans_bfs.append(n)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# for _ in adj:
#     _.sort()

for i in range(1, N+1):
    adj[i].sort()

ans_dfs = []
v = [0]*(N+1)
dfs(V)

ans_bfs = []
v = [0]*(N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
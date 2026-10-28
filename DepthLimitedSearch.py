graph={
    0:[1,2],
    1:[0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

visited= set()

def dls(node,limit,snode):
    if limit<0:
        return

    visited.add(node)
    print(node,end=" ")

    
    if limit ==0:
        return 
    if node== snode:
        print("node Founded")
        return
    for n in graph[node]:
        if n not in visited:
            dls(n,limit-1,snode)

limit=int(input("Enter limit"))
snode=2
dls(0,limit,snode)
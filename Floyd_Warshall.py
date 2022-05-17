INF=10000000000000

def floyd_warshall(busTransition,trainTransition,transferTransition,quickest,vertexCount):
    for k in range(vertexCount):
        for i in range(vertexCount):
            for j in range( vertexCount):
                #print(busTransition[k][i])
                busTransition[i][j]=min(busTransition[i][j], busTransition[i][k]+busTransition[k][j], trainTransition[i][k]+busTransition[k][j]+transferTransition[k])
                trainTransition[i][j]=min(trainTransition[i][j], trainTransition[i][k]+trainTransition[k][j], busTransition[i][k]+trainTransition[k][j]+ transferTransition[k])
                quickest[i][j]=min(busTransition[i][j], trainTransition[i][j])

def printResult(mat,vertexCount):
    for i in range(vertexCount):
        for j in range(vertexCount):
            print(mat[i][j], end=" ")
        print()



"""
busTransition=[
    [0,23,8,15,2],\
    [21,0,5,2,1],\
    [12,32,0,25,23],\
    [0,3,8,0,123],\
    [12,2,12,1,0],]
"""
busTransition=[
    [0,100,INF],\
    [100,0,120],\
    [INF,120,0],]

trainTransition=[
    [0,INF,180],\
    [INF,0,INF],\
    [180,INF,0],]

quickest=[
    [0, INF, INF],\
    [INF, 0, INF],\
    [INF, INF, 0],\
]

transferTransition=[30, INF, 10]  

vertexCount=len(busTransition)
floyd_warshall(busTransition,trainTransition,transferTransition, quickest, vertexCount)
printResult(quickest, vertexCount)
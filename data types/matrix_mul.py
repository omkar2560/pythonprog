l1=[[4,2,5,1],[1,3,5,2]]
l2=[[5,7,4,6],[4,2,3,1]]
c=[[0,0,0,0],[0,0,0,0]]

for i in range (len(l1)):

    for j in range(len (l2[0])):
        for k in range(len(l2)):
            c[i][k]+=l1[i][k]*l2[k][j]
        print c
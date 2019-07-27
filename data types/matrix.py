l1=[[4,5,2,1],[8,4,2,3]]
l2=[[2,3,4,1],[5,6,2,7]]
c=[]
for i in range(len (l1)):
    print l1[i]
    c.insert(i,[])
    for j in range(len(l1[i])):

        print l1[i][j]
        c[i].insert(j,(l1[i][j]+l2[i][j]))

print c
#
# c[i],[j]=l1[i][j]+l2[i][j]
# print(c[i][j])
a=[[8,3,4],
   [1,5,9],
   [6,7,2]]
row1=0
row2=0
row3=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            row1=row1+a[i][j]
        elif i==1:
            row2=row2+a[i][j]
        else:
            row3=row3+a[i][j]
        j+=1
    i+=1
if row1==row2==row3:
    print("row1:",row1)
    print("row2:",row2)
    print("row3:",row3)
else:
    print("not equal",row1,row2,row3)
column1=0
column2=0
column3=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if j==0:
            column1=column1+a[i][j]
        elif j==1:
            column2=column2+a[i][j]
        else:
            column3=column3+a[i][j]
        j+=1
    i+=1
if column1==column2==column3:
    f=0
else:
    f=1
print("column1:",column1)
print("column2:",column2)
print("column3:",column3)
diagonol1=0
diagonol2=0
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==j:
            diagonol1=diagonol1+a[i][j]
        if i==3-1:
            diagonol2=diagonol2+a[i][j]
        j+=1
    i+=1
if diagonol1==diagonol2:
    f=0
else:
    f=1
print("diagonol1:",diagonol1)
print("diagonol2:",diagonol2)
if f==0:
    print("it is a magic square")
else:
    print("it is a not magic square")                                





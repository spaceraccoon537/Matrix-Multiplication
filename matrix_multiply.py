def multiply(a,b):
    rowa=len(a)
    cola=len(a[0])
    rowb=len(b)
    colb=len(b[0])
    if(cola!=rowb):
        print("the matrices cannot be multiplied")
    else:
        prod=[[0]*rowa for i in range(colb)]
        for i in range(0,rowa):
            for j in range(0,colb):
                prod[i][j]=0
                for k in range(0,rowb):
                    prod[i][k]=prod[i][k]+a[i][k]*b[k][j]
    for i in range(0,rowa):
        for j in range(0,colb):
            print(prod[i][j])
x=[
    [1,2],
    [4,5],
    ];
y=[
    [1,0],
    [0,1],
    ];
multiply(x,y)

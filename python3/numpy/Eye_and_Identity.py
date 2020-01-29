import numpy
n,m = list(map(int,input().split()))
print(numpy.eye(n,m,k=0))

#-- OR

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

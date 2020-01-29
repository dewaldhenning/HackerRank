import numpy
N,M, P= list(map(int, input().split()))
A= numpy.array([list(map(int, input().split()))  for i in range(N)] )
B= numpy.array([list(map(int, input().split()))  for i in range(M)] )
print (numpy.concatenate((A,B),axis =0))

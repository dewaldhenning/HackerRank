// Code for Python 2
import numpy

N, M = map(int,raw_input().split())

my_array = numpy.array( [map(int, raw_input().split()) for i in range(N)] )
print numpy.transpose(my_array)
print my_array.flatten()

//Code for Pyton 3

import numpy

N, M = map(int,input().split())

my_array = numpy.array( [map(int, input().split()) for i in range(N)])

print (numpy.transpose(my_array))
print (my_array.flatten())

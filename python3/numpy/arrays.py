import numpy

def arrays(arr):
    x = numpy.array(arr)
    arr = x.astype(numpy.float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

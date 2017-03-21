from theano import *
import theano.tensor as T

if __name__ != '__main__':
    raise ImportError("%s should not be imported"%__file__)

'''numpy hello world'''
_array = numpy.asarray([[0.,1],[1,1],[2,1]])
print _array
print _array.shape
'''' Don't know why 3x2 * 1*2 -> 1*1 '''
print _array[2,0]

''' Algebra hello world '''
import numpy
#dscalar is double type scalar (array)
x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x,y], z)
print f(2,3)
print numpy.allclose(f(16.3, 12.1), 28.4, 28.40000)
print x.type is T.dscalar
print pp(z)
#eval s a quick way performs like function
print numpy.allclose(z.eval({x:16.300, y:12.100}), 28.4)

x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)
print f([[0,1], [1,2]], [[0,0],[0,1]])

a = T.vector()
out = a + a**10
f = function([a], out)
print f([0,1,2])
a = T.vector()
b = T.vector()
out = a**2 + b**2 + 2*a*b
print out.eval({a:[0,1,2],b:[1,1,1]})

a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff**2
f = function([a, b], [diff, abs_diff, diff_squared])
_result = f([[1, 1], [1, 1]], [[0, 1], [2, 3]])
print _result
_result_a, _result_b, _result_c = _result
print _result_a
print _result_b
print _result_c

'''TODO http://deeplearning.net/software/theano/tutorial/examples.html#setting-a-default-value-for-an-argument '''


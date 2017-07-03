# from numpy import *
import numpy as np 
from numpy import linalg as la
from scipy.linalg import hilbert
import scipy.linalg
import pprint

# http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.set_printoptions.html
np.set_printoptions(precision=16)

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# print a
#
# # The condition number of x is defined as the norm of x times the norm of the inverse of x [R37];
# # the norm can be the usual L2-norm (root-of-sum-of-squares) or one of a number of other matrix norms.
# # the manual: http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.linalg.cond.html
#
# # a problem with a low condition number is said to "well conditioned".
# # a problem with a high condition number is said to "ill conditioned".
#
# # linalg.inv(a) is the function for computing the inverse.
#
# # print '{0:.16e}'.format(positive_root)
#
# pprint.pprint(la.inv(a))
# print(la.inv(a))
# print(la.cond(a))
#
# # print '{0:.16e}'.format(la.inv(a))
# print '{0:.16e}'.format(la.cond(a))
#
# la.inv(a)
#
# b = la.inv(a)
#
# c = np.dot(a,b)
#
# print "This is c:"
# print c
#
# # clearly c is not the identity matrix so a IS singular.

# ***** Problem #3 *****
#
# A = hilbert(4)
#
# print A
#
# z = np.ones(4)
#
# print z
#
# b = np.dot(A,z)
#
# print(b)
#
# # a\b in MATLAB is equivalent to linalg.solve(a,b) in numpy
#
# print "This is the solution.", la.solve(A, b)
#
# for i in (4, 8, 12):
#
#     A = hilbert(i)
#     print A
#
#     z = np.ones(i)
#     print z
#
#     b = np.dot(A,z)
#     print b
#
#     x_hat = la.solve(A, b)
#     print "This is the solution", la.solve(A, b)
#
#     # condition_number = la.cond(A)
#     print 'This is the condition number:{0:.16e}'.format(la.cond(A))
#
#     numerator_error = np.subtract(x_hat, z)
#     numerator_error = la.norm(numerator_error)
#
#     denominator_error = la.norm(z)
#
#     relative_error = numerator_error / denominator_error
#
#     relative_error = np.divide(numerator_error, denominator_error)
#
#     print"This is the relative error: {0}".format(relative_error)
#
#     # now we want to calculate the relative residual.
#
#     c = np.dot(A, x_hat)
#
#     r = np.subtract(b, c)
#
#     # the norm should be a scalar so we should be able to just divide.
#     norm_r = la.norm(r)
#
#     norm_b = la.norm(b)
#
#     residual = np.divide(norm_r, norm_b)
#
#     print "This is the residual: {0}".format(residual)



# *********************** this is problem 4 **********************
#
# A = np.random.rand(12, 12)
# print A
#
# z = np.ones(12)
# print z
#
# b = np.dot(A, z)
# print b
#
# x_hat = la.solve(A, b)
# print "This is the solution", la.solve(A, b)
#
# # condition_number = la.cond(A)
# print 'This is the condition number:{0:.16e}'.format(la.cond(A))
#
# numerator_error = np.subtract(x_hat, z)
# numerator_error = la.norm(numerator_error)
#
# denominator_error = la.norm(z)
#
# relative_error = numerator_error / denominator_error
#
# relative_error = np.divide(numerator_error, denominator_error)
#
# print"This is the relative error: {0}".format(relative_error)
#
# # now we want to calculate the relative residual.
#
# c = np.dot(A, x_hat)
#
# r = np.subtract(b, c)
#
# # the norm should be a scalar so we should be able to just divide.
# norm_r = la.norm(r)
#
# norm_b = la.norm(b)
#
# residual = np.divide(norm_r, norm_b)
#
# print "This is the residual: {0}".format(residual)


# ****************** here is problem 5 **********************************
#
# A = hilbert(12)
#
# print A
#
# print 'This is the condition number:{0:.16e}'.format(la.cond(A))
#
#
# P, L, U = scipy.linalg.lu(A)
# print"this is the U:"
# pprint.pprint(U)
#
#
# print(U[:, 11])


# *********** here is problem 6 ***********************************

import numpy as np
from scipy import sparse

nx, ny = 3, 3
N  = nx*ny
main_diag = np.ones(N)*-4.0
side_diag = np.ones(N-1)
side_diag[np.arange(1,N)%nx==0] = 0
up_down_diag = np.ones(N-3)
diagonals = [main_diag,side_diag,side_diag,up_down_diag,up_down_diag]
laplacian = sparse.diags(diagonals, [0, -1, 1,nx,-nx], format="csr")
print laplacian.toarray()
# assignment 4 for Watkins

# from numpy import *
import numpy as np
from scipy.interpolate import lagrange

# **************** problem #1 **********************
# Find the polynomial of degree 2 that interpolates these points

# x = np.array([.8, .9, 1.0])
# f = np.array([.696707, .621610, .540302])
#
# polynomial_2 = lagrange(x, f)
#
# a = polynomial_2(0.85)
#
# print a
#
# print polynomial_2

# ******** problem #4 ***********


def f(x):
    return 3.0*np.power(x, 2) - 6.0*x + 5

x = np.array([-3, -2, -1, 0, 1, 2, 3, 4])
y = np.array([f(-3), f(-2), f(-1), f(0), f(1), f(2), f(3), f(4)])

print y 

polynomial_2 = lagrange(x, y)

print polynomial_2

#
# # **************** problem #2 *************************
# from pylab import *
#
#
# def divided_difference( x, y ):
#     """Compute interpolated polynomial coefficients using divided differences.
#
#     USAGE:
#         a = divided_difference( x, y )
#
#     INPUT:
#         x      - integer or float array of x coordinates
#         y      - integer or float array of y coordiantes
#
#     OUTPUT:
#         float array - array of interpolating polynomial coefficients
#
#     NOTES:
#         This function computes the divided differences that can be used to
#         construct an interpolating polynomial for the given set of data.
#
#         This function accepts two vectors and returns a vector whose elements
#         are the divided difference values.
#
#         The value of the polynomial p (degree will be at most n) evaluated at
#         r is given by:
#
#             s = a[n]
#             for i in range( n, 0, -1 ):
#                 s = s * ( r - x[i-1] ) + a[i-1]
#
#         using the array a returned by this function.
#
#     AUTHOR:
#         Jonathan R. Senning <jonathan.senning@gordon.edu>
#         Gordon College
#         February 7, 1999
#         Converted to Python May 2008
#     """
#
#     nx = shape( x )
#     ny = shape( y )
#
#     if max( nx ) != max( ny ):
#         print 'both input variables must be vectors of the same length'
#         return
#     elif len( nx ) != 1 or len( ny ) != 1:
#         print 'both input variables must be vectors, not matrices'
#         return
#
#     n = max( nx ) - 1
#     a = y.copy()
#
#     for i in xrange( 1, n + 1 ):
#         for j in xrange( n, i - 1 , -1 ):
#             a[j] = float( a[j] - a[j-1] ) / float( x[j] - x[j-i] )
#
#     return a
#
#
# def evaluate(r, x, a):
#     """Evaluate divided difference polynomial at r
#
#     USAGE:
#         a = evaluate( r, x, a )
#
#     INPUT:
#         r      - integer or float scalar or numpy array of evaluation points
#         x      - integer or float array of interpolation point x coordinates
#         a      - coefficient array returned by divided_difference()
#
#     OUTPUT:
#         float array - float scalar or array of y-values corresponding to r
#
#     """
#
#     n = len( a ) - 1
#     s = a[n]
#     for i in xrange( n - 1, -1, -1 ):
#         s = s * ( r - x[i] ) + a[i]
#     return s
#
# b = divided_difference(x, f)
#
# c = evaluate(x, f, b)
#
# print c
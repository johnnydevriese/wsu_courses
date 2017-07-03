# we are going to solve -u''(x) + 16*u(x)^p = 0
# intial condition of u(0) = 0 and u(1) = 2
# using Newton's method with an initial guess of 2x
# build a mesh on the domain of [0,1]

import numpy as np
import matplotlib.pyplot as plt

left_point = 0.0
right_endpoint = 1.0

p = 1.0  # the power on the u(x) term, the problem is nonlinear when p != 1
n = 4.0  # number of sub intervals
h = 1.0 / n  # sub interval length

x = np.arange(left_point, right_endpoint + h, h)

u = 2.0 * x
print "This is u", u
# when n = 4, then u = [ 0.   0.5  1.   1.5  2. ]

# now we need to create our Jacobian matrix.
# recall that Python is 0 based indexing and MATLAB has 1 based indexing!!!

for i in np.arange(0, 1):

    # Jacobian has -1 on both sides of the main diagonal
    diagonals = -1.0*np.ones(n)

    # storage space
    main_diagonal = np.zeros(len(x))

    for j in np.arange(len(x)):
        # print x[i]
        main_diagonal[j] = 2.0 + 16.0 * p * np.power(h, 2.0) * np.power(u[j], p - 1.0)
        # print main_diagonal

    jacobian = np.diag(diagonals, -1) + np.diag(diagonals, 1) + np.diag(main_diagonal)

    print jacobian

    # but I think we also need an F(u) vector
    # making space to put this vector.
    F = np.zeros(len(x))

    for k in np.arange(0, 3):
        # print u[i]
        F[k] = -u[k] + (2.0 * u[k+1]) - u[k+2] + (16.0 * (h**2.0) * u[k+1]**p)


    # now we want to solve the system for delta u
    delta_u = np.linalg.solve(jacobian, F)

    print "this is u", u
    print "this is delta u", delta_u

    u += delta_u
    print "this is u", u

    if np.linalg.norm(delta_u) < 10e-15:
        break


def hyperbolic_sin(x):
    return 2.0 * np.sinh(4.0*x) / np.sinh(4)


# x = np.arange(0, 1 + h, h)
y = hyperbolic_sin(x)
# print "this is y", y
plt.plot(x, u)
plt.plot(x, y)
# plt.show()


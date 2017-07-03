# we are going to solve -u''(x) + 16*u(x)^p = 0
# initial condition of u(0) = 0 and u(1) = 2
# using Newton's method with an initial guess of 2x
# build a mesh on the domain of [0,1]

import numpy as np
import matplotlib.pyplot as plt

left_point = 0.0
right_endpoint = 1.0

p = 1.0  # the power on the u(x) term, the problem is nonlinear when p != 1
n = 3.0  # number of sub intervals
h = 1.0 / (n + 1.0)  # sub interval length

x = np.arange(left_point + h, right_endpoint, h)

u = 2.0 * x
print "this is u", u

for i in np.arange(0, 1):

    # Jacobian has -1 on both sides of the main diagonal
    diagonals = -1.0*np.ones(n-1)

    main_diagonal = np.zeros(len(x))

    for j in np.arange(n):
        # print x[i]
        main_diagonal[j] = 2.0 + 16.0 * p * np.power(h, 2.0) * np.power(u[j], p - 1.0)
        # print main_diagonal

    jacobian = np.diag(diagonals, -1) + np.diag(diagonals, 1) + np.diag(main_diagonal)
    print jacobian

    # but I think we also need an F(u) vector
    # making space to put this vector.
    F = np.zeros(n)


    for k in np.arange(0, n):
        print u[i]
        F[k] = -u[k] + (2.0 * u[k+1]) - u[k+2] + (16.0 * (h**2.0) * u[k+1]**p)

    # for k in np.arange(0, n):
    #     if k == 0:
    #         F[k] = u[k+1] - 2.0*u[k] + left_point + (16.0 * (h**2.0) * u[k]**p)
    #     elif k == n-1:
    #         F[k] = right_endpoint - 2.0*u[k] - u[k-1] + (16.0 * (h**2.0) * u[k]**p)
    #     else:
    #         F[k] = u[k+1] - 2.0*u[k] + u[k-1] + (16.0 * (h**2.0) * (u[k]**p))

    print 'This is F', F

    # now we want to solve the system for delta u
    delta_u = np.linalg.solve(jacobian, F)

    print "this is delta u", delta_u

    u += delta_u

    print "this is u.", u

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
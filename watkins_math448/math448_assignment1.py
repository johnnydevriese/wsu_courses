from math import *


# just testing out printing our 16 decimals places
# a = 2.0
#
# b = 3.0
#
# c = float( a * b )
#
# print '{0:.16f}'.format(c)


def quadratic_formula(a, b, c):

    # initialize an array to store the roots.
    roots = []

    positive_root = float((-(b/2.0) + sqrt((b/2.0)**2 - (a * c))) / a)

    negative_root = float((-(b/2.0) - sqrt((b/2.0)**2 - (a * c))) / a)

    print"quadratic equation yields:"
    print '{0:.16e}'.format(positive_root)
    print '{0:.16e}'.format(negative_root)

    roots.append(positive_root)
    roots.append(negative_root)

    print roots

    return roots


def muller_method(a, b, c):

    # according to the internet this is the fastest way to initialize an empty list
    roots = []

    positive_root = float(c / (-(b/2.0) + sqrt((b/2.0)**2 - a * c)))

    negative_root = float(c / (-(b/2.0) - sqrt((b/2.0)**2 - a * c)))

    print "Muller method yields:"
    print '{0:.16e}'.format(positive_root)
    print '{0:.16e}'.format(negative_root)

    roots.append(positive_root)
    roots.append(negative_root)

    print roots

    return roots


# the solution for 2x^2 + 5x - 25 = 0 should be -5 and 5/2
# quadratic_formula(2, 5, -25)
#
# muller_method(2, 5, -25)
#
# #problem 2 is where we compute the roots of the polynomial: 0.0256x^2 - 78x + 0.0142 = 0
#
# quadratic_formula(0.0256, -78.0, 0.0142)
#
# muller_method(0.0256, -78.0, 0.0142)


# quadratic_formula(0.002, -42000.0, 0.001)
#
# muller_method(0.002, -42000.0, 0.001)


# quadratic_formula(0.000256, -7800.0, 0.000142)

quadratic_formula(0.00042, -9800.0, 0.00035)

muller_method(0.00042, -9800.0, 0.00035)
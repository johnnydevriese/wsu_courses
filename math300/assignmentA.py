from pylab import *
import string
import numpy as np
from numpy.polynomial.polynomial import polyval
from strings import *


def p(left_limit, right_limit):
    # get user input, feel incredibly reckless and don't check user input at all.
    # surname = raw_input("What is your last name?")

    # convert to lowercase.
    # surname = surname.lower()

    surname = 'minor'

    # print surname

    # intializing an array to store the numbers.
    numbers = np.zeros(len(surname))

    # converting from the ASCII values to make 'a' = 1
    for i in range(len(surname)):
        numbers[i] = ord(surname[i]) - 96.0

    # print numbers

    # subtracting 13 as part of the original problem.
    for i in range(len(numbers)):
        numbers[i] -= 13.0

    # print numbers

    for i in range(len(numbers)):
        numbers[i] = numbers[i] / 6.0
    # print numbers

    for i in range(len(numbers)):
        numbers[i] = numbers[i] / np.power(2.0, i)

    # print numbers

    # this is our polynomial function.
    def f(x):
        x = numbers[0] + numbers[1] * x + numbers[2] * np.power(x, 2) + numbers[3] * np.power(x, 3) + numbers[
                                                                                                          4] * np.power(
            x, 4)

        return x

    # reverse the array for the form of the polyint function
    # don't overwrite the numbers array so we could still use the horner form in polyval() function.
    reversed_arr = numbers[::-1]

    # print reversed_arr

    # this function will create an integral of form x^n + x^n-1 + x^n-2 + ... + a_0
    # hence why we needed to reverse the string.
    P = np.polyint(reversed_arr)

    # this gives the correct integral!
    # print(np.poly1d(P))

    # cast P as a poly1d array so that we can easily evaluate it!
    P = np.poly1d(P)

    # ~ onez = np.ones(5)
    # ~
    # ~ print onez

    # P will take a vector argument as I tested it with an array of ones.
    # analytical_integral = P(left_limit) - (right_limit)
    analytical_integral = P(right_limit) - P(left_limit)

    # print'this is the analytic integral: {}' .format( analytical_integral)

    # print P(5)

    # print(f(0))

    # a = - pi / 2.0 #left_limit
    # b = pi / 2.0 #right_limit

    # print(trapezoid(f,a,b,n))

    # print numerical_integral

    integral = np.zeros(6)

    # print(integral)

    # could do something like this and fill an array with the trapezoidal integrals.
    n = 1.0

    for i in range(6):
        n = n * 10.0
        # print n
        integral[i] = trapezoid(f, left_limit, right_limit, n)


    # ~ for i in range(len(integral)):
    # ~
    # ~ print(format(integral[i],'.12f') 	)

    # now we need to calcuate the difference.
    difference = np.zeros(6)

    for i in range(len(integral)):
        difference[i] = np.log(np.absolute(analytical_integral - integral[i]))

    # print difference

    # now make a plot
    # x = arange(0.0, 1000000.0, 1.0)

    n = 1.0

    intervals = np.zeros(6)
    for i in range(6):
        n = n * 10.0
        intervals[i] = np.log(n)
    # print intervals

    scatter(intervals, difference, color='r')
    xlim(0.0, 15.0)
    # ylim(0, -30.0)
    xlabel('Log of Number of subintervals(log(n))')
    ylabel('Log of the difference')
    title('Difference Between Analytical and Trapezoidal Rule')

    show()

    return analytical_integral


p(-pi / 2.0, pi / 2.0)

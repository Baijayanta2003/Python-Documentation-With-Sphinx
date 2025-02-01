import math
def area_of_ellipse(a, b):
    """
    Computes the area of an ellipse:

    .. math::
        A = \\pi a b

    where:
    - :math:`A` is the area,
    - :math:`a` is the semi-major axis,
    - :math:`b` is the semi-minor axis.

    :param a: The semi-major axis length.
    :param b: The semi-minor axis length.
    :return: The area of the ellipse.
    :rtype: float
    """
    return math.pi * a * b

def fibonacci(n):
    """
    Computes the nth Fibonacci number using Binet's formula:

    .. math::
        F_n = \\frac{1}{\\sqrt{5}} \\left( \\left( \\frac{1 + \\sqrt{5}}{2} \\right)^n - \\left( \\frac{1 - \\sqrt{5}}{2} \\right)^n \\right)

    where:
    - :math:`F_n` is the nth Fibonacci number.

    :param n: The index of the Fibonacci sequence.
    :return: The nth Fibonacci number.
    :rtype: int
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((1 / math.sqrt(5)) * (phi**n - psi**n))


def logistic_growth(P0, r, t, K):
    """
    Models the population growth according to the logistic growth model:

    .. math::
        P(t) = \\frac{K P_0}{P_0 + (K - P_0) e^{-rt}}

    where:
    - :math:`P(t)` is the population at time :math:`t`,
    - :math:`P_0` is the initial population,
    - :math:`r` is the growth rate,
    - :math:`K` is the carrying capacity of the environment.

    :param P0: Initial population size.
    :param r: Growth rate.
    :param t: Time at which to evaluate the population.
    :param K: Carrying capacity.
    :return: The population at time :math:`t`.
    :rtype: float
    """
    return (K * P0) / (P0 + (K - P0) * math.exp(-r * t))

def logistic_map(x0, r, n):
    """
    Simulates the logistic map: 

    .. math::
        x_{n+1} = r x_n (1 - x_n)

    where:
    - :math:`x_{n+1}` is the population at the next time step,
    - :math:`x_n` is the population at the current time step,
    - :math:`r` is the growth rate.
    
    This is often used to model chaotic systems.

    :param x0: Initial population size.
    :param r: Growth rate parameter.
    :param n: Number of iterations.
    :return: The population after n iterations.
    :rtype: float
    """
    x = x0
    for _ in range(n):
        x = r * x * (1 - x)
    return x


def pendulum_period(length, g=9.81):
    """
    Calculates the period of a simple pendulum:

    .. math::
        T = 2 \\pi \\sqrt{\\frac{l}{g}}

    where:
    - :math:`T` is the period,
    - :math:`l` is the length of the pendulum,
    - :math:`g` is the acceleration due to gravity (default value is 9.81 m/s²).

    :param length: The length of the pendulum.
    :param g: The gravitational acceleration (default is 9.81 m/s²).
    :return: The period of the pendulum.
    :rtype: float
    """
    return 2 * math.pi * math.sqrt(length / g)


def quadratic_formula(a, b, c):
    """
    Solves the quadratic equation: 

    .. math::
        ax^2 + bx + c = 0

    Using the quadratic formula:

    .. math::
        x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}

    where:
    - :math:`a`, :math:`b`, and :math:`c` are the coefficients of the quadratic equation.
    - :math:`x` is the solution to the equation.

    :param a: Coefficient of x^2.
    :param b: Coefficient of x.
    :param c: Constant term.
    :return: A tuple containing the two solutions for x.
    :rtype: tuple of floats
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real solutions
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return (x1, x2)






def sum_of_squares(n):
    """
    Computes the sum of squares of the first :math:`n` integers:

    .. math::
        S = 1^2 + 2^2 + \\cdots + n^2 = \\frac{n(n+1)(2n+1)}{6}

    where:
    - :math:`S` is the sum of squares.
    - :math:`n` is the number of terms.

    :param n: The number of terms to sum.
    :return: The sum of squares.
    :rtype: float
    """
    return n * (n + 1) * (2 * n + 1) / 6



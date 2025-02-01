def area_of_circle(radius):
    """
    Compute the area of a circle.

    The formula is given by:

    .. math:: A = \pi r^2

    where:
    - :math:`A` is the area,
    - :math:`r` is the radius.

    :param radius: The radius of the circle.
    :type radius: float
    :return: The computed area.
    :rtype: float
    """
    import math
    return math.pi * radius ** 2

def velocity(distance, time):
    """
    Computes velocity using the equation:

    .. math::

        v =\\frac{d}{t}

    Parameters
    ----------
    distance : float
        Distance traveled (:math:`d`).
    time : float
        Time taken (:math:`t`).

    Returns
    -------
    float
        Computed velocity (:math:`v`).
    """
    return distance / time


def kinetic_energy(mass, velocity):
    """
    Computes kinetic energy using the formula:

    .. math::

        KE = \\frac{1}{2} m v^2

    Args:
        mass (float): The object's mass (:math:`m`).
        velocity (float): The object's velocity (:math:`v`).

    Returns:
        float: The kinetic energy (:math:`KE`).
    """
    return 0.5 * mass * velocity ** 2



def pythagoras(a, b):
    """
    Computes the hypotenuse using the Pythagorean theorem:
     .. math::

        c^2=a^2+b^2
    
      (a+b)^2=a^2+2ab+b^2

    :param a: Side A length.
    :param b: Side B length.
    :return: Hypotenuse length.
    """
    import math
    return math.sqrt(a**2 + b**2)
def force(mass, acceleration):
    """
    Computes force using Newton's Second Law:
    .. math::
    F = m \\cdot a

    where:
    - :math:`F` is the force,
    - :math:`m` is the mass,
    - :math:`a` is the acceleration.

    :param mass: The object's mass.
    :param acceleration: The object's acceleration.
    :return: The computed force.
    """
    return mass * acceleration

def energy(mass, c):
    """
    Computes energy using Einstein's equation:

    .. math::
        E=mc^2

    where:
    - :math:`E` is energy,
    - :math:`m` is mass,
    - :math:`c`    is the speed of light.

    :param mass: The mass of the object.
    :param c: The speed of light.
    :return: The computed energy.
    """
    return mass * c**2

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle based on the provided radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Example:
        >>> calculate_area(5)
        78.53981633974483
    """
    import math
    return math.pi * radius ** 2


import math

#Constants

G = 6.67430e-11        #Gravitational Constant
M = 5.972e24           #Earth Mass
R = 6371000            #Earth Radius

def orbital_velocity(r):
    """
    Calculates circular orbial velocity.
    """
    return math.sqrt(G * M / r)


def escape_velocity(r):
    """
    Calculates escape velocity.
    """
    return math.sqrt(2 * G * M / r)


def orbital_period(r):
    """
    Calculates orbital period in seconds.
    """
    return 2 * math.pi * math.sqrt((r**3) / (G * M))


def angular_velocity(period):
    """
    Returns angular velocity in rad/s
    """
    return 2 * math.pi / period
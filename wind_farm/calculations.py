import numpy as np

"""
Source: https://www.omnicalculator.com/physics/air-density#how-to-calculate-the-air-density
"""


def get_air_pressure(alt, temp):
    """
     Calculates atmospheric pressure given the altitude and temperature
     Units:
     alt: meters
     temp: Celsius
     Returns: air pressure in hPa
    """

    p_0 = 1013.25
    g = 9.80665
    mol = 0.0289644
    r_constant = 8.31432
    kelvin = temp + 273.15

    return p_0 * np.exp((-g * mol * alt) / (r_constant * kelvin))


def get_dew_point(temp, rh):
    """
    Calculates dew point given temperature and humidity
    Units:
    temperature: Celsius
    Returns: dew point in Celsius
    """

    a = 17.62
    b = 243.12
    alpha = np.log(rh / 100) + (a * temp / (b + temp))

    return (b * alpha) / (a - alpha)


def get_air_density(alt, temp, rh, lb=False):
    """
    Calculates air density given altitude, temperature, and relative humidity
    Units:
    alt: meters
    temp: Celsius
    Optional: can return in lb/ft3 if lb = True (default: False)
    Returns: air density in kg/m3
    """

    if lb:
        converter = 16.018
    else:
        converter = 1

    # Get air pressure in Pa
    p = get_air_pressure(alt, temp) * 100

    # Calculate saturation vapor pressure given the temperature
    p1 = 6.1078 * np.power(10, (7.5 * temp) / (temp + 237.3))

    # Calculate actual vapor pressure
    pv = p1 * rh

    # subtract vapor pressure from total air pressure
    pd = p - pv

    # Constants
    r_d = 287.058  # specific gas constant for dry air
    r_v = 461.495  # specific gas constant for water vapor
    kelvin = temp + 273.15

    rho = (pd / (r_d * kelvin)) + (pv / (r_v * kelvin))

    return rho / converter

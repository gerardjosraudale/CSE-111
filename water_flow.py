# Author: Josue Raudales    
# Date: 10/14/2023
# Purpose: This module provides functions for calculating water-related parameters.
# Sources: I used the preparation content in how to use pytest, assert and approx. Also, the example test function.

def jr_water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4
"""
    Calculates the height of a column of water in a tank.

    Args:
        tower_height (float): The height of the tower.
        tank_height (float): The height of the tank walls.

    Returns:
        float: The height of the water column.
    """
def jr_pressure_gain_from_water_height(height):
    density_water = 998.2
    gravity = 9.80665
    return (density_water * gravity * height) / 1000
"""
    Calculates the pressure due to gravity on the water in an elevated tank.

    Args:
        height (float): The height of the water column.

    Returns:
        float: The pressure in kilopascals.
"""        

def jr_pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
"""
    Calculates the pressure loss due to friction in a pipe.

    Args:
        pipe_diameter (float): The diameter of the pipe.
        pipe_length (float): The length of the pipe.
        friction_factor (float): The pipe's friction factor.
        fluid_velocity (float): The velocity of the fluid.

    Returns:
        float: The pressure loss in kilopascals.
    """
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters) 11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters) 1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)


def jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the water pressure loss due to fittings in a pipeline.

    :param fluid_velocity: Velocity of the water flowing through the pipe in meters/second.
    :param quantity_fittings: Number of fittings in the pipeline.
    :return: The pressure loss in kilopascals.
    """
    rho = 998.2  # kg/m^3
    v = fluid_velocity
    n = quantity_fittings
    P = (-0.04 * rho * v ** 2 * n) / 2000
    return P


def jr_reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for water flow in a pipe.

    :param hydraulic_diameter: Hydraulic diameter of the pipe in meters.
    :param fluid_velocity: Velocity of the water flowing through the pipe in meters/second.
    :return: The Reynolds number, a dimensionless value.
    """
    rho = 998.2  # kg/m^3
    d = hydraulic_diameter
    v = fluid_velocity
    mu = 0.0010016  # Pascal seconds
    R = (rho * d * v) / mu
    return R


def jr_pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the water pressure loss due to water moving from a pipe with a large diameter into a pipe with a smaller diameter.

    :param larger_diameter: Diameter of the larger pipe in meters.
    :param fluid_velocity: Velocity of the water flowing through the larger diameter pipe in meters/second.
    :param reynolds_number: The Reynolds number corresponding to the larger diameter pipe.
    :param smaller_diameter: Diameter of the smaller pipe in meters.
    :return: The pressure loss in kilopascals.
    """
    D = larger_diameter
    v = fluid_velocity
    R = reynolds_number
    d = smaller_diameter
    k = 0.1 + (50 / R ** (D / d) ** 4 - 1)
    rho = 998.2  # kg/m^3
    P = (-k * rho * v ** 2) / 2000
    return P



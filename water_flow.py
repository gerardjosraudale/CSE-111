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
# Author: Josue Raudales 
# Date: 10/
# Purpose: This module provides test functions for the water_flow module.
# Sources: I used the preparation content in how to use pytest, assert and approx.


from pytest import approx
import pytest
from water_flow import jr_water_column_height, jr_pressure_gain_from_water_height, jr_pressure_loss_from_pipe

def test_jr_water_column_height():
    assert jr_water_column_height(0, 0) == 0
    assert jr_water_column_height(0, 10) == 7.5
    assert jr_water_column_height(25, 0) == 25
    assert jr_water_column_height(48.3, 12.8) == approx(57.9, abs=0.001)

def test_jr_pressure_gain_from_water_height():
    assert jr_pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert jr_pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert jr_pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_jr_pressure_loss_from_pipe():
    assert jr_pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert jr_pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])

from water_flow import jr_pressure_loss_from_fittings, jr_reynolds_number, jr_pressure_loss_from_pipe_reduction

def jr_test_pressure_loss_from_fittings():
    # Test case 1
    fluid_velocity = 0
    quantity_fittings = 3
    expected_pressure_loss = 0.0
    tolerance = 0.001
    result = jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    assert abs(result - expected_pressure_loss) < tolerance

    # Test case 2
    fluid_velocity = 1.65
    quantity_fittings = 0
    expected_pressure_loss = 0.0
    tolerance = 0.001
    result = jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    assert abs(result - expected_pressure_loss) < tolerance

    # Test case 3
    fluid_velocity = 1.65
    quantity_fittings = 2
    expected_pressure_loss = -0.109
    tolerance = 0.001
    result = jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    assert abs(result - expected_pressure_loss) < tolerance

    # Test case 4
    fluid_velocity = 1.75
    quantity_fittings = 2
    expected_pressure_loss = -0.122
    tolerance = 0.001
    result = jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    assert abs(result - expected_pressure_loss) < tolerance

    # Test case 5
    fluid_velocity = 1.75
    quantity_fittings = 5
    expected_pressure_loss = -0.306
    tolerance = 0.001
    result = jr_pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    assert abs(result - expected_pressure_loss) < tolerance

def jr_test_reynolds_number():
    # Test case 1
    hydraulic_diameter = 0.048692
    fluid_velocity = 0
    expected_reynolds_number = 0.0
    tolerance = 1
    result = jr_reynolds_number(hydraulic_diameter, fluid_velocity)
    assert abs(result - expected_reynolds_number) < tolerance

    # Test case 2
    hydraulic_diameter = 0.048692
    fluid_velocity = 1.65
    expected_reynolds_number = 80069
    tolerance = 1
    result = jr_reynolds_number(hydraulic_diameter, fluid_velocity)
    assert abs(result - expected_reynolds_number) < tolerance

    # Test case 3
    hydraulic_diameter = 0.048692
    fluid_velocity = 1.75
    expected_reynolds_number = 84922
    tolerance = 1
    result = jr_reynolds_number(hydraulic_diameter, fluid_velocity)
    assert abs(result - expected_reynolds_number) < tolerance

    # Test case 4
    hydraulic_diameter = 0.28687
    fluid_velocity = 1.65
    expected_reynolds_number = 471729
    tolerance = 1
    result = jr_reynolds_number(hydraulic_diameter, fluid_velocity)
    assert abs(result - expected_reynolds_number) < tolerance

    # Test case 5
    hydraulic_diameter = 0.28687
    fluid_velocity = 1.75
    expected_reynolds_number = 500318
    tolerance = 1
    result = jr_reynolds_number(hydraulic_diameter, fluid_velocity)
    assert abs(result - expected_reynolds_number) < tolerance

jr_test_pressure_loss_from_fittings()
jr_test_reynolds_number()

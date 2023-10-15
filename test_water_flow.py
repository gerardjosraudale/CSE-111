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

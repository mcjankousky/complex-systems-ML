# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:53:11 2026

@author: matth
"""

from IterativeMap import IterativeMap
import pytest

@pytest.fixture
def iterative_map():
    return IterativeMap()

@pytest.mark.parametrize("state_start, scale, expected_value", [
    (0,3,0),
    (0.5,4,1),
    (0.5,2,0.5)])

def test_quadratic_map_1_step(iterative_map,state_start,scale,expected_value):
    assert iterative_map.quadratic_map(state_start,scale) == expected_value

    

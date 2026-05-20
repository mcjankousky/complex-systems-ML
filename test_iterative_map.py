# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:53:11 2026

@author: matth
"""

from IterativeMap import IterativeMap


def test_quadratic_map_max():
    obj = IterativeMap()
    assert obj.quadratic_map(0.5,4)==1
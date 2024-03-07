import pytest
from ej1b1 import gcd, gcd_list, lcm, lcm_list

def test_gcd():
    assert gcd(54, 24) == 6, "The MCD of 54 and 24 should be 6."

def test_gcd_list():
    assert gcd_list([8, 12, 16]) == 4, "The MCD of [8, 12, 16] should be 4."

def test_lcm():
    assert lcm(4, 6) == 12, "The MCM of 4 and 6 should be 12."

def test_lcm_list():
    assert lcm_list([4, 6, 8]) == 24, "The MCM of [4, 6, 8] should be 24."

import pytest
from ques2 import *

def test_power():
    assert power(5, 5) == 5**5
    assert power(1.5, 2) == 1.5**2

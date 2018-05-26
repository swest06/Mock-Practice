import pytest
from  ques1 import*


def test_elem_swap():
    list1 = [1,2,3,4,5]
    list2 = [5,2,3,4,1]

    assert list2 == elem_swap(list1)

'''test_elem_swap'''
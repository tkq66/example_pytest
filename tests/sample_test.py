import pytest
import sample

def test_sample_func_result_succeed():
    x = 5
    expected = 2
    assert sample.sample_func(x) == expected, "Test failed"

def test_sample_func_divide_zero_succeed():
    x = 0
    with pytest.raises(ZeroDivisionError) as e:
        sample.sample_func(x)

def test_sample_func_result_fail():
    x = 5
    expected = 1
    assert sample.sample_func(x) == expected, "Test failed"

def test_sample_func_divide_zero_fail():
    x = 0
    expected = 0
    assert sample.sample_func(x) == expected, "Test failed"


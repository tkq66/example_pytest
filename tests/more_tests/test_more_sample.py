import pytest
from more.more_sample import SampleClass

def test_more_sample_func_2():
    sample_class = SampleClass(1, "b")
    with pytest.raises(TypeError) as e:
        sample_class.class_func_2(4)
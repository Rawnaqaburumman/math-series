from math_series import __version__
from math_series.series import fibonacci 
from math_series.series import lucas
from math_series.series import sum_series  
def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_7():
    expected=13
    actual=fibonacci(7)
    assert actual == expected

def test_lucas_4():
    expected=1
    actual=lucas(1)
    assert actual == expected

def test_sum_series_3():
    expected=2
    actual=sum_series(3)
    assert actual == expected
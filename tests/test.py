from hackathon import recursion
from hackathon import sorting

def test_sorting():
    """
    make sure top_n works correctly
    """

    assert sorting.bubble_sort([8,3,2,7,4]) == [2,3,4,7,8], 'incorrect'
    assert sorting.merge_sort([10,1,12,9,2]) == [1,2,9,10,12], 'incorrect'
    assert sorting.quick_sort([1,2,3,4,5]) == [1,2,3,4,5], 'incorrect'
    assert sorting.quick_sort([6,4,5,3,1,2]) == [1,2,3,4,5,6]

def test_factorial():

    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(4) == 24, 'incorrect'
    assert recursion.factorial(0) == 1, 'incorrect'

def test_fibonacci():

    assert recursion.fibonacci(3) == 2, 'incorrect'
    assert recursion.fibonacci(5) == 5, 'incorrect'
    assert recursion.fibonacci(8) == 21, 'incorrect'

def test_reverse():

    assert recursion.reverse('zingisa') == 'asigniz', 'incorrect'
    assert recursion.reverse('fibonacci') == 'iccanobif', 'incorrect'
    assert recursion.reverse('predict') == 'tciderp', 'incorrect'

def test_sum_array():

    assert recursion.sum_array([8,[3,2],7,4]) == 24, 'incorrect'
    assert recursion.sum_array([10,1,12,9,2]) == 34, 'incorrect'
    assert recursion.sum_array([1,2,[3,4,5]]) == 15, 'incorrect'

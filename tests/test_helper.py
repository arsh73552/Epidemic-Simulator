from Simulator.helper import helperClass


def test_custom_uv_func():
    '''
    This function is used to map the x and y coordinates of the screen to the x, y and z coordinates of the sphere.
    '''
    helper = helperClass()
    assert helper.custom_uv_func(1, 1, 1, 1, 1) == (1.0, -2.4492935982947064e-16, 6.123233995736766e-17)
    assert helper.custom_uv_func(2, 2, 2, 2, 2) == (2.0, -4.898587196589413e-16, 1.2246467991473532e-16)
    assert helper.custom_uv_func(3, 3, 3, 3, 3) == (3.0, -7.347880794884119e-16, 1.8369701987210297e-16)


def test_distance_manhattan():
    '''
    This function calculates the manhattan distance between two points in n-dimensional space.
    '''
    helper = helperClass()
    assert helper.distance_manhattan([1, 2, 3], [4, 5, 6]) == 9
    assert helper.distance_manhattan([4, 5, 6], [7, 8, 9]) == 9
    assert helper.distance_manhattan([7, 8, 9], [10, 11, 12]) == 9


def test_distance_euler():
    '''
    This function calculates the euclidean distance between two points in n-dimensional space.
    '''
    helper = helperClass()
    assert helper.distance_euler([0, 0], [3, 4]) == 5
    assert helper.distance_euler([0, 0], [6, 8]) == 10
    assert helper.distance_euler([0, 0], [9, 12]) == 15
    assert helper.distance_euler([0, 0], [12, 16]) == 20
    assert helper.distance_euler([0, 0], [15, 20]) == 25
    assert helper.distance_euler([0, 0], [18, 24]) == 30

from Simulator.helper import helperClass


def test_function():
    helper = helperClass()
    assert helper.custom_uv_func(1, 1, 1, 1, 1) == (1.0, -2.4492935982947064e-16, 6.123233995736766e-17)

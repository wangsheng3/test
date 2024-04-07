import os, sys

if os.path.exists("answers"):
    sys.path.append("answers")
else:
    sys.path.append("problems")
from python_basic import factorial, fibonacci, intersection


def test_factorial():
    input = [i for i in range(10)]
    output = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    for i in range(len(input)):
        assert factorial(input[i]) == output[i]


def test_fibonacci():
    input = [i for i in range(1, 10)]
    output = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(len(input)):
        assert fibonacci(input[i]) == output[i]


def test_intersection():
    input = [
        [[1, 1, 1], [2, 2, 2]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 2, 5], [5, 6, 7]],
        [[-1, 1, 1], [1, -1, 1]],
        [[2, 4, 5], [7, 8, 9]],
        [[10, 9, 6], [-5, -3, -2]],
    ]
    output = [None, [1, 0], [-4, 4.5], None, [-0.33333, 1.416667], [0, 0.666666]]
    for i in range(len(input)):
        if output[i] is None:
            assert intersection(input[i][0], input[i][1]) is None
        else:
            assert abs(intersection(input[i][0], input[i][1])[0] - output[i][0]) < 0.001
            assert abs(intersection(input[i][0], input[i][1])[1] - output[i][1]) < 0.001

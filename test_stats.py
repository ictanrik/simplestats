#!/anaconda/bin/python
from stats import *

def test_mean():
        assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
        assert mean([]) == 0.0
test_empty_list()


def test_float_mean():
	assert mean([0.2,0.5,1.1]) == 0.6
test_float_mean()

exit()


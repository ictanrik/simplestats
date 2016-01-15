#!/anaconda/bin/python
from stats import *

def test_mean():
        assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
        assert mean([]) == 0.0
test_empty_list()


exit()


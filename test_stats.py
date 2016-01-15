#!/anaconda/bin/python
from stats import *
from nose.tools import assert_equal, assert_almost_equals

def test_mean():
        assert_equal( mean([2,4]), 3.0)

def test_empty_list():
        assert mean([]) == 0.0

def test_float_mean():
	assert_almost_equals( mean([0.5,0.5,1]), 0.666, 2 )

def test_str_list_mean():
	assert_equal(mean(['1','2','3']), 2.0)

#exit()


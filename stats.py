#!/anaconda/bin/python

def mean(vals):
	assert type(vals) is list, 'wrong input type'
	if not vals:
		return 0.0
	return sum(vals)/len(vals)

def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
	assert mean([]) == 0.0
test_empty_list()

print(mean( [2,4,5,7] ) )
#print(mean( "blah" ))


exit()

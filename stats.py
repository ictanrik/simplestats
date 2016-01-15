#!/anaconda/bin/python

def mean(vals):
	assert type(vals) is list, 'wrong input type'
	if not vals:
		return 0.0
	return sum(vals)/len(vals)



if __name__ == '__main__':
	print(mean( [2,4,5,7] ) )
	#print(mean( "blah" ))


exit()


#!/anaconda/bin/python

def mean(vals):
	assert type(vals) is list, 'wrong input type'
	if not vals:
		return 0.0
	nvals = len(vals)
	vals = [float(x) for x in vals] #nice!
	for i in range(len(vals)):
		vals[i] = float(vals[i])
	return sum(vals)/nvals



if __name__ == '__main__':
	print(mean( [2,4,5,7] ) )
	#print(mean( "blah" ))
	print( mean( ['1','2','3'] ) )

exit()


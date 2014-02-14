
def multiplication_table():
	for i in range(1,10):
		for j in range(1,i+1):
			print "%d*%d=" %(j,i), j*i,
			#print j*i,
	  	print '\n'


multiplication_table()
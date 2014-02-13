def sushu():
	for i in range(2,101):
		m=1
		for j in range(2,i/2+1):
			if i%j==0:
				m=0
		if m: 
			print i

sushu()
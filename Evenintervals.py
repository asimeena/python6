try:
	s,e=map(int,raw_input().split())
	for i in range(s+1,e):
		if i%2!=0 :
			continue
		print(i)
except:
	print('invalid')	

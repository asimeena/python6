try:
	n=int(raw_input())
	print(int(n*(n+1)/2))
except ValueError:
	print('invalid integer')

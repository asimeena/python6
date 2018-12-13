import sys
def num():
	(a,b,c)=map(int,sys.stdin.readline().split())
	print((a*b)%c)
try:
	num()
except:
	print('invalid')

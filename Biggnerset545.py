def countd(n):
	a=0
	while(n!=0):
		n//=10
		a+=1
	print(a)
def main():
	try:
		n=int(input())
		countd(n)
	except:
		print('invalid')
main()

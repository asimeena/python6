def countd(e):
	print(e+1)
def main():
	try:
		e=int(input())
		countd(e)
	except:
		print('invalid')
main()

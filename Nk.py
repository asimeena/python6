try:
	N,K=map(int,input().split())
	l=list(map(int,input().split()))
	sum=0
	for i in range(K):
		sum+=l[i]
	print(sum)
except :
	print("invalid integer")

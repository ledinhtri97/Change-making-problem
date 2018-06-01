
def CoinGreedy(n):
	N = n
	D = [30000, 20000, 10000, 5000, 2000, 500, 200]
	X = [N/x for x in D]
	V = N
	Result = []	

	if N > 0:
		while(len(D)):
			T = [V-D[i]*X[i]+X[i] for i in range(len(D))]
			index = T.index(min(T))
			V = V - D[index]*int(X[index])
			if int(X[index]):
				Result.append((D[index], int(X[index])))
			del D[index]
			X = [V/x for x in D]	

	print(Result)
	return Result

CoinGreedy(155000)
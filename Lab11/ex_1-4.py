# Ilie Dumitru

import numpy as np

def timeSeries(times):
	return times*times*0.1-times*0.07+3.1 + \
		np.sin(3.9*np.pi*times)*1.3 + np.cos(1.2*np.pi*times)*0.9 + \
		np.random.normal(size=times.shape)*0.17

def hankel(series, L):
	N=series.size
	X=np.zeros((L, N-L+1))
	for i in range(L):
		for j in range(N-L+1):
			X[i, j]=series[i+j]
	return X

def myNormalize(M):
	for i in range(M.shape[1]):
		if M[0, i]<0:
			M[:, i]=-M[:, i]

def main():
	# ex. 1
	s=timeSeries(np.linspace(0, 10, 1000))

	# ex. 2
	L=30
	X=hankel(s, L)

	# ex. 3
	gamma1, V1=np.linalg.eigh(np.matmul(X, X.T))
	gamma2, V2=np.linalg.eigh(np.matmul(X.T, X))
	myNormalize(V1)
	myNormalize(V2)

	U, S, Vh=np.linalg.svd(X)
	myNormalize(U)
	myNormalize(Vh)

	with open("valori_ex_3.txt", "w", encoding="utf-8") as f:
		f.write(f"Valori proprii gamma1 ale matricei X*XT\n{gamma1}\n\n")
		f.write(f"Valori proprii gamma2 ale matricei XT*X\n{gamma2[np.abs(gamma2)>0.0001]}\n\n")
		f.write(f"Valorile singulare sigma ale matricei X, la patrat\n{np.flip(S*S)}\n\n")
		f.write(f"||sigma**2-gamma1||\n{np.linalg.norm(np.flip(S*S)-gamma1)}\n\n")
		f.write(f"Diferenta intre vectorii proprii si vectorii singulari\n{np.linalg.norm(np.flip(U, axis=1)-V1)}\n\n")

if __name__=="__main__":
	main()

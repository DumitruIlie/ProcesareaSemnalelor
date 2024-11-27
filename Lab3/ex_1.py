# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def genMat(N):
	# Am putea sa punem un factor de 1/sqrt(N) astfel incat produsul matricei cu transpusa complexa sa fie exact I_N
	return np.matrix(
		[
			[np.exp(-2j*np.pi*i*j/N) for j in range(N)] # linia i
			for i in range(N)
		]
	)

def desenMatrice(M):
	M=np.array(M)
	N=M.shape[0]
	fig, axs=plt.subplots(N)
	x=np.arange(N)
	for i in range(N):
		axs[i].plot(x, M[i, :].real, "green", label="real")
		axs[i].plot(x, M[i, :].imag, "red", label="imaginar")
		axs[i].set_ylim(-1, 1)

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='upper center')

	plt.savefig("Plot_ex_1.pdf")
	plt.cla()

def main():
	N=8
	F=genMat(N)
	FH=F.getH()
	P=F*FH
	if np.abs(P[0, 0]-N)>1e-5:
		print(f"Ceva nu e bine, pe diagonala avem {P[0][0]} in loc de {N}.")
	else:
		P/=P[0, 0]
		if not np.allclose(np.eye(N), P):
			print(f"Inmultirea nu pare bine facuta.\n{P=}")
		else:
			desenMatrice(F)

if __name__=="__main__":
	main()

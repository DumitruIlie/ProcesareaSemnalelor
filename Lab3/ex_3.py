# Ilie Dumitru

import matplotlib.pyplot as plt
import numpy as np
import ex_1

# [start, end)
def linspace(start, end, steps):
	return start+np.arange(steps)*((end-start)/steps)

def main():
	semnal=lambda x: 0.5*np.sin(2*np.pi*50*x+np.pi*0.5)+2*np.cos(2*np.pi*20*x+np.pi/3)+np.cos(2*np.pi*30*x)
	#  x=np.linspace(0, 1, 1024)
	x=linspace(0, 1, 1024)

	fig, axs=plt.subplots(2, figsize=(5, 10))
	axs[0].plot(x, semnal(x))

	N=x.shape[0]
	X=np.zeros(N, dtype=complex)
	for w in range(N):
		# Componenta w (omega) sau m (cum era in curs)
		X[w]=sum([semnal(x[i])*np.exp(-2j*np.pi*w*i/N) for i in range(N)])

	axs[1].stem(np.arange(N), np.abs(X))
	axs[1].set_aspect("equal")

	plt.savefig("Plot_ex_3.pdf")
	plt.close(fig)

	# Mai jos se poate testa, folosind matricea Fourier de la exercitiul 1, ca ambele dau acelasi raspuns
	#  X=ex_1.genMat(N)*semnal(x).reshape(-1, 1)
	#  plt.stem(np.arange(N), np.abs(X))
	#  plt.show()

if __name__=="__main__":
	main()

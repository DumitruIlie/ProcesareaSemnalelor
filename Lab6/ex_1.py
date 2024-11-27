# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def main():
	x=np.random.random(100)
	fig, axs=plt.subplots(4, layout="constrained")
	axs[0].plot(np.arange(x.shape[0])/x.shape[0], x)
	axs[0].set_xlabel("x")
	axs[0].set_ylabel("f(x)")
	axs[0].set_title("Random")
	x=np.convolve(x, x)
	x/=np.max(x)
	axs[1].plot(np.arange(x.shape[0])/x.shape[0], x)
	axs[1].set_xlabel("x")
	axs[1].set_ylabel("f2(x)")
	axs[1].set_title("Prima iteratie")
	x=np.convolve(x, x)
	x/=np.max(x)
	axs[2].plot(np.arange(x.shape[0])/x.shape[0], x)
	axs[2].set_xlabel("x")
	axs[2].set_ylabel("f4(x)")
	axs[2].set_title("A doua iteratie")
	x=np.convolve(x, x)
	x/=np.max(x)
	axs[3].plot(np.arange(x.shape[0])/x.shape[0], x)
	axs[3].set_xlabel("x")
	axs[3].set_ylabel("f8(x)")
	axs[3].set_title("A treia iteratie")
	plt.savefig("Plot_ex_1.pdf")
	fig.clf()

	# Se observa ca ploturile "tind" spre o variabila aleatoare normala. Acest fapt este cunoscut drept
	# Teorema Limita Centrala.
	# Mai multe detalii: https://www.youtube.com/watch?v=zeJD6dqJ5lo&pp=ygUYM2IxYiBub3JtYWwgZGlzdHJpYnV0aW9u

if __name__=="__main__":
	main()

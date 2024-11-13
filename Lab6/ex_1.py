# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def main():
	x=np.random.random(100)
	fig, axs=plt.subplots(4)
	axs[0].plot(np.arange(x.shape[0])/x.shape[0], x)
	x=np.convolve(x, x)
	axs[1].plot(np.arange(x.shape[0])/x.shape[0], x)
	x=np.convolve(x, x)
	axs[2].plot(np.arange(x.shape[0])/x.shape[0], x)
	x=np.convolve(x, x)
	axs[3].plot(np.arange(x.shape[0])/x.shape[0], x)
	plt.savefig("Plot_ex_1.pdf")
	fig.clf()

	# Se observa ca ploturile "tind" spre o variabila aleatoare normala. Acest fapt este cunoscut drept
	# Teorema Limita Centrala.
	# Mai multe detalii: https://www.youtube.com/watch?v=zeJD6dqJ5lo&pp=ygUYM2IxYiBub3JtYWwgZGlzdHJpYnV0aW9u

if __name__=="__main__":
	main()

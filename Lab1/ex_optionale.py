# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoida(A, frq, phz):
	return lambda x: A*np.sin(2*np.pi*frq*x+phz)

def main():
	# Frecventa variaza
	x=np.linspace(0, 5, 1000)
	f=lambda t: np.sin(2*np.pi*t*t)
	plt.plot(x, f(x))
	plt.suptitle(f"Exercitiu optional")
	plt.savefig(f"Plot_ex_optional_1.pdf")
	plt.close()

	# Doua sinusoide diferite care arata la fel
	fig, axs=plt.subplots(2)
	fig.suptitle("Exercitiu optional")
	x=np.linspace(0, 1, 100)
	s0=sinusoida(1, 200, 0)
	s1=sinusoida(1, 2, 0)
	axs[0].plot(x, s0(x))
	axs[1].plot(x, s1(x))
	plt.savefig("Plot_ex_optional_2.pdf")
	plt.close(fig)

if __name__=="__main__":
	main()

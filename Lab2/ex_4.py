# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def main():
	f=sinusoidal(1, 3, 0)
	g=lambda x : np.mod(x, 1)
	x=np.linspace(0, 5, 10000)
	fig, axs=plt.subplots(3)
	axs[0].plot(x, f(x))
	axs[1].plot(x, g(x))
	axs[2].plot(x, f(x)+g(x))

	plt.savefig("Plot_ex_4.pdf")
	plt.close()

if __name__=="__main__":
	main()

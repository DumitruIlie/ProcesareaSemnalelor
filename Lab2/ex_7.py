# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def main():
	f=sinusoidal(1, 30, 0)
	x=[np.linspace(0, 1, 1000//(4**i)) for i in range(3)]
	fig, axs=plt.subplots(3)
	axs[0].plot(x[0], f(x[0]))
	axs[1].plot(x[1], f(x[1]))
	axs[2].plot(x[2], f(x[2]))
	plt.savefig("Plot_ex_7.pdf")
	plt.close()

if __name__=="__main__":
	main()

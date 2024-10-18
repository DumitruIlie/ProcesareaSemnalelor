# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def cosinusoidal(A, frq, phi):
	return lambda x : A*np.cos(2*np.pi*frq*x+phi)

def main():
	x=np.linspace(0, 1, 300)
	f=sinusoidal(1, 3, np.pi*0.5)
	g=cosinusoidal(1, 3, 0)

	fig, axs=plt.subplots(2)
	axs[0].plot(x, f(x))
	axs[1].plot(x, g(x))
	plt.savefig("Plot_ex_1.pdf")
	plt.close()

if __name__=="__main__":
	main()

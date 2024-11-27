# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def main():
	fs=100
	x=np.linspace(0, 1, fs)
	f0=sinusoidal(1, fs/2, 0)
	f1=sinusoidal(1, fs/4, 0)
	f2=sinusoidal(1, 0, 0)
	fig, axs=plt.subplots(3, layout="constrained")
	axs[0].stem(x, f0(x))
	axs[0].set_title("fs/2")
	axs[1].stem(x, f1(x))
	axs[1].set_title("fs/4")
	axs[2].stem(x, f2(x))
	axs[2].set_title("0")
	plt.savefig("Plot_ex_6.pdf")
	plt.cla()

if __name__=="__main__":
	main()

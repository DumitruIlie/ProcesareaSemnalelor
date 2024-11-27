# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def main():
	x=np.linspace(-np.pi*0.5, np.pi*0.5, 2000)
	#  x=np.linspace(-np.pi, np.pi, 2000) # Pare ca e relativ decenta si pe intervalul asta
	i=lambda x : x
	#  f=sinusoidal(1, 0.5/np.pi, 0)
	f=np.sin
	p=lambda x : (x-7*x*x*x/60)/(1+x*x/20)
	fig, axs=plt.subplots(4, layout="constrained", figsize=(5, 18))
	for ax in axs[3:]:
		ax.set_yscale("log")
	axs[0].plot(x, i(x))
	axs[0].set_title("Identitatea")
	axs[1].plot(x, p(x))
	axs[1].set_title("Pade")
	axs[2].plot(x, f(x))
	axs[2].set_title("Sinus")
	axs[3].plot(x, np.abs(p(x)-f(x)), "green", label="Eroare pade")
	axs[3].plot(x, np.abs(i(x)-f(x)), "red", label="Eroare identitate")
	axs[3].legend()
	axs[3].set_title("Erori")
	plt.savefig("Plot_ex_8.pdf")
	plt.cla()

if __name__=="__main__":
	main()

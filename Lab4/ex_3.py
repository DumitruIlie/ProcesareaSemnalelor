# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

# [start, end)
def linspace(start, end, steps):
	return start+np.arange(steps)*((end-start)/steps)

def main():
	x=linspace(0, 1, 1000)
	s=lambda x : np.sin(2*np.pi*13*x)
	t=lambda x : np.sin(2*np.pi*6*x)
	u=lambda x : np.sin(-2*np.pi*x)

	fig, axs=plt.subplots(3)

	# Sunt de fapt 3 semnale
	axs[0].plot(x, s(x), "red")
	axs[1].plot(x, t(x), "green")
	axs[2].plot(x, u(x), "blue")

	y=linspace(0, 1, 70)
	axs[0].stem(y, s(y), "pink")
	axs[1].stem(y, t(y), "yellow")
	axs[2].stem(y, u(y), "cyan")

	plt.savefig("Plot_ex_3.pdf")
	plt.clf()

if __name__=="__main__":
	main()

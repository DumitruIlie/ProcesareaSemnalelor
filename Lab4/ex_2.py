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

	# Sunt de fapt 3 semnale
	plt.plot(x, s(x), "red")
	plt.plot(x, t(x), "green")
	plt.plot(x, u(x), "blue")

	y=linspace(0, 1, 7)
	plt.stem(y, s(y), "black")

	plt.savefig("Plot_ex_2.pdf")
	plt.clf()

if __name__=="__main__":
	main()

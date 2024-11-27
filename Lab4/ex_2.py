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
	plt.plot(x, s(x), "red", label="sin(2*pi*13*x)")
	plt.plot(x, t(x), "green", label="sin(2*pi*6*x)")
	plt.plot(x, u(x), "blue", label="sin(-2*pi*x)")

	y=linspace(0, 1, 7)
	plt.stem(y, s(y), "black", label="esantioane")

	plt.suptitle("Aliere")
	plt.xlabel("Timp")
	plt.ylabel("Amplitudine")
	plt.legend(*plt.gca().get_legend_handles_labels(), loc='upper left')
	plt.savefig("Plot_ex_2.pdf")
	plt.clf()

if __name__=="__main__":
	main()

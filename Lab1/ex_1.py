# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoida(A, frq, phz):
	return lambda x: A*np.sin(2*np.pi*frq*x+phz)

def main():
	# Formula din pdf se reduce la asta, deoarece avem un 2 in plus in sinusoidala
	x=sinusoida(1, 260, np.pi/3)
	y=sinusoida(1, 140, -np.pi/3)
	z=sinusoida(1, 60, np.pi/3)

	coords=np.linspace(0, 0.03, 60)
	#  coords=np.linspace(0, 0.03, 200)
	vals=[x, y, z]

	fig, axs=plt.subplots(3)
	fig.suptitle("Exercitiu 1")
	for i in range(3):
		axs[i].plot(coords, vals[i](coords))
	#  plt.show()
	plt.savefig("Plot_ex_1_frc_60.pdf")
	#  plt.savefig("Plot_ex_1_frc_200.pdf")
	plt.close()

if __name__=="__main__":
	main()

# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def sinusoida(A, frq, phz):
	return lambda x: A*np.sin(2*np.pi*frq*x+phz)

def saveSignal(signal, filePath="./semnal.wav"):
	scipy.io.wavfile.write(filePath, 1_000_000, signal)

def plot_1d(f, x, id_pct):
	saveSignal(f(np.linspace(0, 10, 30000)), f"./semnal_ex_{id_pct}.wav")
	plt.plot(x, f(x))
	plt.suptitle(f"Exercitiu 2 pct {id_pct}")
	plt.savefig(f"Plot_ex_2_pct_{id_pct}.pdf")
	plt.cla()


def pct_a():
	plot_1d(sinusoida(1, 400, 0), np.linspace(0, 0.2, 1600), "a")

def pct_b():
	# 100 se poate modifica, dar functioneaza ciudat, la 2400 avem de fapt o sinusoida cu frecventa 1/3
	# la 800 frecventa 1 ...
	plot_1d(sinusoida(1, 800, 0), np.linspace(0, 3, 100), "b")

def pct_c():
	plot_1d(lambda x: np.mod(x, 1)*2-1, np.linspace(0, 4, 100), "c")

def pct_d():
	plot_1d(lambda x:1-np.mod(np.floor(x), 2)*2, np.linspace(0, 6, 100), "d")

def pct_e():
	vals=np.random.rand(128, 128)
	plt.imshow(vals)
	plt.suptitle("Exercitiu 2 pct e")
	plt.savefig("Plot_ex_2_pct_e.pdf")
	plt.cla()

def pct_f():
	s=sinusoida(0.5, 5, 0)
	c=sinusoida(0.5, 5, np.pi*0.5)
	x=c(np.linspace(0, 1, 100)).reshape((100, 1))
	y=s(np.linspace(0, 1, 100)).reshape((1, 100))
	plt.imshow(x+y)
	plt.suptitle("Exercitiu 2 pct f")
	plt.savefig("Plot_ex_2_pct_f.pdf")
	plt.cla()

def main():
	pct_a()
	pct_b()
	pct_c()
	pct_d()
	pct_e()
	pct_f()

if __name__=="__main__":
	main()

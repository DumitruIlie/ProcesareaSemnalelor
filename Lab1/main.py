# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def sinusoida(A, frq, phz):
	return lambda x: A*np.sin(2*np.pi*frq*x+phz)

def ex_1():
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
	plt.cla()

def ex_2():
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

	pct_a()
	pct_b()
	pct_c()
	pct_d()
	pct_e()
	pct_f()

def ex_3():
	# Pct a: 1/2000 sec = 0.0005 sec
	# Pct b: 0.125 byte/bit * 4 bit/esantion * 2000 esantion/sec * 60 sec/ora = 60000 byte
	pass

def ex_optionale():
	# Frecventa variaza
	x=np.linspace(0, 5, 1000)
	f=lambda t: np.sin(2*np.pi*t*t)
	plt.plot(x, f(x))
	plt.suptitle(f"Exercitiu optional")
	plt.savefig(f"Plot_ex_optional_1.pdf")
	plt.cla()

	# Doua sinusoide diferite care arata la fel
	fig, axs=plt.subplots(2)
	fig.suptitle("Exercitiu optional")
	x=np.linspace(0, 1, 100)
	s0=sinusoida(1, 200, 0)
	s1=sinusoida(1, 2, 0)
	axs[0].plot(x, s0(x))
	axs[1].plot(x, s1(x))
	plt.savefig("Plot_ex_optional_2.pdf")
	plt.cla()

def main():
	#  ex_1()
	ex_2()
	#  ex_3()
	#  ex_optionale()
	pass

if __name__=="__main__":
	main()

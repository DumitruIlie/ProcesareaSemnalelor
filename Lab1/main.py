import numpy as np
import matplotlib.pyplot as plt

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

def ex_2():
	def plot_1d(f, x, id_pct):
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

def main():
	#  ex_1()
	#  ex_2()
	#  ex_3()
	pass

if __name__=="__main__":
	main()

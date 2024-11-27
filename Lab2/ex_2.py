# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def noiseify(signal, SNR):
	z=np.random.normal(0, 1, signal.shape[0])
	gamma=np.linalg.norm(signal)/np.linalg.norm(z)/np.sqrt(SNR)

	if abs((np.linalg.norm(signal)/gamma/np.linalg.norm(z))**2-SNR)>1e-5:
		print(f"SNR in={SNR} but out={(np.linalg.norm(signal)/gamma/np.linalg.norm(z))**2}")

	return signal+gamma*z

def main():
	x=np.linspace(0, 1, 500)
	f=[sinusoidal(1, 4, ph) for ph in [0, np.pi*0.5, np.pi, np.pi*1.5]]
	for g in f:
		plt.plot(x, g(x))
	plt.suptitle("Semnal fara zgomot")
	plt.savefig("Plot_ex_2_no_noise.pdf")
	plt.cla()

	SNRs=[100, 10, 1, 0.1]
	fig, axs=plt.subplots(len(SNRs)+1, layout="constrained")
	axs[0].plot(x, f[0](x))
	axs[0].set_title("Semnal pur")
	for i in range(len(SNRs)):
		SNR=SNRs[i]
		axs[i+1].plot(x, noiseify(f[0](x), SNR))
		axs[i+1].set_title(f"{SNR=}")
		#  axs[i+1].legend()
	plt.savefig("Plot_ex_2_noised.pdf")
	plt.cla()

if __name__=="__main__":
	main()

# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def dreptunghiular(Nw):
	return np.ones(Nw)

def Hanning(Nw):
	return 0.5-0.5*np.cos(2*np.pi/Nw*np.arange(Nw))

def sinusoida(A, frcv, phi, samples):
	return A*np.sin(phi+2*np.pi*frcv*samples)

# [start, end)
def linspace(start, end, cnt):
	return start+(end-start)*np.arange(cnt)/cnt

def main():
	samples=linspace(0, 0.3, 1000)
	s=sinusoida(1, 100, 0, samples)

	fig, axs=plt.subplots(3, layout="constrained")

	axs[0].plot(samples, s)
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")
	axs[0].set_title("Semnal")

	filt1=np.convolve(s, dreptunghiular(200))
	axs[1].plot(np.arange(filt1.shape[0])/samples.shape[0], filt1)
	axs[1].set_xlabel("Timp")
	axs[1].set_ylabel("Amplitudine")
	axs[1].set_title("Convolutie cu filtru dreptunghiular")

	filt2=np.convolve(s, Hanning(200))
	axs[2].plot(np.arange(filt2.shape[0])/samples.shape[0], filt2)
	axs[2].set_xlabel("Timp")
	axs[2].set_ylabel("Amplitudine")
	axs[2].set_title("Convolutie cu filtru Hanning")

	plt.suptitle("Filtrari")
	plt.savefig("Plot_ex_3.pdf")
	fig.clf()

if __name__=="__main__":
	main()

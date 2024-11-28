# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def plot(ax, semnal):
	ax.plot(np.arange(semnal.shape[0]), semnal)

def main():
	semnal=np.genfromtxt("./Train.csv", delimiter=",")[1:, 0:4:2].swapaxes(0, 1)[1]

	# Punctul a
	semnal=semnal[:3*24]
	ws=[5, 9, 13, 17]
	fig, axs=plt.subplots(1+len(ws), layout="constrained", figsize=(5, (len(ws)+1)*3))
	axs[0].plot(np.arange(semnal.shape[0]), semnal)
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")
	axs[0].set_title("Semnal original")

	# Punctul b
	for w in range(len(ws)):
		conv=np.convolve(semnal, np.ones(ws[w])/ws[w], "valid")
		axs[w+1].plot(np.arange(conv.shape[0]), conv)
		axs[w+1].set_xlabel("Timp")
		axs[w+1].set_ylabel("Amplitudine")
		axs[w+1].set_title(f"Filtrare cu len={ws[w]}")

	plt.suptitle("Filtrari cu medie alunecatoare")
	plt.savefig("Plot_ex_4_pct_b.pdf")
	plt.close()

	# Punctul c
	# Vreau sa scot componentele cu perioada mai mica de 200 de minute.
	# Deci componentele cu frecventa mai mare de 1/(200 min) * (1 min)/(60 sec) = 1/12000 Hz.
	# Frecventa de esantionare este 1/3600 Hz. Daca presupunem ca esantioanele au fost facute
	# "corect", cu o frecventa mai mare decat frecventa Nyquist, obtinem ca aceasta este < 1/3600 Hz.
	# Voi considera totusi ca frecventa Nyquist este exact 1/3600 Hz ca sa fac mai simplu exercitiul.
	# Frecventa normalizata este 1/12000 / (1/3600) = 0.3

	# Punctul d
	Wn=1/12000
	fs=1/3600
	filt1=scipy.signal.butter(5, Wn, btype="low", fs=fs)
	filtrat1=scipy.signal.filtfilt(*filt1, semnal)

	filt2=scipy.signal.cheby1(5, 5, Wn, btype="lowpass", fs=fs)
	filtrat2=scipy.signal.filtfilt(*filt2, semnal)

	# Punctul e
	fig, axs=plt.subplots(3, layout="constrained")
	axs[0].plot(np.arange(semnal.shape[0]), semnal)
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")
	axs[0].set_title("Semnal original")
	axs[1].plot(np.arange(filtrat1.shape[0]), filtrat1)
	axs[1].set_xlabel("Timp")
	axs[1].set_ylabel("Amplitudine")
	axs[1].set_title("Filtrare cu Butterworth")
	axs[2].plot(np.arange(filtrat2.shape[0]), filtrat2)
	axs[2].set_xlabel("Timp")
	axs[2].set_ylabel("Amplitudine")
	axs[2].set_title("Filtrare cu Chebyshev")
	plt.suptitle("Filtre Butterworth si Chebyshev")
	plt.savefig("Plot_ex_4_pct_e.pdf")
	plt.close()

	# As folosi filtrul Butterworth, deoarece pare sa reflecte mai bine caracteristicile semnalului original

	fig, axs=plt.subplots(3, layout="constrained")
	axs[0].stem(np.arange(semnal.shape[0]), 10*np.log10(np.abs(np.fft.fft(semnal))))
	axs[0].set_xlabel("Frecventa")
	axs[0].set_ylabel("Intensitate (dB)")
	axs[0].set_title("FFT semnal original")
	axs[1].stem(np.arange(filtrat1.shape[0]), 10*np.log10(np.abs(np.fft.fft(filtrat1))))
	axs[1].set_xlabel("Frecventa")
	axs[1].set_ylabel("Intensitate (dB)")
	axs[1].set_title("FFT semnal filtrat cu Butterworth")
	axs[2].stem(np.arange(filtrat2.shape[0]), 10*np.log10(np.abs(np.fft.fft(filtrat2))))
	axs[2].set_xlabel("Frecventa")
	axs[2].set_ylabel("Intensitate (dB)")
	axs[2].set_title("FFT semnal filtrat cu Chebyshev")
	plt.suptitle("FFT semnal filtrat")
	plt.savefig("Plot_fft_semnal_filtrat.pdf")
	plt.clf()

	# Punctul f
	orders=[3, 4, 5, 6, 7]
	rps=[4, 5, 6]
	nrPlots=1+len(orders)*(len(rps)+1)
	fig, axs=plt.subplots(nrPlots, layout="constrained")
	fig.set_figheight(nrPlots*1.2)
	axs=axs.reshape(-1)

	plot(axs[0], semnal)
	axs[0].set_title("Original")
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")
	for i in range(len(orders)):
		filt=scipy.signal.butter(orders[i], Wn, btype="low", fs=fs)
		plot(axs[1+i*len(rps)+i], scipy.signal.filtfilt(*filt, semnal))
		axs[1+i*len(rps)+i].set_title(f"Butter ordin {orders[i]}")
		axs[1+i*len(rps)+i].set_xlabel("Timp")
		axs[1+i*len(rps)+i].set_ylabel("Amplitudine")

		for j in range(len(rps)):
			filt=scipy.signal.cheby1(orders[i], rps[j], Wn, btype="lowpass", fs=fs)
			plot(axs[2+i*len(rps)+i+j], scipy.signal.filtfilt(*filt, semnal))
			axs[2+i*len(rps)+i+j].set_title(f"Chebyshev ordin {orders[i]}, rp {rps[j]} dB")
			axs[2+i*len(rps)+i+j].set_xlabel("Timp")
			axs[2+i*len(rps)+i+j].set_ylabel("Amplitudine")

	plt.suptitle("Filtrari")
	plt.savefig("Plot_ex_4_pct_f.pdf")
	plt.close()

	# Filtrul Butterworth de ordin 4 pare a fi cel mai potrivit

if __name__=="__main__":
	main()

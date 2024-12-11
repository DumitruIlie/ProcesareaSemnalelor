# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

# Trend, Season, Residuals
def timeSeries(times):
	return times*times*0.1-times*0.07+3.1, \
		np.sin(3.9*np.pi*times)*1.3 + np.cos(1.2*np.pi*times)*0.9, \
		np.random.normal(size=times.shape)*0.17 # Variatii

def predictii(series, coefs):
	return np.convolve(series, np.flip(coefs), mode="valid")

def predictie(series, coefs):
	return np.matmul(series[-coefs.shape[0]:], coefs)[0]

def AR(y, p, m):
	Y=np.zeros((m, p))
	for i in range(m):
		for j in range(p):
			Y[i][j]=series[i+j]
	Gamma=np.matmul(Y.T, Y)
	gamma=np.matmul(Y.T, series[D:].copy().reshape((-1, 1)))
	x=np.linalg.solve(Gamma, gamma)

def main():
	# Punctul a
	N=1024
	times=np.arange(N)*0.01
	trend, season, residuals=timeSeries(times)
	series=trend+season+residuals
	fig, axs=plt.subplots(4, layout="constrained", figsize=(5, 15))
	axs[0].plot(times, trend)
	axs[0].set_xlabel("Timp")
	axs[0].set_ylabel("Amplitudine")
	axs[0].set_title("Trend")
	axs[1].plot(times, season)
	axs[1].set_xlabel("Timp")
	axs[1].set_ylabel("Amplitudine")
	axs[1].set_title("Sezon")
	axs[2].plot(times, residuals)
	axs[2].set_xlabel("Timp")
	axs[2].set_ylabel("Amplitudine")
	axs[2].set_title("Reziduuri")
	axs[3].plot(times, series)
	axs[3].set_xlabel("Timp")
	axs[3].set_ylabel("Amplitudine")
	axs[3].set_title("Serie")
	plt.suptitle("Serie de timp")
	plt.savefig("Plot_pct_a.pdf")
	plt.clf()

	# Punctul b
	corr=np.correlate(series, series, mode="full")
	corr=corr[corr.size//2:]
	corr=20*np.log10(corr)
	plt.plot(corr)
	plt.xlabel("t")
	plt.ylabel("Corelatie")
	plt.suptitle("Corelatia in dB")
	plt.gcf().set_size_inches(5, 5)
	plt.savefig("Plot_vector_autocorelatie.pdf")
	plt.clf()

	# Punctul c
	D=4
	Y=np.zeros((N-D, D))
	for i in range(N-D):
		for j in range(D):
			Y[i][j]=series[i+j]
	Gamma=np.matmul(Y.T, Y)
	gamma=np.matmul(Y.T, series[D:].copy().reshape((-1, 1)))
	x=np.linalg.solve(Gamma, gamma)

	pred=predictii(series, x.reshape(-1))
	fig, axs=plt.subplots(3, figsize=(5, 15), layout="constrained")
	axs[0].plot(times, series, "green", label="actual")
	axs[1].plot(np.arange(pred.shape[0])*0.01+D*0.01, pred, "red", label="predictie")
	axs[2].plot(times, series, "green", label="actual")
	axs[2].plot(np.arange(pred.shape[0])*0.01+D*0.01, pred, "red", label="predictie")
	axs[0].set_xlabel("x")
	axs[1].set_xlabel("x")
	axs[2].set_xlabel("x")
	axs[0].set_ylabel("y")
	axs[1].set_ylabel("y")
	axs[2].set_ylabel("y")
	axs[0].set_title("Serie")
	axs[1].set_title("Predictii")
	axs[2].set_title("Suprapus")
	fig.suptitle(f"Predictii cu dimensiune p={D}\nsi orizont maxim")
	plt.legend()
	plt.savefig("Plot_predictii.pdf")
	plt.clf()

if __name__=="__main__":
	main()

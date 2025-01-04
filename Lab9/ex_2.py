# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def timeSeries(times):
	return times*times*0.1-times*0.07+3.1, \
		np.sin(3.9*np.pi*times)*1.3 + np.cos(1.2*np.pi*times)*0.9, \
		np.random.normal(size=times.shape)*0.27

def medieExponentiala(x, alpha):
	if alpha<0:
		alpha=0
	elif 1<alpha:
		alpha=1
	N=x.shape[0]
	s=np.zeros(N)
	s[0]=x[0]
	for i in range(1, N):
		s[i]=x[i]*alpha+s[i-1]*(1-alpha)
	return s

def eroarePredictie(x, s):
	err=0
	N=x.shape[0]
	for i in range(N-1):
		err+=(s[i]-x[i+1])**2
	return err

def main():
	timp=np.arange(1024)/100
	components=timeSeries(timp)
	x=components[0]+components[1]+components[2]
	s=medieExponentiala(x, 0.5)
	fig, axs=plt.subplots(3, layout="constrained")

	axs[0].plot(timp, x, color="green", label="original")
	axs[1].plot(timp, x, color="green")
	axs[0].plot(timp, s, color="red", label="medie cu α=0.5")
	axs[2].plot(timp, s, color="red")

	axs[0].set_xlabel("Timp")
	axs[1].set_xlabel("Timp")
	axs[2].set_xlabel("Timp")

	axs[0].set_ylabel("Amplitudine")
	axs[1].set_ylabel("Amplitudine")
	axs[2].set_ylabel("Amplitudine")

	axs[0].set_title("Seriile suprapuse")
	axs[1].set_title("Seria originala")
	axs[2].set_title("Seria medie exponentiala")

	plt.suptitle("Medie exponentiala")
	#  print(eroarePredictie(x, s))
	# Eroarea obtinuta cu α=0.5 este in jur de 150-160 pe cazurile pe care le-am rulat
	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.savefig("Plot_ex_2_alpha_0.5.pdf")
	plt.clf()

	# Gasirea optimului
	bestAlpha=0.5
	bestErr=eroarePredictie(x, s)
	for alpha in np.linspace(0, 1, 1001):
		s=medieExponentiala(x, alpha)
		err=eroarePredictie(x, s)
		if err<bestErr:
			bestErr=err
			bestAlpha=alpha

	for alpha in np.linspace(bestAlpha-0.01, bestAlpha+0.01, 1001):
		s=medieExponentiala(x, alpha)
		err=eroarePredictie(x, s)
		if err<bestErr:
			bestErr=err
			bestAlpha=alpha

	#  print(bestErr, bestAlpha)
	s=medieExponentiala(x, bestAlpha)
	fig, axs=plt.subplots(3, layout="constrained")
	axs[0].plot(timp, x, color="green", label="original")
	axs[1].plot(timp, x, color="green")
	axs[0].plot(timp, s, color="red", label=f"medie cu α={bestAlpha}")
	axs[2].plot(timp, s, color="red")

	axs[0].set_xlabel("Timp")
	axs[1].set_xlabel("Timp")
	axs[2].set_xlabel("Timp")

	axs[0].set_ylabel("Amplitudine")
	axs[1].set_ylabel("Amplitudine")
	axs[2].set_ylabel("Amplitudine")

	axs[0].set_title("Seriile suprapuse")
	axs[1].set_title("Seria originala")
	axs[2].set_title("Seria medie exponentiala")

	plt.suptitle(f"Cea mai buna predictie incercata\n este pentru alpha={bestAlpha}")
	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.savefig(f"Plot_ex_2_alpha_cautat.pdf")
	plt.clf()

if __name__=="__main__":
	main()

# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import csv

# Punctul a
# Avem un esantion pe ora / 3600 secunde pe ora. 1/3600 esantioane pe secunda

# Punctul b
# [25-08-2012 00:00, 25-09-2014 23:00]

# Punctul c
# 1/3600 * 1/2 = 1/7200

def main():
	# Punctul d
	semnal=np.genfromtxt("./Train.csv", delimiter=",")[1:, 0:4:2].swapaxes(0, 1)
	N=semnal.shape[1]
	FS=1/3600
	frecvente=FS/N*np.linspace(0, N//2-1, N//2)
	fft=(np.fft.fft(semnal[1]))[:N//2]
	plt.plot(frecvente, np.abs(fft))
	plt.xlabel("Frecvente")
	plt.ylabel("Intensitate")
	plt.suptitle("FFT")
	plt.savefig("Plot_ex_d.pdf")
	plt.clf()

	# Punctul e
	# Deja am facut fft pentru semnal, scot componenta constanta
	fft[0]=0
	plt.plot(frecvente, np.abs(fft))
	plt.xlabel("Frecvente (fara medie)")
	plt.ylabel("Intensitate")
	plt.suptitle("FFT")
	plt.savefig("Plot_ex_e.pdf")
	plt.clf()

	# Punctul f
	maxime=sorted(list(range(N//2)), key=lambda i : -np.abs(fft[i]))[:10]
	importante=[(round(N/max((1, m))/24, 2), m) for m in maxime]
	with open("Punctul_f.txt", "w") as fisier:
		fisier.writelines("\n".join([f"Perioada {peri} zile, frecventa {frecvente[frcv]} Hz" for peri, frcv in importante]))

	# Punctul g
	# Am ales 03.12.2012. Ar trebui sa fie multe masini, fiind sarbatorile
	startingPoint=2400
	days=28
	times=startingPoint+np.arange(days*24)
	values=semnal[1, times]
	plt.plot(np.arange(days*24), values)
	plt.suptitle("Masini in decembrie 2012")
	plt.xlabel("Timp")
	plt.ylabel("Nr. masini")
	plt.savefig("Plot_ex_g.pdf")
	plt.clf()

	# Punctul h
	# Putem calcula transformata fourier a esantioanelor.
	# Componenta cu perioada de opt ore ne poate ajuta sa vedem ora de start, sau macar o posibila ora de start.
	# Putem spre exemplu presupune ca traficul este mare la orele 8, 9, 16, 17.
	# Deci putem afla 3 posibili timpi de start.
	# Aceasta idee se poate extinde.
	# Putem presupune ca sambata si duminica este mai putin trafic decat in restul saptamanii si atunci putem
	# obtine aproximari pentru ziua de start folosind faza componentei corespunzatoare unei saptamani
	# Pentru o zi ne asteptam ca in timpul zilei sa fie mai mult trafic decat noaptea.
	# Astfel de aproximari ne pot conduce din ce in ce mai aproape de raspunsul adevarat.
	# Folosim totusi niste presupuneri, pentru a le "demonstra" am putea incerca o analiza similara intr-un alt
	# set de date in care stim exact care este inceputul

	# Punctul i
	# Scot toate frecventele corespunzatoare perioadelor de sub 8 ore
	aux=np.arange(N//2)
	aux[0]=1
	aux=((N/aux)>=8)
	aux=fft*aux
	plt.plot(frecvente, np.abs(aux))
	plt.xlabel("Timp")
	plt.ylabel("Intensitate (redusa)")
	plt.suptitle("FFT (redus)")
	plt.savefig("Plot_ex_i.pdf")
	plt.clf()

if __name__=="__main__":
	main()

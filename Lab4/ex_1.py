# Ilie Dumitru

import time
import numpy as np
import matplotlib.pyplot as plt
import os

def genMat(N):
	# Am putea sa punem un factor de 1/sqrt(N) astfel incat produsul matricei cu transpusa complexa sa fie exact I_N
	return np.matrix(
		[
			np.exp(-2j*np.pi*np.arange(N))
			#  [np.exp(-2j*np.pi*i*j/N) for j in range(N)] # linia i
			for i in range(N)
		]
	)

def DFT(v):
	return genMat(v.shape[0])*v

def timeFunc(func, *params):
	start=time.time()
	func(*params)
	end=time.time()
	return end-start

# [start, end)
def linspace(start, end, steps):
	return start+np.arange(steps)*((end-start)/steps)

def main():
	s=lambda x : np.sin(2*np.pi*3*x)*0.1+np.sin(2*np.pi*2*x+np.pi/3)*0.5+np.sin(np.pi*1.5*x+np.pi/2)

	myTimes=[]
	npTimes=[]

	ns=[128<<i for i in range(7)]
	saveFile="./saved_times.npy"
	if os.path.isfile(saveFile):
		times=np.load(saveFile)
		myTimes=times[0, :]
		npTimes=times[1, :]
	else:
		for n in ns:
			x=linspace(0, 1, n).reshape(-1, 1)
			myTime=timeFunc(DFT, s(x))
			npTime=timeFunc(np.fft.fft, s(x))

			myTimes.append(myTime)
			npTimes.append(npTime)

		times=np.array([myTimes, npTimes])
		np.save(saveFile, times)

	plt.plot(np.array(ns), myTimes, "red")
	plt.plot(np.array(ns), npTimes, "green")
	plt.xscale("log")
	plt.yscale("log")
	plt.savefig("Plot_ex_1.pdf")
	plt.clf()

if __name__=="__main__":
	main()

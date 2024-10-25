# Ilie Dumitru

import scipy
import numpy as np
import matplotlib.pyplot as plt

def loadSignal(filePath="./semnal.wav"):
	return scipy.io.wavfile.read(filePath)

def saveSignal(signal, filePath="./semnal.wav"):
	scipy.io.wavfile.write(filePath, 44100, signal)

def spectrograma(sgn):
	N=sgn.shape[0]
	if N<200:
		raise Exception("Signal too short for processing")

	L=N//100
	spectr=[]
	for i in range(0, N, L//2):
		if i+L<=N:
			spectr.append(np.fft.fft(sgn[i:i+L]))
	return 10*np.log10(np.abs(np.array(spectr).T))

def drawSpec(spec, subpunct):
	plt.imshow(spec[:spec.shape[0]//2], origin="lower", cmap="plasma")
	plt.gca().set_aspect("auto")
	plt.savefig(f"Plot_ex_6_{subpunct}.pdf")
	plt.clf()

def main():
	signals=loadSignal("./AEIOU.wav")[1].swapaxes(0, 1)
	spectrograme=[spectrograma(signal) for signal in signals]
	for i in range(len(spectrograme)):
		drawSpec(spectrograme[i], i)

if __name__=="__main__":
	main()

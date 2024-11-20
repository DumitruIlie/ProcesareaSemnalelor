# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def SNR(signal):
	return np.mean(signal)*np.mean(signal)/np.var(signal)

def main():
	img=scipy.misc.face(gray=True)
	pxlNoise=400
	noiseComp=np.random.randint(-pxlNoise, pxlNoise+1, img.shape)
	noisedImg=img+noiseComp

	print(f"SNR inainte de eliminarea zgomotului: {SNR(noisedImg)}, dupa {SNR(img)}")
	print(f"In decibeli: {10*np.log10(SNR(noisedImg))} respectiv {10*np.log10(SNR(img))}")

if __name__=="__main__":
	main()

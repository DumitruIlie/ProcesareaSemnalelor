# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def SNR(signal):
	return np.mean(signal)*np.mean(signal)/np.var(signal)

def main():
	img=scipy.misc.face(gray=True)
	frecv=np.fft.fft2(img)

	N, M=img.shape
	lines=np.minimum(np.arange(N), N-np.arange(N)).reshape((N, 1))
	columns=np.minimum(np.arange(M), M-np.arange(M))

	MAXFRQ=0.08
	remove=(lines*lines/N/N+columns*columns/M/M>MAXFRQ*MAXFRQ)

	frecv2=frecv.copy()
	frecv2[remove]=0
	img2=np.real(np.fft.ifft2(frecv2))

	noise=img-img2

	fig, axs=plt.subplots(4, figsize=(10, 40))
	axs[0].imshow(img, cmap="gray")
	axs[1].imshow(img2, cmap="gray")
	axs[2].imshow(noise, cmap="gray")
	axs[3].imshow(np.abs(noise), cmap="gray")
	plt.savefig("Plot_ex_2.pdf")
	plt.clf()

	snr0=np.sum(np.multiply(img, img))/np.sum(np.multiply(noise, noise))
	snr1=SNR(img)
	print(f"SNR-ul imaginii este {snr0}, iar in decibeli {10*np.log10(snr0)}")
	print(f"SNR-ul imaginii este {snr1}, iar in decibeli {10*np.log10(snr1)}")

if __name__=="__main__":
	main()

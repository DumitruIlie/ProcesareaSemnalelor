# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt
import scipy

def main():
	img=scipy.misc.face(gray=True)
	plt.imshow(img, cmap=plt.cm.gray)
	plt.show()

	frecv=np.fft.fft2(img)
	frecv_dB=20*np.log10(np.abs(frecv))
	plt.imshow(frecv_dB)
	plt.colorbar()
	plt.show()

	rotImg=scipy.ndimage.rotate(img, 45)
	plt.imshow(rotImg, cmap=plt.cm.gray)
	plt.show()

	rotFrecv=20*np.log10(np.abs(np.fft.fft2(rotImg)))
	plt.imshow(rotFrecv)
	plt.colorbar()
	plt.show()

	frecvAxs=(np.fft.fftfreq(img.shape[1]), np.fft.fftfreq(img.shape[0]))
	plt.stem(frecvAxs[0], frecv_dB[:][0])
	plt.show()

	cutoff=120
	chopped=frecv.copy()
	chopped[frecv_dB>cutoff]=0
	imgCut=np.real(np.fft.ifft2(chopped))
	plt.imshow(imgCut, cmap=plt.cm.gray)
	plt.show()

	pxlNoise=400
	noiseComp=np.random.randint(-pxlNoise, pxlNoise+1, img.shape)
	noisedImg=img+noiseComp
	plt.imshow(noisedImg, cmap=plt.cm.gray)
	plt.show()

if __name__=="__main__":
	main()

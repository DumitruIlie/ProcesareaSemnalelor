# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

# Ne asteptam sa vedem valori in frecventa pentru "diagonala" (2, 3)
# Care de fapt este facuta din "bare verticale"
# Dar din desen ne asteptam si la valori pe "prima" linie, care sa captureze natura repetitiva orizontala
def semnal_0(N, M):
	img=np.sin(np.arange(N).reshape((N, 1))*2*np.pi+np.arange(M)*3*np.pi)
	fft=10*np.log10(0.1+np.abs(np.fft.fft2(img)))
	return img, fft

# Semnalul asta ar trebui sa fie constant 1, dar nu este din pricina erorilor de precizie
# Ar trebui sa fie 1 deoarece sin(2k pi)=0, iar cos(2k pi)=1 pentru orice k numar intreg
# In imagine se vad benzi verticale dar doar din cauza ca valoarea minima, respectiv maxima, nu este exact 1
def semnal_1(N, M):
	img=np.sin(np.arange(N)*4*np.pi).reshape((N, 1))+np.cos(6*np.pi*np.arange(M))
	fft=10*np.log10(0.1+np.abs(np.fft.fft2(img)))
	return img, fft

# Adaugm in frecventele (0, 5) si (0, -5), deci ne asteptam sa vedem benzi verticale
# Distanta dintre centrele a 2 benzi consecutive ar trebui sa fie M/5
def semnal_2(N, M):
	fft=np.zeros((N, M))
	fft[0][5]=fft[0][M-5]=1
	img=np.real(np.fft.ifft2(fft))
	return img, 10*np.log10(0.1+np.abs(fft))

# Analog exercitiului precedent, dar vom avea benzi orizontale, iar distanta dintre centrele
# a 2 benzi consecutive va fi N/5
def semnal_3(N, M):
	fft=np.zeros((N, M))
	fft[5][0]=fft[N-5][0]=1
	img=np.real(np.fft.ifft2(fft))
	return img, 10*np.log10(0.1+np.abs(fft))

# Similar cu exercitiile precedente, dar vom avea benzi oblice. Distanta dintre centrele a
# 2 benzi consecutive va fi N/5*M/5 / sqrt(N/5 * N/5 + M/5 * M/5)
# Formula de mai sus e bazata pe aria unui dreptunghi, aria unui triunghi si diagonala dreptunghiului
def semnal_4(N, M):
	fft=np.zeros((N, M))
	fft[5][5]=fft[N-5][M-5]=1
	img=np.real(np.fft.ifft2(fft))
	return img, 10*np.log10(0.1+np.abs(fft))

def main():
	N=128
	M=128

	semnale=[semnal_0, semnal_1, semnal_2, semnal_3, semnal_4]

	for i in range(len(semnale)):
		img, frcv=semnale[i](N, M)
		fig, axs=plt.subplots(2, layout="constrained")
		axs[0].imshow(img, cmap=plt.cm.gray)
		axs[0].set_xlabel("Timp")
		axs[0].set_ylabel("Amplitudine")
		axs[0].set_title("Semnal")
		axs[1].imshow(frcv)
		axs[1].set_title("")
		plt.suptitle(f"Semnal {i}")
		plt.savefig(f"Plot_ex_1_pct_{i}.pdf")
		plt.close()

if __name__=="__main__":
	main()

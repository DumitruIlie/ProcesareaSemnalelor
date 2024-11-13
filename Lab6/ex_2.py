# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def convolutieInceata(p, q):
	r=np.zeros(p.shape[0]+q.shape[0]-1)
	for i in range(p.shape[0]):
		for j in range(q.shape[0]):
			# Mai usor de gandit asa
			r[i+j]+=p[i]*q[j]
	return r

def main():
	N=100

	p=np.random.random(N)*5
	q=np.random.random(N)*5

	r=convolutieInceata(p, q)
	# Gradul "maxim" este N*2-1 pentru ca asa vine suma
	P=np.fft.fft(np.concatenate((p, np.zeros(N-1))))
	Q=np.fft.fft(np.concatenate((q, np.zeros(N-1))))
	R=np.fft.ifft(P*Q)
	# Urmatoarea linie este echivalenta si fac ce e mai sus doar ca sa arat ca stiu ce se intampla in spate.
	# Destul de sigur ca este mai rapida versiunea de jos.
	#  R=np.convolve(p, q)

	fig, axs=plt.subplots(2)
	axs[0].plot(np.arange(r.shape[0]), r)
	axs[1].plot(np.arange(R.shape[0]), np.abs(R))
	plt.savefig("Plot_ex_2.pdf")
	plt.clf()

if __name__=="__main__":
	main()

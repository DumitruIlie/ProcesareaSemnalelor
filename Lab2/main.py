# Ilie Dumitru
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sounddevice

def saveSignal(signal, filePath="./semnal.wav"):
	scipy.io.wavfile.write(filePath, 1_000_000, signal)

def loadSignal(filePath="./semnal.wav"):
	return scipy.io.wavfile.read(filePath)

def playSignal(signal):
	sounddevice.play(signal, 44100)
	sounddevice.wait()

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def cosinusoidal(A, frq, phi):
	return lambda x : A*np.cos(2*np.pi*frq*x+phi)

def ex_1():
	x=np.linspace(0, 1, 300)
	f=sinusoidal(1, 3, np.pi*0.5)
	g=cosinusoidal(1, 3, 0)

	fig, axs=plt.subplots(2)
	axs[0].plot(x, f(x))
	axs[1].plot(x, g(x))
	plt.savefig("Plot_ex_1.pdf")
	plt.cla()

def noiseify(signal, SNR):
	z=np.random.normal(0, 1, signal.shape[0])
	gamma=np.linalg.norm(signal)/np.linalg.norm(z)/np.sqrt(SNR)

	if abs((np.linalg.norm(signal)/gamma/np.linalg.norm(z))**2-SNR)>1e-5:
		print(f"SNR in={SNR} but out={(np.linalg.norm(signal)/gamma/np.linalg.norm(z))**2}")

	return signal+gamma*z

def ex_2():
	x=np.linspace(0, 1, 500)
	f=[sinusoidal(1, 4, ph) for ph in [0, np.pi*0.5, np.pi, np.pi*1.5]]
	for g in f:
		plt.plot(x, g(x))
	plt.savefig("Plot_ex_2_no_noise.pdf")
	plt.cla()

	SNRs=[100, 10, 1, 0.1]
	fig, axs=plt.subplots(len(SNRs)+1)
	axs[0].plot(x, f[0](x))
	for i in range(len(SNRs)):
		SNR=SNRs[i]
		axs[i+1].plot(x, noiseify(f[0](x), SNR))
	plt.savefig("Plot_ex_2_noised.pdf")
	plt.cla()

def ex_3():
	for pct in "abcd":
		playSignal(loadSignal(f"./semnal_ex_{pct}.wav")[1])

def ex_4():
	f=sinusoidal(1, 3, 0)
	g=lambda x : np.mod(x, 1)
	x=np.linspace(0, 5, 10000)
	fig, axs=plt.subplots(3)
	axs[0].plot(x, f(x))
	axs[1].plot(x, g(x))
	axs[2].plot(x, f(x)+g(x))

	plt.savefig("Plot_ex_4.pdf")
	plt.cla()

def ex_5():
	x=np.linspace(0, 1, 50000)
	f=sinusoidal(10, 400, 0)
	g=sinusoidal(10, 200, 0)
	playSignal(f(x))
	playSignal(g(x))
	playSignal(f(x)+g(x))

def ex_6():
	fs=100
	x=np.linspace(0, 1, fs)
	f0=sinusoidal(1, fs/2, 0)
	f1=sinusoidal(1, fs/4, 0)
	f2=sinusoidal(1, 0, 0)
	fig, axs=plt.subplots(3)
	axs[0].stem(x, f0(x))
	axs[1].stem(x, f1(x))
	axs[2].stem(x, f2(x))
	plt.savefig("Plot_ex_6.pdf")
	plt.cla()

def ex_7():
	f=sinusoidal(1, 30, 0)
	x=[np.linspace(0, 1, 1000//(4**i)) for i in range(3)]
	fig, axs=plt.subplots(3)
	axs[0].plot(x[0], f(x[0]))
	axs[1].plot(x[1], f(x[1]))
	axs[2].plot(x[2], f(x[2]))
	plt.savefig("Plot_ex_7.pdf")
	plt.cla()

def ex_8():
	x=np.linspace(-np.pi*0.5, np.pi*0.5, 2000)
	#  x=np.linspace(-np.pi, np.pi, 2000) # Pare ca e relativ decenta si pe intervalul asta
	i=lambda x : x
	#  f=sinusoidal(1, 0.5/np.pi, 0)
	f=np.sin
	p=lambda x : (x-7*x*x*x/60)/(1+x*x/20)
	fig, axs=plt.subplots(5)
	for ax in axs[3:]:
		ax.set_yscale("log")
	axs[0].plot(x, i(x))
	axs[1].plot(x, p(x))
	axs[2].plot(x, f(x))
	axs[3].plot(x, np.abs(p(x)-f(x)))
	axs[4].plot(x, np.abs(i(x)-f(x)))
	plt.savefig("Plot_ex_8.pdf")
	plt.cla()

def main():
	#  ex_1()
	#  ex_2()
	#  ex_3()
	#  ex_4()
	#  ex_5()
	#  ex_6()
	#  ex_7()
	#  ex_8()
	pass

if __name__=="__main__":
	main()

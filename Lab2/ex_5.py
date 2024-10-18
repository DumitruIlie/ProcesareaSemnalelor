# Ilie Dumitru

import numpy as np
import sounddevice

def playSignal(signal):
	sounddevice.play(signal, 44100)
	sounddevice.wait()

def sinusoidal(A, frq, phi):
	return lambda x : A*np.sin(2*np.pi*frq*x+phi)

def main():
	x=np.linspace(0, 1, 50000)
	f=sinusoidal(1, 400, 0)
	g=sinusoidal(1, 390, 0)
	playSignal(f(x))
	playSignal(g(x))
	playSignal(np.concatenate((f(x), g(x))))

	playSignal(np.concatenate([sinusoidal(1, frq, 0)(x) for frq in range(300, 401, 5)]))

if __name__=="__main__":
	main()

# Ilie Dumitru

import scipy
import sounddevice

def loadSignal(filePath="./semnal.wav"):
	return scipy.io.wavfile.read(filePath)

def playSignal(signal):
	sounddevice.play(signal, 44100)
	sounddevice.wait()

def main():
	for pct in "abcd":
		playSignal(loadSignal(f"./semnal_ex_{pct}.wav")[1])

if __name__=="__main__":
	main()

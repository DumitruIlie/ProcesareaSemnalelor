# Ilie Dumitru

import numpy as np
import matplotlib.pyplot as plt

def plotPoints(plt, pct):
	plt.set_aspect("equal")
	plt.set_xlim(-1.1, 1.1)
	plt.set_ylim(-1.1, 1.1)
	colors=np.array([
		# Pe verde si albastru nu avem culoare iar pe rosu e direct proportional cu distanta.
		# Cu cat mai departe cu atat mai negru
		[1-p.real*p.real-p.imag*p.imag, 0, 0, 1] for p in pct
	])

	plt.scatter(pct.real, pct.imag, color=colors)

def main():
	x=np.linspace(0, 1, 1000)
	s=lambda x: np.sin(2*np.pi*3*x)
	rot=lambda x, w: np.exp(-2j*np.pi*w*x)

	fig, axs=plt.subplots(2, figsize=(5, 10))
	axs[0].plot(x, s(x))
	pct=s(x)*rot(x, 1)
	plotPoints(axs[1], pct)
	plt.savefig("Plot_ex_2_fig_1.pdf")
	plt.close(fig)

	ws=[1, 2, 3, 4]
	fig, axs=plt.subplots(len(ws), figsize=(5, 5*len(ws)))
	for i in range(len(ws)):
		pct=s(x)*rot(x, ws[i])
		plotPoints(axs[i], pct)
	plt.savefig("Plot_ex_2_fig_2.pdf")
	plt.close(fig)

if __name__=="__main__":
	main()

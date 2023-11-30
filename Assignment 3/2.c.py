from scipy import signal
import soundfile as sf
from matplotlib import pyplot as plt
import numpy as np

data, samplerate = sf.read("Recording (2).wav")

z, p, k = signal.butter(4, 3400*2*np.pi, analog=True, output='zpk')

H = signal.ZerosPolesGain(z, p, k)

w, mag, phase = signal.bode(H, n=1000)

plt.plot(w/2/np.pi, 10**(mag/20))
plt.grid(which='both')
plt.xlim((1000, 10000))
plt.xlabel("f [Hz]")
plt.ylabel("Gain []")
plt.savefig("mag.png")


data, samplerate = sf.read("Recording (2)_1.wav")

t = np.arange(0, data.shape[0]/samplerate, 1/samplerate)

tf, xf, _ = signal.lsim(H, data, t)

newdata = xf[::6]

sf.write("Recording (2)3.wav", newdata, 8000)


data, samplerate = sf.read("Recording_1.wav")
print(samplerate)

t = np.arange(0, data.shape[0]/samplerate, 1/samplerate)

tf, xf, _ = signal.lsim(H, data, t)

print(t)

plt.clf()
plt.plot(t[:100], data[:100])
plt.plot(t[:100], xf[:100])
plt.savefig("2.png")

newdata = xf[::6]

sf.write("Recording3.wav", newdata, samplerate)
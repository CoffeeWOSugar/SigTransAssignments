import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

K = 20
Ts = 1/128

def x1(k, T):
    return np.cos(42*np.pi*k*T)

def x2(k, T):
    return np.cos(44*np.pi*k*T)


k = np.arange(0, K, 1)
x1_k = x1(k, Ts)
x2_k = x2(k, Ts)
x3_k = x1_k + x2_k

X3 = fft(x3_k) / K

L = K
fs = 1/Ts
fl = np.arange(0, L)/L*fs

X3b = fft(x3_k, 256) / K



L = 256
fs = 1/Ts
fl2 = np.arange(0, L)/L*fs

plt.stem(fl2, np.abs(X3b), label='X3 with zero padding')

plt.stem(fl, np.abs(X3), label='X3 without zero padding', markerfmt="g", linefmt="g")



K=1000

k = np.arange(0, K, 1)
x1_k = x1(k, Ts)
x2_k = x2(k, Ts)
x3_k = x1_k + x2_k

X3 = fft(x3_k) / K

L = K
fs = 1/Ts
fl = np.arange(0, L)/L*fs


plt.stem(fl, np.abs(X3), label="X3 with higher spectral resolution", markerfmt="k", linefmt="k")

plt.legend()

plt.xlim(-1, fs/2+1)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude []")

plt.xticks(np.arange(0, 65, 4))

plt.grid()

plt.savefig("3a_X3")

plt.clf()
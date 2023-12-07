import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

K = 20
Ts = 1/128

def x1(k):
    return np.cos(42*np.pi*k*Ts)

def x2(k):
    return np.cos(44*np.pi*k*Ts)


k = np.arange(0, K, 1)
x1_k = x1(k)
x2_k = x2(k)

X1 = fft(x1_k) / K
X2 = fft(x2_k) / K


L = K
fs = 1/Ts
fl = np.arange(0, L)/L*fs

X1b = fft(x1_k, 256) / K
X2b = fft(x2_k, 256) / K


L = 256
fs = 1/Ts
fl2 = np.arange(0, L)/L*fs

plt.stem(fl2, np.abs(X1b), label='$X_1$ without zero padding')
plt.stem(fl, np.abs(X1), label='$X_1$ with zero padding', markerfmt="g", linefmt="g")

plt.legend()

plt.xlim(-1, fs/2+1)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude []")

plt.xticks(np.arange(0, 65, 4))

plt.grid()

plt.savefig("2b_X1")

plt.clf()



plt.stem(fl2, np.abs(X2b), label='$X_2$ without zero padding')
plt.stem(fl, np.abs(X2), label='$X_2$ with zero padding', markerfmt="g", linefmt="g")

plt.legend()
plt.xlim(-1, fs/2+1)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude []')

plt.xticks(np.arange(0, 65, 4))

plt.grid()

plt.savefig("2b_X2")

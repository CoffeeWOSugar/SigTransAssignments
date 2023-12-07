import numpy as np
import matplotlib.pyplot as plt


K = 20
Ts = 1/128


k_array = np.arange(0, K, 1)


def x1(k):
    return np.cos(42*np.pi*k*Ts)

def x2(k):
    return np.cos(44*np.pi*k*Ts)


x1_array = x1(k_array)
x2_array = x2(k_array)


plt.stem(k_array, x1_array, label="x1[k]", markerfmt="b", linefmt="b")
plt.stem(k_array, x2_array, label="x2[k]", markerfmt="g", linefmt="g")

plt.xlabel('time step [k]')
plt.ylabel('Amplitude []')
plt.xticks(k_array)

plt.legend()

plt.savefig("1c")

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 15, 1000, endpoint=True) 
  
# Plot the sawtooth wave 
plt.plot(t, signal.sawtooth((2/5) * np.pi * t - np.pi), label="Odd components") 
  
# Give x, y, title axis label 
plt.xlabel('Time [ms]') 
plt.ylabel('Amplitude []') 
plt.title('Sawtooth Signal') 
  
plt.axhline(y=0, color='r', label="Even components") 
  
plt.legend()

# Display 
plt.savefig("1b") 
plt.clf()



def freq_response(a, w):
    return a**2/(a+w*1j)**2

w_arr = np.arange(-15*10**3, 15*10**3, 1)

f_arr = freq_response(1000*np.pi, w_arr)

mag_arr = np.absolute(f_arr)
phase_arr = np.angle(f_arr)


plt.plot(w_arr, mag_arr, label='Magnitude')

plt.xlabel('$\omega$ [rad/s]')
plt.ylabel('Magnitude []')

plt.legend()

plt.savefig("2a1")
plt.clf()

plt.plot(w_arr, phase_arr, label="Phase")

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel('Phase [rad]')

plt.legend()

plt.savefig("2a2")
plt.clf()




def get_nth_f_trans(n, w0, w, dw):
    bn = -2*(-1)**n/(n*np.pi)
    "x(t) = bn*sin(n*w0*t)"
    bool_arr1 = w==round(n*w0)
    bool_arr2 = w==-round(n*w0)
    bool_arr = np.logical_or(bool_arr1, bool_arr2)
    arr = np.zeros(w.shape, 'complex')
    arr[bool_arr] = bn*1j*np.pi/dw
    return arr
    
w_arr = np.arange(-15*10**3, 15*10**3, 1)

res_arr = np.zeros(w_arr.shape)
for n in range(1, 10000):
    res_arr = res_arr + get_nth_f_trans(n, 2*np.pi/5, w_arr, 1)


Y_arr = res_arr*f_arr

plt.plot(w_arr, np.absolute(res_arr), label='Magnitude of Input')
plt.plot(w_arr, np.absolute(Y_arr), label="Magnitude of Output")

plt.xlabel('$\omega$ [rad/s]')
plt.ylabel('Magnitude []')

plt.legend()

plt.savefig("2c1")
plt.clf()


plt.plot(w_arr, np.angle(res_arr), label="Phase of Input")
plt.plot(w_arr, np.angle(Y_arr), label="Phase of Output")

plt.xlabel("$\omega$ [rad/s]")
plt.ylabel('Phase [rad]')

plt.legend()

plt.savefig("2c2")
plt.clf()
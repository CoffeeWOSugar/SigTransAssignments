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
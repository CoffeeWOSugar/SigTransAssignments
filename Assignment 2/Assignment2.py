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
plt.show() 
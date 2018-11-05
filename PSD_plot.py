# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:35:11 2018

@author: Tsende
"""

import numpy as np
import matplotlib.pyplot as plt


data1 = np.loadtxt("Stability-measurement.txt")
x1 = data1[:,0]
y1 = data1[:,1]

x2 = data1[:,2]
y2 = data1[:,3]

x3 = data1[:,4]
y3 = data1[:,5]

x4 = data1[:,6]
y4 = data1[:,7]

plt.loglog(x1,y1,x2,y2,x3,y3,linewidth='0.5')
plt.title('Delay VS AC setup noise measurement')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (V$^{2}$/Hz)')

#plt.axis([10, 10e+2,10e-13, 0.001])
plt.grid(which='minor', alpha=0.1)                                                
plt.grid(which='major', alpha=0.3) 

plt.legend(['Delay chamber','AC setup','Difference'])
#plt.legend(loc='upper left', bbox_to_anchor=(1,1))

ax2 = plt.twinx()

ax2.loglog(x4,y4,linewidth='1',color='red')
ax2.set_ylabel('Integral', color='r')
ax2.tick_params('y', colors='r')
#ax2.axis([10, 10e+2,10e-4, 0.01])
#plt.title('AC stability measurement')
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('PSD (V$^{2}$/Hz)')
#plt.axis([8*10e-5, 10e+3,10e-14, 10e+2])
#plt.legend(['Integral'])

plt.grid(linestyle='-.', linewidth='0.1', color='black')
plt.savefig("Delay_vs_AC_noisecomparison.png", dpi=900)


plt.show()

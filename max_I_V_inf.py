#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:44:53 2023

@author: nicoleevans
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

I, V_inf = np.loadtxt('/Users/nicoleevans/phy224/max_I_V_Inf.txt', delimiter=',',unpack=True)

def ohmslaw(I, R)-> float:
    return I*R

popt, pcov = curve_fit(ohmslaw, I, V_inf, absolute_sigma=True)
R= popt[0]
print(R)


plt.ylabel('$Voltage Infinite \\ (V)$')
plt.xlabel('$Max Current\\ (A)$')
plt.title('Voltage Infinite vs Max Current')
plt.grid(visible=True, which='both', axis='both')
plt.plot(I, V_inf, color='blue', linestyle='solid',marker='o', markersize=5, markerfacecolor="blue", label='V Infinite')
plt.plot(I, ohmslaw(I,R), color='red', linestyle='dashed',label='$V_{inf} = I_{max}*R$')
plt.legend(loc='upper left', frameon=True)
plt.savefig('Circiut 1 Battery plot.png')

plt.show()

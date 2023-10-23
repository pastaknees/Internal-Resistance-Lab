#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:43:56 2023

@author: nicoleevans
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

R,u_R,I,u_I,V,u_V,V_infinite,u_V_infinite = np.loadtxt('/Users/nicoleevans/phy224/Circuit 2 DC 10V.csv', skiprows=1, delimiter=',',unpack=True)

def internal_R(I, R_int, V_inf) -> (float):
    return V_inf-(I*R_int)

popt, pcov = curve_fit(internal_R, I, V, sigma = u_V, absolute_sigma=True)
R_int= popt[0]
V_inf = popt[1]
curve_fit_sds = np.sqrt(np.diag(pcov))
u_R_int = curve_fit_sds[0]
u_V_inf = curve_fit_sds[1]


plt.ylabel('$Voltage \\ (V)$')
plt.xlabel('$Current\\ (A)$')
plt.title('Voltage vs Current of 10V DC Power Supply')
plt.grid(visible=True, which='both', axis='both')
plt.errorbar(I, V, u_I, u_V, marker='|', capsize=4, ecolor='black',fmt = 'none', mfc='black', mec='black', ms=5, mew=2, label='Measurement Uncertainty')
plt.plot(I, internal_R(I,R_int, V_inf), color='red', linestyle='solid',label='$V(I) = V_{infinty}-IR_{internal} $')
plt.plot(I, V, color='blue', linestyle='none',marker='o', markersize=5, markerfacecolor="blue", label='Measured voltage')
plt.legend(loc='lower left', frameon=True)
plt.savefig('Circiut 1 Battery plot.png')


print('The estimated internal resistance is ', R_int,'Ohms +-', u_R_int, 'Ohms.')
print('The estimated voltage_inf is', V_inf, 'Volts +-', u_V_inf,'Volts.')
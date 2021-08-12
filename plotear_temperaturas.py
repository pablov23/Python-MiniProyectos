# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:11:06 2020

@author: Administrador
"""

import matplotlib.pyplot as plt
import numpy as np


tempLeida= np.load('Data/Temperaturas.npy')

plt.hist(tempLeida,bins=80)
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:25:45 2022

@author: Arnav Ambre

Requirements: Python 3.8, numpy, matplotlib

Input (input.txt):
n
x1 y1
x2 y2
...
xn yn

Output (output.txt):
X    Y
x1   y1
px1  py1
...
xn yn

Also graphs given values + linear interpolation using matplotlib.
"""

#Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import sys

#Redirecting sys.stdin and sys.stdout to files
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

#Take in the input and intiialize input lists
numberDataPoints = int(sys.stdin.readline().strip("\n"))
dataX = [0 for i in range(numberDataPoints)]
dataY = dataX.copy()

#Populate input lists
for i in range(numberDataPoints):
    dataX[i],dataY[i] = map(int, sys.stdin.readline().strip("\n").split())

#Initialize output lists
outputX = []
outputY = []

#Formatting output.txt
print("X\tY")

#Starts linear interpolation from min(dataX) --> max(dataX) [inclusive]
for i in range(min(dataX),max(dataX)+1):
    linearInterpolation = np.interp(i, dataX, dataY)
    print(str(i)+"\t"+str(linearInterpolation))
    outputX.append(i)
    outputY.append(linearInterpolation)

#Plot input + linear interpolation
plt.plot(dataX, dataY, 'o')
plt.plot(outputX, outputY, '-x')
plt.show()

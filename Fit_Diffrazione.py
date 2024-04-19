# import libraries
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# ####################################################################
# initial parameters

N=1.00 # valore massimo (V) 
L=1.00 # distanza fenditura - schermo (m)
d=60.0e-06 # larghezza della fenditura (m)
b0=0.0 # background costante (V)    
LAMBDA=500.E-9 # lunghezza d'onda della luce (m)
x0=-0.05 # posizione del massimo del picco di diffrazione (m)

# ####################################################################


# function to be fitted
def diffrazione(x, N, b0,LAMBDA,x0): # y = 

    y = d/LAMBDA*(x+x0)/np.sqrt((x+x0)**2+L**2)

    return b0+N*np.sinc(y)**2 # np.sinc(x) = sin(pi*x) / (pi*x) by definition


# ####################################################################

# get dataset from file
filename = "nomefile.txt"
x,y, yerr = np.loadtxt(filename, unpack=True)

# ####################################################################

P0 = [N,b0,LAMBDA,x0] 
popt, pcov = curve_fit(diffrazione, # function to be fitted (defined above)
                       x, y, # data 
                       p0 = P0, # guessed parameters (used as starting values)
                       sigma = yerr, # error on y
                       maxfev=50000 # the more difficult is the function, the longer it takes to fit the data. If maxfev is too short, it gives a RuntimeError
                       )

print( f"FIT PARAMS\n\n\nN={popt[0]}\nb0={popt[1]}\nLAMBDA={popt[2]}\nx0={popt[3]}\n\nCOVARIANCE MATRIX = \n{pcov}")

# ####################################################################
# plot data and fit

#plt.errorbar(x,y,yerr=yerr, linestyle= '.', color = "steelblue") # uncomment to show also errorbars
plt.plot(x,y, '.', label = "data", color = 'steelblue')
plt.plot(x,diffrazione(x, *popt), 
         color = 'orange', 
         label = "FIT")

plt.legend() 
plt.xlabel("x")
plt.ylabel("y")
plt.title("diffraction fit")
#plt.show() # --> Per visualizzare
plt.savefig("./FiguraDiffrazione.png") # --> Per salvare

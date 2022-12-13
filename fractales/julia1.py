'''import numpy as np
import matplotlib.pyplot as plt

# Crear una matriz de coordenadas para el plano complejo
X = np.linspace(-1.5, 1.5, 1000)
Y = np.linspace(-1.5, 1.5, 1000)

Z = X + Y * 1j

# Definir la fórmula de Julia con c = -0.8 + 0.156i
c = -0.8 + 0.156j

# Aplicar la fórmula de Julia a la matriz de coordenadas del plano complejo
Z = Z**2 + c

# Dibujar el fractal de Julia
plt.imshow(np.abs(Z), cmap="Reds")
plt.show()
'''



# https://stackoverflow.com/questions/15024461/plot-mandelbrot-with-matplotlib-pyplot-numpy-python
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


x,y=np.ogrid[-2:1:5000j,-1.5:1.5:5000j]

print('')
print('Grid set')
print('')

c=x + 1j*y
z=0

for g in range(500):
        print('Iteration number: ',g)
        z=z**2 + c

threshold = 2
mask=np.abs(z) < threshold

print('')
print('Plotting using imshow()')
plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])

print('')
print('plotting done')
print('')

plt.gray()

print('')
print('Preparing to render')
print('')

plt.show()
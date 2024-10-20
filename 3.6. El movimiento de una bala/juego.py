python
Copiar código
import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
x0 = 0  # Posición inicial en x
y0 = 0  # Posición inicial en y
v0 = 50  # Velocidad inicial en m/s
theta = 45  # Ángulo de lanzamiento en grados
g = 9.81  # Gravedad en m/s²

# Conversión de grados a radianes
theta_rad = np.radians(theta)

# Tiempo de vuelo
t_flight = (2 * v0 * np.sin(theta_rad)) / g
t = np.linspace(0, t_flight, num=500)

# Ecuaciones de movimiento
x = x0 + v0 * np.cos(theta_rad) * t
y = y0 + v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Trayectoria de una bala')
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.xlim(0, max(x))
plt.ylim(0, max(y) + 5)
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.show()
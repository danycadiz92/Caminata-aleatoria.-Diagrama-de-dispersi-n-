import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Establece el titulo del grafico y las etiquetas de los ejes.
ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize=14)


plt.show()
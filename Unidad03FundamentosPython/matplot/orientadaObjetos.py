import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,2)
ax[0].plot([1,2,3],[4,5,6])
ax[0].set(title = "Modo OO",
       xlabel = "x",
       ylabel = "y")

ax[1].plot([5,6,7],[8,9,10])
ax[1].set(title = "Segundo gráfico")
plt.tight_layout()
plt.show()
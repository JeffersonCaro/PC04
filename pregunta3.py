import pyfiglet
import random

fig = pyfiglet.Figlet()
fig.getFonts()
fuente = input("Ingrese una de las siguientes fuentes a usar: ")

if fuente == "":
    fuente = random.choice(fig.getFonts())
else:
    fuente = fuente

texto = input("Ingrese un texto: ")

result = pyfiglet.figlet_format("texto",font = fuente)
print(result)
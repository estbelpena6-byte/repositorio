ruta_archivo = r"C:\Users\WINDOWS\Desktop\repositorio\clases\archivo\Vimm's Lair.txt"

f = open(ruta_archivo, "r")

data = f.readlines()

print(data)

f.close

with open(ruta_archivo, "r") as f:
    f.writelines("agua en el desierto\n")


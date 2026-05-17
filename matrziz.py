from os import system
if system("clear") != 0: system("cls")

matriz = [[0,1,0,1],
          [1,0,0,0],
          [0,0,1,1],
          [1,1,0,0],
          [0,1,1,0]]
fin = False
while not fin:
    fila = int(input("insertar el numero de fila: "))
    columna = int(input("insertar el numero de columna: "))
    accion = input("¿Desea salir o ingresar? (s/i): ")
    if accion == "s" or accion == "S":
        if 0 <= fila < 5 and 0 <= columna < 4:
            if matriz[fila][columna] == 1:
                matriz[fila][columna] = 0
                print("Valor cambiado a 0 ya que se retiró del lugar.")
                print(matriz)  
            else:
                print("el espacio esta vacio.")
                print(matriz)
        else:
            print("Fila o columna fuera de rango. Por favor, ingrese valores válidos.")
    elif accion == "i" or accion == "I":
        if 0 <= fila < 5 and 0 <= columna < 4:
            if matriz[fila][columna] == 0:
                matriz[fila][columna] = 1
                print("Valor cambiado a 1 ya que se estacionó en un lugar vacío.")
                print(matriz)
            elif matriz[fila][columna] == 1:
                print("el espacio esta ocupado.")
                print(matriz)
        else:
            print("Fila o columna fuera de rango. Por favor, ingrese valores válidos.")
    else:
        print("Acción no válida. Por favor, ingrese 's' para salir o 'i' para ingresar.")    
    salir = input("¿Desea salir cerrar el sistema? (s/n): ")    
    if salir == "s" or salir == "S":
        salir = input("al salir se perderan los datos, igualmente desea salir (s/n): ")
        if salir == "s" or salir == "S":
            fin = True
            print("Saliendo del sistema...")
        elif salir == "n" or salir == "N":
            print("Continuando en el sistema...")
        else:
            print("Opción no válida. Continuando en el sistema...")
    else:
        print("Continuando en el sistema...")
        


# suma = 0
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         suma = suma + matriz[i][j]
# print(f"la suma de los valores de nuestra matriz es: {suma}")

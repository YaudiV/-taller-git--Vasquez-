###
# Proyecto: Motor de optimización de dispensado (Cajero ATM).
# Yaudi Vasquez V30186941.
# Seccion: 701201.
# Unidad curricular: Algoritmos y programacion.
# Profesor: Jose Ortiz
###

### Inicio:

# Se importa el modulo "Clear" del sistema operativo para que se vea clara la ejecucion del codigo en la terminal
# al tener que ejecutar el mismo repetidas veces

from os import system
if system("clear") != 0: system("cls")

# Variables / Entradas: (coin_type: tipo de moneda), (withdraw_amount: monto a retirar), (account_type: tipo de cuenta).
# Tambien vemos los procesos logicos con el uso de (if-elif-else) para que el codigo actue si se cumplen las condiciones correctas.

print("¡Bienvenido al sistema de Cajero ATM Y.V Corporation, lea cuidadosamenta cada instruccion antes de continuar!")

# Validación por tipo de moneda:
coin_type = int(input("\nIntroducir 1 para retiro en bolivares / introducir 2 para retiro en Dólares: "))
if coin_type == 2:
    print("\nSu retiro en dólares se estará procesando")
elif coin_type == 1:
    print("\nSu retiro en Bolívares se estará procesando")
else:
    print("\nError: Tipo de moneda no está dispononible\n")
    exit()

# Validación del monto:

print("\nRecuerde que los cajeros solo pueden dispensar Billetes de 100, 50, 20 y 10")

withdraw_amount = int(input("\nIntroducir el monto a retirar: "))
if withdraw_amount % 10 == 0:
    print("\nEl monto ingresado es valido con las denominaciones disponibles")
else:
    print("\nError: Monto no compatible con denominaciones disponibles\n")
    exit()

# Validación para aplicar o no comisión:
account_type = int(input("\nIntroducir 1 para tipo de cuenta Ahorro / introducir 2 para tipo de cuenta Corriente: "))
if account_type == 2:
    print("\nse aplicara comisión del 5%, al monto a retirar")
    comision = withdraw_amount * 0.05
elif account_type == 1:
    print("\nNo se aplicara comisión")
else:
    print("\n¡Error!: Tipo de cuenta no está disponible\n")
    exit()

# Calculo para el desglose de los billetes de 100,50,20 y 10

cant_100 = withdraw_amount // 100
Resto_1 = withdraw_amount % 100
cant_50 = Resto_1 // 50
Resto_2 = Resto_1 % 50
cant_20 = Resto_2 // 20
resto_3 = Resto_2 % 20
cant_10 = resto_3 // 10
resto_4 = resto_3 % 10

print("\n------------")

# logica y salida: Uso de (match-case) y de (if-elif-else) para mostrar la salida de datos deseada con (f"strings")

match coin_type, account_type:
    case 1, 2:
        if withdraw_amount > 10000:
            print("\nTransaccion denegada: Excede limite diario")
        else:
            print("\n===RESUMEN DE RETIRO EN BOLÍVARES===")
            print(f"Monto solicitado: {withdraw_amount}")
            print(f"Comisión aplicada: {comision}")
            print("\n===DESGLOSE DE BILLETES Y MONTO TOTAL===")
            print(f"Billetes de 100:{cant_100}")
            print(f"Billetes de 50: {cant_50}")
            print(f"Billetes de 20: {cant_20}")
            print(f"Billetes de 10: {cant_10}")
            print(f"Total debitado: {withdraw_amount + comision}")
    case 2, 1:
        if withdraw_amount > 500:
            print("\nTransaccion denegada: Excede limite diario")
        else:
            print("\n===RESUMEN DE RETIRO EN DOLARES===")
            print(f"Monto solicitado: {withdraw_amount}")
            print("\n===DESGLOSE DE BILLETES Y MONTO TOTAL===")
            print(f"Billetes de 100: {cant_100}")
            print(f"Billetes de 50: {cant_50}")
            print(f"Billetes de 20: {cant_20}")
            print(f"Billetes de 10: {cant_10}")
            print(f"Total debitado: {withdraw_amount}")
    case 1, 1:
        if withdraw_amount > 10000:
            print("\nTransaccion denegada: Excede limite diario")
        else:
            print("\n===RESUMEN DE RETIRO EN BOLÍVARES===")
            print(f"Monto solicitado: {withdraw_amount}")
            print("\n===DESGLOSE DE BILLETES Y MONTO TOTAL===")
            print(f"Billetes de 100: {cant_100}")
            print(f"Billetes de 50: {cant_50}")
            print(f"Billetes de 20: {cant_20}")
            print(f"Billetes de 10: {cant_10}")
            print(f"Total debitado: {withdraw_amount}")
    case 2, 2:
        if withdraw_amount > 500:
            print("\nTransaccion denegada: Excede limite diario")
        else:
            print("\n===RESUMEN DE RETIRO EN DOLARES===")
            print(f"Monto solicitado: {withdraw_amount}")
            print(f"Comisión aplicada: {comision}")
            print("\n===DESGLOSE DE BILLETES Y MONTO TOTAL===")
            print(f"Billetes de 100:{cant_100}")
            print(f"Billetes de 50: {cant_50}")
            print(f"Billetes de 20: {cant_20}")
            print(f"Billetes de 10: {cant_10}")
            print(f"Total debitado: {withdraw_amount + comision}")
print("\n------------")
exit("\n¡¡GRACIAS POR PREFERIR EL SISTMA DE CAJERO ATM Y.V CORPORATION!!\n")
## Fin.

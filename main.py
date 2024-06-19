# Práctica de pilas realizada en la clase 8

from Pila import Pila
pila = Pila()
opcion = 0
def intinput(string):
    bandera = False
    while not bandera:
        try:
            entero = int(input(string))
            bandera = True
        except ValueError:
            print("No es un entero válido")
    return entero

while opcion !=10:
    opcion= intinput("Digite la opcion que requiera: \n"
                      "1. EsVacía \n"
                      "2. Apilar \n"
                      "3. Desapilar \n"
                      "4. Mostrar \n"
                      "5. Vaciar \n"
                      "6. Buscar\n"
                      "7. Copiar (transferir a otra fila)\n"
                      "8. Ordenar de menor a mayor\n"
                      "9. Cantidad de elementos\n"
                      "10. Salir \n: ")
    match opcion:
        case 1:
            if pila.esta_vacia():
                print("La pila está vacía")
        case 2:
            numero = intinput("Digite el número que desea apilar: ")
            pila.apilar(numero)
        case 3:
            print(pila.desapilar())
        case 4:
            print(pila.mostrar())
        case 5:
            pila.vaciar()
        case 6:
            numero = intinput("Digite el número que desea buscar: ")
            if pila.buscar(numero):
                print("El número está en la pila")
            else:
                print("El número NO está en la pila")
        case 7:
            pila_nueva = pila.copiar()
            print('Pila Nueva:')
            print(pila_nueva.mostrar())
        case 8:
            pila.ordenar_ascendente()
        case 9:
            print(pila.cantidad_elementos())
        case 10:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")

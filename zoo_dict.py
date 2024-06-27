"""
Ahora mismo este codigo no funciona porque es imposible salir del while.
Debes:
 1. Ejecutar el programa y detectar el error.
 2. Corregir ese error para que salga del while
 3. Terminar el for de impresion para que imprima algo como esto
      0 entradas de BEBE: 0.00 €
      3 entradas de NIÑO: 42.00 €
      2 entradas de ADULTO: 46.00 €
      1 entradas de JUBILADO: 18.00 €
      -----------
      TOTAL: 96.00 €
 4. Corregir cualquier otro error que pueda haber, recuerda que no hemos probado nada
 --
 5. Opcional. Si eres capaz de que escriba entrada cuando solo sea una y entradas en otro caso... estaría muy bien.
"""


"""
Indicamos mediante diccionarios los tipos de entradas que venderemos, su precio, y añadimos un contador para ver cuantas
de cada tipo se han vendido
"""
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

""""
Esta función se encarga de decidir si es entrada o entradas la palabra que acompaña al precio
recibe un diccionario y la clave donde esta el contador al que queremos apuntar, si es distinto a 1
asignara entradas

"""
def entrada_name(index,name_dic):
    entrada_name="entrada"
    if index[name_dic]!=1:
     entrada_name="entradas"
    return entrada_name

"""
Transforma la edad a entero
si no se puede vuelve a pedir una edad valida
"""
def tansform_edad(edad):
    return int(edad)
        

"""
Devuelve True si edad es mayor que 0, si no devuelve False
e imprime un aviso para el usuario
"""

def upper_zero(edad):
    result=True
    if edad<0:
        print("La edad no puede ser un número negativo, por favor ingrese una edad valida ")
        result=False
    return result



while True:
    edad = input("Edad: ").strip()
    
    if edad=="": #Si el usuario pulsa intro el bucle se detendrá y continuará el programa calculando el precio
        break

    try: 
      edad=tansform_edad(edad)#Convertimos la edad en un entero

      if upper_zero(edad):#Si edad es mayor que cero lo aceptamos

            if edad < 3 and int(edad)>0: #sumamos 1 al contador que corresponda
                tipos_entrada["BEBE"]["CONTADOR"] = tipos_entrada["BEBE"]["CONTADOR"] + 1
            elif edad < 13 and int(edad)>3:
                tipos_entrada["NIÑO"]["CONTADOR"] = tipos_entrada["NIÑO"]["CONTADOR"] + 1
            elif edad < 65 and int(edad)>13:
                tipos_entrada["ADULTO"]["CONTADOR"] = tipos_entrada["ADULTO"]["CONTADOR"] + 1
            elif edad <0:
                print("Por favor escoge una edad valida ")
            else:
                tipos_entrada["JUBILADO"]["CONTADOR"] = tipos_entrada["JUBILADO"]["CONTADOR"] + 1
    except ValueError :
            print("Por favor escoge una edad valida ") #Si el usuarío nos da algo que no sea un número se lo avisaremos

    
total = 0 

for tipo, valores in tipos_entrada.items(): #sacamos el subtotal de cada tipo de entrada multiplicando contador por el precio
    
    subtotal = valores['CONTADOR'] * valores['PRECIO']
    total+=subtotal #vamos sumando los subtotales para tener el total
    print(f"{valores['CONTADOR']} {entrada_name(valores,'CONTADOR')} de {tipo}: {subtotal:.2f} Euros") #imprimimos el precio de cada tipo de entrada
    
print(f"Total a pagar: {total} euros") #imprimimos el monto total de euros a pagar

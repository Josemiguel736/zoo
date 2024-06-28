
tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}


def ask_age():
   edad = input("Edad: ").strip()  
   return edad

def entrada_name(index,name_dic):
    """"
    Esta función se encarga de decidir si es entrada o entradas la palabra que acompaña al precio
    recibe un diccionario y la clave donde esta el contador al que queremos apuntar, si es distinto a 1
    asignara entradas

    """
    entrada_name="entrada"
    if index[name_dic]!=1:
     entrada_name="entradas"
    return entrada_name


def tansform_edad(edad):
    """
    Transforma la edad a entero
    si no se puede vuelve a pedir una edad valida
    """
    return int(edad)        

def upper_zero(edad):
    """
    Devuelve True si edad es mayor que 0, si no devuelve False
    e imprime un aviso para el usuario
    """
    result=True
    if edad<0:
        print("La edad no puede ser un número negativo, por favor ingrese una edad valida ")
        result=False
    return result


def count_tickets(edades):
 """
    Suma el contador adecuado a cada grupo de entradas

 """
 for edad in edades:
    if edad < 3 and int(edad)>=0: 
        tipos_entrada["BEBE"]["CONTADOR"] = tipos_entrada["BEBE"]["CONTADOR"] + 1
    elif edad < 13 and int(edad)>=3:
        tipos_entrada["NIÑO"]["CONTADOR"] = tipos_entrada["NIÑO"]["CONTADOR"] + 1
    elif edad < 65 and int(edad)>=13:
        tipos_entrada["ADULTO"]["CONTADOR"] = tipos_entrada["ADULTO"]["CONTADOR"] + 1
    else:
        tipos_entrada["JUBILADO"]["CONTADOR"] = tipos_entrada["JUBILADO"]["CONTADOR"] + 1


def print_cost():
 """
 Imprime los precios de las entradas, muestra tanto el valor de cada grupo de entradas como
 el coste total
 
 """
 total = 0 

 for tipo, valores in tipos_entrada.items(): #sacamos el subtotal de cada tipo de entrada multiplicando contador por el precio    
    subtotal = valores['CONTADOR'] * valores['PRECIO']
    total+=subtotal #vamos sumando los subtotales para tener el total
    print(f"{valores['CONTADOR']} {entrada_name(valores,'CONTADOR')} de {tipo}: {subtotal:.2f} Euros") #imprimimos el precio de cada tipo de entrada
    
 print(f"Total a pagar: {total} euros") #imprimimos el monto total de euros a pagar


 
def age_validate():
   """
   Valida que las edades introducidas sean validas, si lo son lo añade a una lista
   si el usuario pulsa enter cierra el bucle y 
   retorna una lista con SOLO las edades validas introducidas
   
   """
   ages=[]
   while True:      
    edad=ask_age()
    if edad=="": #Si el usuario pulsa intro el bucle se detendrá y continuará el programa calculando el precio
        break
    try: 
      edad=tansform_edad(edad)#Convertimos la edad en un entero
      if upper_zero(edad):#Si edad es mayor que cero lo aceptamos
          ages.append(edad)
    except ValueError :
            print("Por favor escoge una edad valida ") #Si el usuarío nos da algo que no sea un número se lo avisaremos
   return ages



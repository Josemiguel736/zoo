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

from zoo_func import count_tickets,print_cost,age_validate

if __name__=="__main__":
    count_tickets(age_validate())
    print_cost()
    

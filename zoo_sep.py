from zoo_func import print_cost,print_cost,count_tickets,tipos_entrada,age_validate
from simple_screen import Screen_manager,locate,cls

with Screen_manager as sc:
    count_tickets(age_validate())
    cls()
    while True:
     
     print_cost()
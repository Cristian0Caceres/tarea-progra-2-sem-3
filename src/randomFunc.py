#!/usr/bin/env python3

import random

def ClasifMonth(mes):
    if mes == 1:
        return "Enero"
    elif mes == 2:
        return "Febrero"
    elif mes == 3:
        return "Marzo"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Mayo"
    elif mes == 6:
        return "Junio"
    elif mes == 7:
        return "Julio"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Septiembre"
    elif mes == 10:
        return "Octubre"
    elif mes == 11:
        return "Noviembre"
    else:
        return "Diciembre"
    
def GenerateDate():
    mes = random.randint(1, 12)
    
    if mes in [4, 6, 9, 11]:  # Meses con 30 días
        dia = random.randint(1, 30)
    elif mes == 2:  # Febrero
        dia = random.randint(1, 28)
    else:  # Meses con 31 días
        dia = random.randint(1, 31)
    
    hora = random.randint(0, 23)
    minutos = random.randint(0, 59)
    
    mes = ClasifMonth(mes)
    
    return mes, dia, hora, minutos

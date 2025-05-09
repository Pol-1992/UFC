import pandas as pd
from datetime import datetime

def clean(series):
    series = series.str.upper().str.strip()
    return series.str.title()

def calcular_retirement_age(row):
    if row['Last Fight'].year >= 2023:
        return "Active"
    
    if pd.isna(row['Age']):
        return "Retired"
    
    birth_year = datetime.now().year - row['Age']
    edad_en_ultima_pelea = row['Last Fight'].year - birth_year
    return edad_en_ultima_pelea

def asignar_epoca(row):
    año_retiro = row['Last Fight'].year
    
    if año_retiro <= 2002:
        return "90's"
    elif año_retiro <= 2012:
        return "2000's"
    else:
        return "2010's"
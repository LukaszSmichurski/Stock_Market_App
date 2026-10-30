import yfinance as yf
from datetime import datetime as dt
import dateutil.relativedelta as rd
import streamlit as st

def Stopa_zwrotu_z_obligcji(kod_obligacji, data_zakupu):
    podana_data = data_zakupu

    dzisiaj = dt.now().replace(hour=0, minute=0, second=0, microsecond=0)

    roznica = dzisiaj - podana_data

    ilosc_dni = roznica.days

    match kod_obligacji:
        case "OTS":
            
            return 100 * ilosc_dni*1.02
        case "ROR":
             return 100 * ilosc_dni * 0.02
        case "DOR":
             return 100 * ilosc_dni * 0.02
        case "TOS":
             return 100 * ilosc_dni * 0.02
        case "COI":
            return 100 * ilosc_dni * 0.02

        case "EDO":
            return 100 * ilosc_dni * 0.02
        case "ROS":
            return 100 * ilosc_dni * 0.02

        case "ROD":
            return 100 * ilosc_dni * 0.02

        case _:
            print(f"Błąd: Nieznany symbol obligacji '{kod_obligacji}'.")


if __name__ == "__main__":
    print(Stopa_zwrotu_z_obligcji("OTS", dt(2020, 1, 2)))

    podana_data = dt(2020, 1, 2).replace(hour=0, minute=0, second=0, microsecond=0)

    dzisiaj = dt.now().replace(hour=0, minute=0, second=0, microsecond=0)
    roznica = dzisiaj - podana_data
    ilosc_dni = roznica.days

    print(ilosc_dni)
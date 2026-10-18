import streamlit as st
import plotly.express as px
import datetime as dt
from config import POPULAR_INDICES
from logic import getDate, fetch_data


with st.sidebar:
    st.title("Porównywarka Indeksów")

    wybrane_nazwy = st.multiselect(
        "Wybierz instrumenty do porównania:",
        options=list(POPULAR_INDICES.keys()),
        default=["S&P 500 (USA - Szeroki rynek)"]
    )
    wybrane_tickery = [POPULAR_INDICES[nazwa] for nazwa in wybrane_nazwy]

    period = st.selectbox("Period",("1 Month", "6 Months", "1 Year", "5 Years"))

    start_date = dt.date.today() - getDate(period)
    end_date = dt.date.today()

if st.button("Oblicz"):
    ceny = fetch_data(wybrane_tickery, start_date, end_date)
    normalized_data = (ceny/ceny.iloc[0]*100)

    rate_of_return = (ceny.iloc[-1] - ceny.iloc[0]) / ceny.iloc[0]*100



    fig = px.line(normalized_data)
    st.plotly_chart(fig, use_container_width=True)

    cols = st.columns(len(wybrane_nazwy))
    for i, nazwa in enumerate(wybrane_nazwy):
        ticker = POPULAR_INDICES[nazwa]
        try:
            wynik_procentowy = float(rate_of_return[ticker])
            aktualna_cena = float(ceny[ticker].iloc[-1])
        except KeyError:
            wynik_procentowy = float(rate_of_return)
            aktualna_cena = float(ceny.iloc[-1])

        cols[i].metric(nazwa, f"{round(aktualna_cena, 2)}", f"{round(wynik_procentowy, 2)} %")
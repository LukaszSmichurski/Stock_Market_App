import streamlit as st
import plotly.express as px
import datetime as dt

from config import POPULAR_INDICES, GEM_ORIGINAL, GEM_ZAWOD_INWESTOR
from logic import getDate, fetch_data

WSZYSTKIE_INSTRUMENTY = {**POPULAR_INDICES, **GEM_ORIGINAL, **GEM_ZAWOD_INWESTOR}

st.set_page_config(
    page_title="Fintech Dashboard",
    layout="wide"
)

with st.sidebar:
    st.title("Index Comparison")

    tryb = st.radio(
        "Analysis mode:",
        ["Instruments of your choice", "GEM strategy"],
        horizontal=True
    )

    st.markdown("---")

    if tryb == "Instruments of your choice":
        wybrane_nazwy = st.multiselect(
            "Select instruments for comparison:",
            options=list(POPULAR_INDICES.keys())
        )
    else:
        st.info("The GEM mode loads the relevant assets to determine what is winning under the Dual Momentum strategy.")
        wersja_gem = st.selectbox("Strategy version:", ["Original (USA)", "European (UCITS - XTB)"])

        if wersja_gem == "Original (USA)":
            wybrane_nazwy = list(GEM_ORIGINAL.keys())
        else:
            wybrane_nazwy = list(GEM_ZAWOD_INWESTOR.keys())

        st.multiselect("Instruments examined in this strategy:", wybrane_nazwy, default=wybrane_nazwy, disabled=True)

    period = st.selectbox("Period", ("1 Month", "6 Months", "1 Year", "5 Years"))

    start_date = dt.date.today() - getDate(period)
    end_date = dt.date.today()

    st.markdown("---")

    oblicz_klikniety = st.button("Calculate the rates of return", type="primary", use_container_width=True)


if oblicz_klikniety:
    if not wybrane_nazwy:
        st.warning("Select at least one instrument")
    else:
        with st.spinner("Fetching data from the exchange..."):

            wybrane_tickery = [WSZYSTKIE_INSTRUMENTY[n] for n in wybrane_nazwy]
            ceny = fetch_data(wybrane_tickery, start_date, end_date)
            normalized_data = (ceny / ceny.iloc[0] * 100)

            rate_of_return = (ceny.iloc[-1] - ceny.iloc[0]) / ceny.iloc[0] * 100

            fig = px.line(normalized_data, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

            cols = st.columns(len(wybrane_nazwy))


            for i, nazwa in enumerate(wybrane_nazwy):
                ticker = WSZYSTKIE_INSTRUMENTY[nazwa]
                try:
                    wynik_procentowy = float(rate_of_return[ticker])
                    aktualna_cena = float(ceny[ticker].iloc[-1])
                except KeyError:
                    wynik_procentowy = float(rate_of_return)
                    aktualna_cena = float(ceny.iloc[-1])

                cols[i].metric(nazwa, f"{round(aktualna_cena, 2)}", f"{round(wynik_procentowy, 2)} %")
else:
    st.title("Stock Market Analytics Dashboard")
    st.markdown("Welcome to the financial instrument return analysis tool.")

    st.info(
        "Configure the parameters in the **sidebar**"
        " and then click the **Calculate the rates of return** button"
        " to generate a chart."
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### What can the application do?")
        st.markdown(
            "- Compare multiple indices and ETFs simultaneously\n"
            "- Automatically normalize prices to a base of 100\n"
            "- Generate interactive charts in real time"
        )
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>"
    "Designed and developed by <a href='https://smichurski.pl' target='_blank'>Łukasz Śmichurski</a> | "
    "Version 1.0"
    "</div>",
    unsafe_allow_html=True
)
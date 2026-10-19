import streamlit as st
import plotly.express as px
import datetime as dt
from config import POPULAR_INDICES, GEM_ORIGINAL, GEM_ZAWOD_INWESTOR
from logic import getDate, fetch_data

WSZYSTKIE_INSTRUMENTY = {**POPULAR_INDICES, **GEM_ORIGINAL, **GEM_ZAWOD_INWESTOR}

st.set_page_config(
    page_title="Fintech Dashboard",
    page_icon="📈",
    layout="wide"
)

with st.sidebar:
    st.title("Porównywarka Indeksów")

    tryb = st.radio(
        "Tryb analizy:",
        ["🔍 Własny Portfel", "🚀 Strategia GEM (Momentum)"],
        horizontal=True
    )

    st.markdown("---")

    if tryb == "🔍 Własny Portfel":
        wybrane_nazwy = st.multiselect(
            "Wybierz instrumenty do porównania:",
            options=list(POPULAR_INDICES.keys())
        )
    else:
        st.info("💡 Tryb GEM ładuje odpowiednie aktywa, aby sprawdzić, co wygrywa w strategii Dual Momentum.")
        wersja_gem = st.selectbox("Wersja strategii:", ["Oryginalna (USA)", "Europejska (UCITS - XTB)"])

        if wersja_gem == "Oryginalna (USA)":
            wybrane_nazwy = list(GEM_ORIGINAL.keys())
        else:
            wybrane_nazwy = list(GEM_ZAWOD_INWESTOR.keys())

        st.multiselect("Instrumenty badane w tej strategii:", wybrane_nazwy, default=wybrane_nazwy, disabled=True)

    period = st.selectbox("Period", ("1 Month", "6 Months", "1 Year", "5 Years"))

    start_date = dt.date.today() - getDate(period)
    end_date = dt.date.today()

    st.markdown("---")

    oblicz_klikniety = st.button("Oblicz stopy zwrotu", type="primary", use_container_width=True)


if oblicz_klikniety:
    if not wybrane_nazwy:
        st.warning("Wybierz chociaż jeden indeks z listy.")
    else:
        with st.spinner("Pobieranie danych z giełdy..."):

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
    st.title("📊 Analityczny Dashboard Giełdowy")
    st.markdown("Witaj w narzędziu do analizy stóp zwrotu instrumentów finansowych.")

    st.info(
        "👈 Skonfiguruj parametry w **panelu po lewej stronie**,"
        " a następnie kliknij czerwony przycisk **Oblicz stopy zwrotu**,"
        " aby wygenerować wykres.")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔍 Co potrafi aplikacja?")
        st.markdown(
            "- Porównywanie wielu indeksów i ETF-ów jednocześnie\n"
            "- Automatyczna normalizacja cen do bazy 100\n"
            "- Generowanie interaktywnych wykresów w czasie rzeczywistym"
        )
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>"
    "Zaprojektowane i zakodowane przez <a href='https://smichurski.pl' target='_blank'>Łukasza Śmichurskiego</a> | "
    "Wersja 1.0"
    "</div>",
    unsafe_allow_html=True
)
import yfinance as yf
import datetime as dt
import dateutil.relativedelta as rd
import streamlit as st

def getDate(period):
    match period:
        case "1 Month": return rd.relativedelta(months=1)
        case "6 Months": return rd.relativedelta(months=6)
        case "1 Year": return rd.relativedelta(years=1)
        case "5 Years": return rd.relativedelta(years=5)

@st.cache_data
def fetch_data(tickers, start_date, end_date):
    data = yf.download(tickers, start_date, end_date)
    return data['Close']
# 📈 Fintech Portfolio & Strategy Dashboard

> An interactive web application for portfolio analysis, financial instrument return comparison, and quantitative strategy automation (Dual Momentum / GEM).

---

Link: https://stock-market-app-smichurski.streamlit.app

---
## 🚀 About the Project
This project was created for modern investors looking for tools based on hard data and proven quantitative strategies. The application combines clean software architecture with advanced visualization of real-time market data fetched from Yahoo Finance.

### Key Features:
* **Two Analysis Modes:** 
  * *Custom Portfolio:* Freely compare any stock indices, equities, or cryptocurrencies.
  * *GEM Strategy (Global Equities Momentum):* Implementation of Gary Antonacci's famous Dual Momentum strategy in two variants – **Original (USA / SPY)** and **European (UCITS ETFs for XTB)**.
* **Automatic Normalization:** Recalculating historical valuations to a base of 100, enabling a reliable comparison of growth dynamics across different assets on a single chart.
* **Professional UI/UX:** KPI tiles (`st.metric`) with dynamic profit/loss coloring, a dark theme for charts (`Plotly`), and a responsive layout with a sidebar.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Web Framework:** Streamlit (optimized for responsiveness and wide layout)
* **Data Analysis:** Pandas, NumPy
* **Visualizations:** Plotly Express
* **Data Source:** yfinance (with data caching via `@st.cache_data`)
* **Version Control:** Git / GitHub

---

## 📂 Project Architecture
The project is designed following the *Separation of Concerns* principle:

```text
Stock_Market_App/
├── app.py              # Main UI presentation layer (Streamlit)
├── logic.py            # Business logic, time-series processing, and API
├── config.py           # Asset dictionaries (Indices, US & UCITS ETFs)
├── requirements.txt    # Project dependencies
└── .gitignore          # Files ignored by Git
import streamlit as st
import requests
from datetime import datetime

st.title("💹 Velor Forex Pair Price Fetche")

base = st.text_input("Base Currency (e.g., USD)", "USD").upper()
quote = st.text_input("Quote Currency (e.g., JPY)", "JPY").upper()

if st.button("Get Rate"):
    url = f"https://api.exchangerate.host/latest?base={base}"
    resp = requests.get(url).json()
    if "rates" in resp and quote in resp["rates"]:
        rate = resp["rates"][quote]
        st.success(f"{base}/{quote}: {rate:.4f}")
        st.caption(f"Updated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.error("Invalid currency code or API error.")

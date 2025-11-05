import streamlit as st
import requests
from datetime import datetime

st.title("💹 Velor Forex Pair Price Fetcher")

base = st.text_input("Base Currency (e.g., USD)", "USD").upper()
quote = st.text_input("Quote Currency (e.g., JPY)", "JPY").upper()

if st.button("Get Rate"):
    url = f"https://v6.exchangerate-api.com/v6/4a02b25dd20ca0b9c6ab5dfa/latest/{base}"
    resp = requests.get(url).json()
    if "rates" in resp and quote in resp["rates"]:
        rate = resp["rates"][quote]
        st.success(f"{base}/{quote}: {rate:.4f}")
        st.caption(f"Updated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.error("Invalid currency code or API error.")

"""Page demonstrating API client interactions."""

import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"


@st.cache_resource
def get_session():
    return requests.Session()


st.header("API Client")
st.caption("Interacting with FastAPI backend endpoints")

if "api_counter_value" not in st.session_state:
    st.session_state.api_counter_value = 0

session = get_session()

st.subheader(f"Counter: {st.session_state.api_counter_value}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Decrement", icon="⬇️", width="stretch"):
        try:
            r = session.post(
                f"{API_BASE_URL}/counter/decrement",
                json={"value": st.session_state.api_counter_value, "amount": 1},
                timeout=5,
            )
            r.raise_for_status()
            st.session_state.api_counter_value = r.json()["result"]
            st.rerun()
        except requests.RequestException as e:
            st.toast(f"API error: {e}", icon="🚨")

with col2:
    if st.button("Reset", icon="🔄", width="stretch", type="secondary"):
        st.session_state.api_counter_value = 0
        st.rerun()

with col3:
    if st.button("Increment", icon="⬆️", width="stretch"):
        try:
            r = session.post(
                f"{API_BASE_URL}/counter/increment",
                json={"value": st.session_state.api_counter_value, "amount": 1},
                timeout=5,
            )
            r.raise_for_status()
            st.session_state.api_counter_value = r.json()["result"]
            st.rerun()
        except requests.RequestException as e:
            st.toast(f"API error: {e}", icon="🚨")

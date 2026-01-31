"""Page demonstrating API client interactions."""

import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

st.header("API Client")
st.markdown("This page interacts with the FastAPI backend endpoints.")

# Health check section
st.subheader("API Health Check")
if st.button("Check API Health"):
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        response.raise_for_status()
        st.success(f"API is healthy: {response.json()}")
    except requests.ConnectionError:
        st.error("Cannot connect to API. Is the server running?")
    except requests.Timeout:
        st.error("Request timed out.")
    except requests.HTTPError as e:
        st.error(f"HTTP error: {e.response.status_code}")

st.divider()

# Counter operations section
st.subheader("Counter Operations")

# Initialize session state for API counter value
if "api_counter_value" not in st.session_state:
    st.session_state.api_counter_value = 0

# Display current value
st.metric("Current Value", st.session_state.api_counter_value)

# Controls
col1, col2, col3 = st.columns(3)

with col1:
    amount = st.number_input("Amount", min_value=1, value=1, key="api_amount")

with col2:
    if st.button("Increment", key="api_inc", use_container_width=True):
        try:
            response = requests.post(
                f"{API_BASE_URL}/counter/increment",
                json={"value": st.session_state.api_counter_value, "amount": amount},
                timeout=5,
            )
            response.raise_for_status()
            st.session_state.api_counter_value = response.json()["result"]
            st.rerun()
        except requests.ConnectionError:
            st.error("Cannot connect to API. Is the server running?")
        except requests.Timeout:
            st.error("Request timed out.")
        except requests.HTTPError as e:
            st.error(f"HTTP error: {e.response.status_code}")

with col3:
    if st.button("Decrement", key="api_dec", use_container_width=True):
        try:
            response = requests.post(
                f"{API_BASE_URL}/counter/decrement",
                json={"value": st.session_state.api_counter_value, "amount": amount},
                timeout=5,
            )
            response.raise_for_status()
            st.session_state.api_counter_value = response.json()["result"]
            st.rerun()
        except requests.ConnectionError:
            st.error("Cannot connect to API. Is the server running?")
        except requests.Timeout:
            st.error("Request timed out.")
        except requests.HTTPError as e:
            st.error(f"HTTP error: {e.response.status_code}")

# Reset button
if st.button("Reset Counter", key="api_reset"):
    st.session_state.api_counter_value = 0
    st.rerun()

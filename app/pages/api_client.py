"""Page demonstrating API client interactions."""

import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

st.header("API Client")
st.caption("Interacting with FastAPI backend endpoints")

# Initialize session state
if "api_counter_value" not in st.session_state:
    st.session_state.api_counter_value = 0
if "api_last_value" not in st.session_state:
    st.session_state.api_last_value = 0
if "api_status" not in st.session_state:
    st.session_state.api_status = None


def check_health():
    """Check API health status."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        response.raise_for_status()
        return True, response.json()
    except requests.ConnectionError:
        return False, "Cannot connect to API. Is the server running?"
    except requests.Timeout:
        return False, "Request timed out."
    except requests.HTTPError as e:
        return False, f"HTTP error: {e.response.status_code}"


def call_counter_api(endpoint: str, value: int, amount: int):
    """Call counter increment/decrement endpoint."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/counter/{endpoint}",
            json={"value": value, "amount": amount},
            timeout=5,
        )
        response.raise_for_status()
        return True, response.json()["result"]
    except requests.ConnectionError:
        return False, "Cannot connect to API"
    except requests.Timeout:
        return False, "Request timed out"
    except requests.HTTPError as e:
        return False, f"HTTP error: {e.response.status_code}"


# Status indicator
status_col, health_col = st.columns([3, 1])
with health_col:
    if st.button("Check Health", use_container_width=True):
        success, result = check_health()
        st.session_state.api_status = (success, result)

with status_col:
    if st.session_state.api_status:
        success, result = st.session_state.api_status
        if success:
            st.success(f"API healthy: {result}", icon="✅")
        else:
            st.error(result, icon="🚨")

st.divider()

# Calculate delta for metric
current = st.session_state.api_counter_value
delta = (
    current - st.session_state.api_last_value
    if st.session_state.api_last_value != current
    else None
)

# Counter display
col_display, col_controls = st.columns([1, 2])

with col_display:
    st.metric("Counter", current, delta=delta)

with col_controls:
    amount = st.slider(
        "Step amount", min_value=1, max_value=10, value=1, key="api_slider"
    )

    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        if st.button("➖", key="api_dec", use_container_width=True, help="Decrement"):
            success, result = call_counter_api("decrement", current, amount)
            if success:
                st.session_state.api_last_value = current
                st.session_state.api_counter_value = result
                st.rerun()
            else:
                st.error(result)

    with btn_col2:
        if st.button(
            "Reset", key="api_reset", use_container_width=True, type="secondary"
        ):
            st.session_state.api_last_value = 0
            st.session_state.api_counter_value = 0
            st.rerun()

    with btn_col3:
        if st.button(
            "➕",
            key="api_inc",
            use_container_width=True,
            type="primary",
            help="Increment",
        ):
            success, result = call_counter_api("increment", current, amount)
            if success:
                st.session_state.api_last_value = current
                st.session_state.api_counter_value = result
                st.rerun()
            else:
                st.error(result)

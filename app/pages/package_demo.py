"""Page demonstrating direct usage of example_pkg."""

import streamlit as st

from example_pkg import Counter

st.header("Package Demo")
st.caption("Direct usage of the `example_pkg.Counter` class")

# Initialize session state
if "counter" not in st.session_state:
    st.session_state.counter = Counter()
if "last_value" not in st.session_state:
    st.session_state.last_value = 0

# Calculate delta for metric
current = st.session_state.counter.value
delta = (
    current - st.session_state.last_value
    if st.session_state.last_value != current
    else None
)

# Counter display
col_display, col_controls = st.columns([1, 2])

with col_display:
    st.metric("Counter", current, delta=delta)

with col_controls:
    amount = st.slider("Step amount", min_value=1, max_value=10, value=1)

    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        if st.button("➖", use_container_width=True, help="Decrement"):
            st.session_state.last_value = current
            st.session_state.counter.decrement(amount)
            st.rerun()
    with btn_col2:
        if st.button("Reset", use_container_width=True, type="secondary"):
            st.session_state.last_value = 0
            st.session_state.counter = Counter()
            st.rerun()
    with btn_col3:
        if st.button("➕", use_container_width=True, type="primary", help="Increment"):
            st.session_state.last_value = current
            st.session_state.counter.increment(amount)
            st.rerun()
